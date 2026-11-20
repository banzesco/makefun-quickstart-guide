"""Capture the real public GitHub README, never a mockup.

Run from this repository: python capture_screenshot.py --check-only
After uploading README.md: python capture_screenshot.py
Requires Playwright only for capture; checks use Python's standard library.
"""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import struct
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
REPOSITORY = "banzesco/makefun-quickstart-guide"
PAGE_URL = f"https://github.com/{REPOSITORY}"
API_URL = f"https://api.github.com/repos/{REPOSITORY}"
REFERRAL = "76vh6q35"
MAX_IMAGE_BYTES = 8_000_000
MAX_PIXELS = 16_000_000


class CaptureError(Exception):
    """A prerequisite or capture check failed; no screenshot is published."""


def public_json(url):
    """Use only unauthenticated public requests; never read credentials."""
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "makefun-quickstart-guide-public-capture",
    })
    try:
        with urlopen(request, timeout=40) as response:
            if response.status != 200:
                raise CaptureError(f"Public GitHub check returned {response.status}.")
            return json.load(response)
    except HTTPError as error:
        raise CaptureError(
            f"Public GitHub check returned HTTP {error.code}; "
            "check publication, connectivity and unauthenticated rate limits."
        ) from error
    except (URLError, TimeoutError, OSError, ValueError) as error:
        raise CaptureError(f"Could not verify public GitHub state: {error}") from error


def verify_public_readme():
    local = ROOT / "README.md"
    if not local.is_file():
        raise CaptureError("README.md is missing beside the capture script.")
    local_bytes = local.read_bytes()
    metadata = public_json(API_URL)
    if metadata.get("private") is not False:
        raise CaptureError("Repository is not confirmed public.")
    if metadata.get("full_name") != REPOSITORY:
        raise CaptureError("GitHub returned a different repository.")
    if metadata.get("html_url") != PAGE_URL:
        raise CaptureError("Repository moved; inspect its identity before capturing.")
    branch = metadata.get("default_branch")
    if not branch:
        raise CaptureError("GitHub returned no default branch.")
    remote = public_json(API_URL + "/readme?" + urlencode({"ref": branch}))
    if remote.get("path") != "README.md" or remote.get("type") != "file":
        raise CaptureError("The displayed README is not the root README.md.")
    if remote.get("encoding") != "base64":
        raise CaptureError("GitHub did not return verifiable README content.")
    try:
        encoded = "".join(remote["content"].split())
        remote_bytes = base64.b64decode(encoded, validate=True)
    except (KeyError, ValueError, TypeError) as error:
        raise CaptureError("GitHub README content could not be decoded.") from error
    if remote_bytes != local_bytes:
        raise CaptureError(
            "Public README differs from local README.md. Upload the final file "
            "to the default branch first (including matching line endings). "
            "No screenshot was created."
        )
    text = local_bytes.decode("utf-8")
    if REFERRAL not in text or "# make.fun: your first bounty" not in text:
        raise CaptureError("The final guide heading or referral code is missing.")
    return {"branch": branch, "readme_sha256": hashlib.sha256(local_bytes).hexdigest()}


def validate_png(data):
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise CaptureError("Browser output is not a PNG with an IHDR header.")
    width, height = struct.unpack(">II", data[16:24])
    if not width or not height or width * height > MAX_PIXELS:
        raise CaptureError(f"PNG dimensions fail the pixel limit: {width} x {height}.")
    if len(data) > MAX_IMAGE_BYTES:
        raise CaptureError("PNG exceeds the conservative 8,000,000-byte limit.")
    return {"width": width, "height": height, "bytes": len(data)}


def capture():
    output = ROOT / "screenshot.png"
    if output.exists():
        raise CaptureError("screenshot.png already exists; refusing to overwrite it.")
    verified = verify_public_readme()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as error:
        raise CaptureError(
            "Install capture tools first: python -m pip install playwright; "
            "then python -m playwright install chromium."
        ) from error
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                # Fresh, unsigned-in context. No stored profile, cookies or secrets.
                context = browser.new_context(
                    viewport={"width": 1440, "height": 1600},
                    device_scale_factor=1,
                    color_scheme="light",
                    locale="en-US",
                )
                page = context.new_page()
                response = page.goto(PAGE_URL, wait_until="domcontentloaded", timeout=60000)
                if response is None or response.status != 200:
                    raise CaptureError("The real public GitHub page did not return HTTP 200.")
                if page.url.rstrip("/") != PAGE_URL:
                    raise CaptureError("The browser did not remain on the intended repository.")
                article = page.locator("article.markdown-body").first
                article.wait_for(state="visible", timeout=30000)
                article_text = article.inner_text()
                if "make.fun: your first bounty, without the guesswork" not in article_text:
                    raise CaptureError("GitHub has not rendered the final guide heading.")
                if REFERRAL not in article_text:
                    raise CaptureError("The visible README has no referral code.")
                badges = article.locator('img[src*="bring-the-humans-02"]')
                if badges.count() != 3:
                    raise CaptureError("The rendered guide does not show exactly three bounty badges.")
                for badge in badges.all():
                    badge.wait_for(state="visible", timeout=30000)
                page.wait_for_function(
                    """() => [...document.querySelectorAll('article.markdown-body img')]
                    .filter(i => i.src.includes('bring-the-humans-02'))
                    .every(i => i.complete && i.naturalWidth > 0)""",
                    timeout=30000,
                )
                page.evaluate("document.fonts.ready")
                # Only scroll the real page: do not restyle or replace its contents.
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(1200)
                image = page.screenshot(type="png", full_page=False, animations="disabled")
                limits = validate_png(image)
                # Fail closed if a concurrent publication changed the README mid-capture.
                if verify_public_readme() != verified:
                    raise CaptureError("README state changed during capture; retry after inspection.")
            finally:
                browser.close()
    except CaptureError:
        raise
    except Exception as error:
        raise CaptureError(f"Browser capture failed; no image saved: {error}") from error
    # Only verified browser pixels reach disk. Exclusive create protects existing evidence.
    with output.open("xb") as file:
        file.write(image)
    return {"file": str(output), "page": PAGE_URL, **verified, **limits}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="Verify publication without capturing.")
    args = parser.parse_args()
    try:
        result = verify_public_readme() if args.check_only else capture()
        print(json.dumps({"verified": True, "captured": not args.check_only, **result}, indent=2))
        return 0
    except (CaptureError, OSError, UnicodeError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
