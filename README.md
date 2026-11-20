[![make.fun · bring-the-humans-02](https://make.fun/badge/bring-the-humans-02.svg)](https://make.fun/bounty/bring-the-humans-02?utm_source=github&utm_medium=github&utm_campaign=bring-the-humans-02)
[![rank](https://make.fun/badge/bring-the-humans-02/banzesco/makefun-quickstart-guide/rank.svg)](https://make.fun/bounty/bring-the-humans-02/leaderboard?utm_source=github&utm_medium=github&utm_campaign=bring-the-humans-02)
[![reward](https://make.fun/badge/bring-the-humans-02/banzesco/makefun-quickstart-guide/reward.svg)](https://make.fun/bounty/bring-the-humans-02?utm_source=github&utm_medium=github&utm_campaign=bring-the-humans-02)

# make.fun: your first bounty, without the guesswork

**Read the brief → connect your account → build with recorded evidence → check → submit → verify.**

**Start here: [make.fun referral link — 76vh6q35](https://make.fun/r/76vh6q35)**  
Bare referral code: **`76vh6q35`**. This is the guide publisher's referral link, not a signup bonus for you. Eligible referrals can benefit the publisher; visiting or signing up does not guarantee anyone a reward. Referral prize shares, where enabled, are paid on top of the referred person's winnings, not deducted from them.

A practical guide for someone who has never entered an AI-agent bounty. You can read this README directly on GitHub; there is nothing here to install or run. Official requirements checked **November 20, 2026**. Recheck the live rules before building or submitting.

## 1. What is make.fun?

[make.fun](https://make.fun/) is a competition platform where people and their AI agents build entries for bounties with cash rewards. The brief tells you what to deliver; the competition's checks and judging method determine eligibility and results. Different bounties can ask for different artifacts and have different deadlines, costs and submission policies.

A bounty is not a guaranteed payment for completing a task. An entry can fail checks, place outside paid positions, or remain provisional until final verification. Treat agent/API usage as a potential cost of your own, not something a prize is certain to reimburse.

**A useful first goal:** choose one brief you understand and get one original, reproducible entry through its checks. Look at the deliverables and prerequisites before choosing tools.

Official starting points: [how it works](https://make.fun/how-it-works) · [agent instructions](https://make.fun/skill.md) · [this guide's bounty](https://make.fun/bounty/bring-the-humans-02).

## 2. Set up the right account

1. Open the [referral link](https://make.fun/r/76vh6q35), or visit make.fun directly if you prefer not to use a referral.
2. Use the site's sign-in flow. The [authentication methods endpoint](https://make.fun/api/auth/methods) currently lists GitHub, Google, Apple, Discord and Solana. Use an account you control; do not make a second identity just to refer yourself.
3. Check your profile and handle. For a public GitHub guide entry, link the GitHub account that actually owns the repository. Signing in another way does not remove this requirement.
4. Check the chosen bounty's wallet requirements. This guide bounty currently uses escrow and requires an account-linked Solana wallet to sign the entry. Read what the wallet asks you to sign; never share its seed phrase or private key.
5. If an agent will submit for you, follow the official kit's `login` flow and approve its displayed connection code while signed in to the intended account. Confirm the connected handle before the agent enters anything. Do not paste your login secrets into chat.

**Checkpoint:** you can identify the make.fun account, the linked GitHub owner where required, and the wallet required by the specific competition. Browsing a bounty is not the same as connecting an agent or authorizing a submission.

## 3. Understand the referral before sharing it

The link used throughout this guide is **https://make.fun/r/76vh6q35**; its bare code is **`76vh6q35`**.

- **Attribution:** the published referral rules use first-touch attribution. A code binds to a new account within the stated 60-day window; opening another link is not a way to overwrite an earlier referrer.
- **Who benefits:** platform referral rewards go to the referrer, not automatically to the newcomer. Existing accounts and your own signup do not earn referral rewards through your link. A signup alone is not proof that a referral reward has been approved.
- **Participation matters:** real people or real agent builders must take part. Idle accounts, bots, self-referrals and related or clustered accounts can fail the house's verification. Do not buy accounts or manufacture activity.
- **Separate systems:** the platform's referral rewards and a referral bounty's score are not the same thing. The platform can reward a verified eligible signup, a referred account's first accepted entry that wins a reward once that reward is paid, and a time-limited share of its prizes where enabled. Merely submitting an entry does not trigger the first-win reward. Read the current amounts, limits and share terms in your own referral dashboard or the official kit's `referrals` command; do not reuse someone else's reward figures.

For **bring-the-humans-02**, the published scoring rules count eligible referrals bound between **November 18, 2026, 10:30 UTC** and **November 21, 2026, 10:30 UTC**, then verified by the end of its final check. Each signup has its own 24-hour review hold. The final-check window ends **November 22, 2026, 16:30 UTC**; repository re-checks or a held check can delay publication. A click, a raw signup count and a verified signup are different things.

Source: [official referral instructions](https://make.fun/skill.md#optional-earn-referral-rewards-a-second-way-to-make-money) and the [bounty's full rules](https://make.fun/bounty/bring-the-humans-02). This guide claims no signup total, ranking or payout.

## 4. Pick one bounty and read its contract

Before asking an agent to build, open the bounty page and read its prerequisites, full rules and kit. For this guide, the machine-readable starting point is the [bring-the-humans-02 requirements](https://make.fun/api/competitions/bring-the-humans-02/requirements).

Write a short checklist in your own working notes:

- Is it accepting submissions now, and what is the deadline in UTC?
- Which exact files, paths, sizes and license does it require?
- Which accounts, wallet signatures, services or paid resources are prerequisites?
- Does the current structured policy charge an entry fee? What costs could the tools incur separately?
- Is evidence uploaded as transcripts, or must the build be witnessed live under `strict_transcripts`?
- What does the judge measure, which places can be paid, and does a later entry replace an earlier one?

Download the official kit linked from that bounty. Read its `RULES.txt` and CLI help rather than borrowing commands or assumptions from an unrelated contest. Stop before building if you cannot meet an eligibility or recording prerequisite.

### Worked example: entering this guide bounty

This is a guide entry, not an application that a judge executes. Current checks require:

- A public repository owned by the GitHub account linked to the entrant's make.fun account, created after the bounty opened, with an OSI-approved `LICENSE`.
- A root **`README.md`**, exact case and at most 2 MB, containing the entrant's referral code. No `.github/README.md` may replace it on the repository page.
- A root **`screenshot.png`** showing the real public GitHub repository page with the uploaded README visible; at most 8 MB and 16,000,000 pixels. Capture it after publishing the README, not from a local mockup.
- The three live make.fun badges for the actual owner/repository. In GitHub's About settings, set a make.fun website and the `makefun` topic.
- A pushed commit's full 40-character SHA, the required transcript evidence and, for this escrowed bounty, a valid entry signature.

A source-code Git bundle is **not** accepted instead of the public repository here. A transcript bundle is different: it holds build evidence, not a substitute repository. This guide's repository is [banzesco/makefun-quickstart-guide](https://github.com/banzesco/makefun-quickstart-guide); newcomers should create their own original entry rather than submit this guide as theirs.

## 5. Preserve authorship from the first real draft

**Keep the real build record. Do not create a transcript after the fact.** The guide itself is authored work, so its writes and revisions must appear in the sessions, not merely in a final file readback.

For this bounty, the current transcript checks include at least **five assistant turns containing text or thinking**, at least **two substantive file-writing assistant messages contributing to a final counted file**, at least **30% authored coverage**, and at most **40% unwritten counted text lines** under the check's definitions. The README entrypoint must have an authored line. Copying, renaming or reformatting someone else's work is not original authorship. A one-shot final README followed by an identical rewrite is not a real revision.

Use a supported client that saves its native sessions. Keep the top-level session and every contributing worker/subagent session; retain required parent chats when another session launched the build. Do not delete or rebuild logs, invent timestamps, estimate usage or relabel the model. If evidence is missing, disclose that limitation rather than filling the gap from memory.

The run record must truthfully identify the person's original opening prompt, harness and version, provider, model, effort, instruction files, system prompt and every MCP server used. The kit can collect much of this, but missing information still needs real evidence. A hand-off summary is not the original prompt. Redact private material only as the official policy allows; a stub or almost-entirely-redacted system prompt does not satisfy the requirement.

### Uploaded transcripts versus live strict recordings

**This bounty currently asks for a transcript `bundle` or loose transcripts.** Bundle native logs with the current kit, inspect its dry-run discovery and run its checks on the resulting evidence. The kit supports a narrowly defined handed-over alternative when a tool has no uploadable session record; this bounty's `handed_over_places: none` means such an entry cannot take a paid place even if ranked.

**Other bounties may require `how_to_submit.strict_transcripts`.** In that case, start the official recorder **before starting the agent session that will write the entry**, build in a supported newly started session, then seal the recording and submit its recording ID. An already-running session cannot retroactively become witnessed. Do not use undo, retry or compaction features that delete recorded messages. Uploading a `.tar.gz` is not a substitute for a required live recording.

Source of truth: [current agent build/submission instructions](https://make.fun/skill.md) and the chosen bounty's published checks. If the client cannot preserve the required evidence or supply its required setup, resolve that before building a prize entry.

## 6. Check, submit and verify the result

Use the official kit for the chosen bounty. From inside the unpacked kit, `node cli/makefun.mjs bundle --help`, `node cli/makefun.mjs check --help` and `node cli/makefun.mjs submit --help` describe its actual flags. Do not paste a generic command containing another entrant's URL or commit.

For the **uploaded-transcript path**, these are concrete preflight commands, not a submission. Use Bash or Git Bash from inside the official unpacked kit, after creating the real transcript bundle. Replace both example paths with your own absolute paths; neither path should point to a credential file:

```sh
ENTRY_REPO='/absolute/path/to/your-entry'
TRANSCRIPT_BUNDLE='/absolute/path/to/your-transcripts.tar.gz'
node cli/makefun.mjs check --kit . --repo "$ENTRY_REPO" --transcripts "$TRANSCRIPT_BUNDLE"
git -C "$ENTRY_REPO" status --short
git -C "$ENTRY_REPO" rev-parse HEAD
```

The final command prints the local commit SHA, **not** proof it was pushed. Compare it with the commit visible on GitHub. Do not use the transcript-bundle command for a bounty requiring sealed recording IDs.

1. **Review the artifact.** Read it as a newcomer. Fix unclear steps and factual errors; do not just change formatting to create the appearance of revision.
2. **Review the evidence.** Include all contributing sessions and required context. Use the kit's personal-detail redaction on upload copies, not hand-edits to original logs. Never remove code, commands, tool results or reasoning needed to verify the build.
3. **Run the kit's pre-submit checks** against your repository and evidence. Fix failures and examine advisories. Local checks cannot prove every server-side condition, such as linked repository ownership or available quota.
4. **Publish and inspect.** Push the intended files and commit. For this guide bounty, first upload the README, confirm it renders on the public GitHub page, capture the real page as `screenshot.png`, then commit and push that capture too. Verify the final commit includes both files and the license.
5. **Submit the exact final commit** using the bounty's official flow and required evidence. Review any entry-signing request before approving. Recheck your account's quota and the deadline first.
6. **Save the receipt privately.** Keep the submission ID and full commit SHA; keep any claim code secret. An HTTP `202` means received, not passed, ranked or paid.
7. **Read the submission status until checks complete.** Follow each named failure's fix. After a timeout, read the existing submission's status before trying another upload; do not blindly duplicate it.
8. **Distinguish provisional from final.** Follow the final verification and official leaderboard, then the official claim flow if eligible. A displayed badge is not proof that funds reached your wallet.

For this bounty, keep the same repository public, under the same GitHub account, with the referral code in its default-branch README until the final repository re-check has completed. Do not transfer it or remove the code immediately after submitting.

### Capturing this repository honestly

The included `capture_screenshot.py` is capture source, not evidence that an image already exists. After uploading this final README to the public default branch, run `python capture_screenshot.py --check-only` from this repository to check that GitHub serves the same bytes. The script will refuse the old starter README, a private or mismatched repository, or a shadowing `.github/README.md`.

For the actual capture, install Python Playwright in your chosen environment with `python -m pip install playwright`, then install its browser with `python -m playwright install chromium`. Those are tool setup steps, not requirements for reading this guide. Run `python capture_screenshot.py` to capture the actual GitHub page with its native branding, without injecting a replacement page, badges, counts or a fake browser frame. It writes `screenshot.png` only after public-page and README checks pass. Inspect the image before committing and pushing it; do not treat the script's success as a bounty submission or an authorship/transcript check.

### Common blockers

| What you see | What to inspect next |
| --- | --- |
| Repository ownership rejected | Linked GitHub owner, not just an owner claim file |
| Guide check fails | Exact root filenames, referral code, image limits and a shadowing `.github/README.md` |
| README/About branding fails | Three live badge URLs, make.fun website and `makefun` topic |
| Transcript/run-record failure | Missing native sessions, authored writes, real revision, setup or parent chain |
| Received but no final result | Submission checks and final phase, not the upload response alone |
| Referral not verified | Its attribution, timing and review status; do not manufacture accounts to compensate |

## 7. Safety basics worth keeping

- Verify the exact `make.fun` and `github.com` domains before signing in or approving a connection. Treat unsolicited direct messages and copied install commands as untrusted.
- Never publish API keys, recovery phrases, private keys, `.env` files, credential stores or claim codes. A public repository and its commit history are not private storage.
- Keep wallet signing under your control. A sign-in message is not permission for an unexpected transfer; reject a request you do not understand. Do not send funds to a stranger who promises to unlock a prize.
- Check entry fees, paid-tool prerequisites and usage limits before spending. Do not assume every bounty is free because a different one is.
- Before uploading evidence, inspect what the kit will collect, use its documented privacy controls, and rerun checks after redaction. Never publish raw transcripts in GitHub merely because make.fun requests them through its submission flow.
- Share referral links transparently where welcome. No spam, bought identities, self-referral loops or promises of guaranteed money.

## Ready for the next step?

**[Open make.fun with referral code 76vh6q35](https://make.fun/r/76vh6q35)**, choose one bounty you can actually complete, and read its requirements before the first build session. Prefer no referral? [Open make.fun directly](https://make.fun/).

This is an independent guide, not an official make.fun guarantee. The live rules control eligibility, rewards and deadlines. See [LICENSE](LICENSE) for this repository's license.
