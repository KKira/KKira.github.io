---
description: Add an idea or bug to docs/backlog.md as a numbered item in the right section
argument-hint: <idea or bug, in your own words>
---

Add this to the backlog: `$ARGUMENTS`

1. If the text is empty, ask the owner what to add and stop.
2. Read `docs/backlog.md` from the latest `master` (`git fetch origin --prune`, then `git show origin/master:docs/backlog.md`; in Git Bash put `MSYS_NO_PATHCONV=1` in front). Pick the section it belongs to (Site & design, CV, Portfolio, Games, Dance, Music, Hobbies, Journal, Hosting & SEO…). If none fits, add a new numbered section at the end.
3. Add it as the next number in that section (e.g. after `3.4` comes `3.5`), written as one or two plain-language sentences. Start bugs with "Bug:". Keep the owner's meaning; don't add scope they didn't ask for.
4. If a similar item already exists, don't add a duplicate. Update that item instead and say so.
5. Work on a branch: never commit on `master`. Create `docs/backlog-<short-topic>` from `origin/master` (`git switch --no-track -c <name> origin/master`). Commit with a message that names the item number.
6. Reply with the item exactly as added, its number, and the branch. Offer `/pr` so the Main live session can merge it with `/mp`. Don't merge it yourself.

Note: the default branch is `master` today; it may be renamed `main` later. If `origin/master` doesn't exist, use `origin/main`.
