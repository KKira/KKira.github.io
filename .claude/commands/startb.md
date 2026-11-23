---
description: Start a new work session from a backlog item (e.g. /startb 5.1)
argument-hint: <backlog number> [extra notes]
---

Start a new Claude Code session for one backlog item. Arguments: `$ARGUMENTS`

The first word is the backlog number (`5.1`, `9.2`); anything after it is extra notes from the owner for that session. "start 5.1" typed in a message means the same, and so does the **Start** button in the Backlog panel (it types `/startb <number>` in the prompt box for you).

This command only **starts** the session. It changes no files, makes no branch here and commits nothing; the new session does the work.

The default branch is `master` today (it may be renamed `main` later; if `origin/master` doesn't exist, use `origin/main` everywhere below).

1. **Number given?** If there is no number, ask the owner which item and stop.
2. **Read the item from the latest `master`.** `git fetch origin --prune`, then read `docs/backlog.md` from `origin/master` (`git show origin/master:docs/backlog.md`; in Git Bash put `MSYS_NO_PATHCONV=1` in front). Find the line `- <number> ...` and the indented lines under it.
   - Not found: say so, list the closest numbers in that section, and stop.
   - Marked `Done (vX)`: say it is done and ask whether to start anyway (for example to finish a "Still to do" part). Stop until the owner answers. `Partly done` items are fine: the task is the part still to do.
3. **Build the branch name** `<type>/<n-n-short-topic>` (the rules in `/createb`):
   - `type`: `fix` if the item is about something broken or wrong (a bug, "fails", "doesn't", "wrong"); `docs` if it only touches docs, notes or `.claude/commands`; `feature` otherwise.
   - topic: the backlog number with dots as hyphens, then 2–4 short words that say what it is: lowercase, letters, digits and hyphens only. Example: 5.1 "Dance page: add dance videos" → `feature/5-1-dance-videos`.
   - Check it fits `^(feature|fix|docs)/[a-z0-9]+(-[a-z0-9]+)*$` and is not used yet: no local branch (`git show-ref --verify --quiet refs/heads/<name>`), none on GitHub (`git ls-remote --heads origin <name>`), no merged pull request (`gh pr list --state merged --head <name>`). If it is taken, add `-2` (then `-3`…).
4. **Start the session** with `start_session`: `initiation: "user_asked"` (the owner asked for it with this command), `context: "fresh"`, `use_worktree: true` (its own worktree), `source_branch: "master"`, `title`: `<number> <short item title>` (under 60 characters), `branch_name`: the topic part of the name (e.g. `5-1-dance-videos`).
   - `prompt`: exactly one line, `/createb <branch name> <item text>`, the item text being the item without its `- ` bullet and with its sub-lines joined on, followed by the owner's extra notes if any. Example: `/createb feature/5-1-dance-videos 5.1 Dance page: add dance videos, hosted on YouTube or Vimeo and embedded.`
   - `background` (needed for a fresh session): "avega.dev personal website (Astro, deployed by Netlify from master). One session = one task = one branch = one pull request; end with /pr. Never merge into master; the Main live session does that with /mp."
5. **Report in two lines:** the session (as a link), its branch name, and the item it works on. Don't do any of the item's work here.

If the app refuses to start a session from here (for example the turn was not started by the owner), propose it instead (`initiation: "own_initiative"`, same title, prompt and background) so the owner starts it with one click on the card.
