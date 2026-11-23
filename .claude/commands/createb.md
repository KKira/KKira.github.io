---
description: Create a branch from the latest master, then do the task on it
argument-hint: <type>/<short-topic> [what to do on it]
---

Create a new branch and work on it. Arguments: `$ARGUMENTS`

The first word is the branch name; anything after it is the task to do on the branch.

The default branch is `master` today (it may be renamed `main` later; if `origin/master` doesn't exist, use `origin/main` everywhere below).

**Branch rules (agreed with the owner):** every task gets a **new** branch cut from the latest `origin/master`; a branch is never reused once it was merged; names say what is inside, in the form `<type>/<short-topic>`; branches are short-lived (one session = one task = one branch = one pull request).

1. **Name given?** If the first word is missing, ask the owner for a branch name and stop.
2. **Name format.** A good name is `<type>/<short-topic>`:
   - `type` is one of `feature` (new or changed content or behaviour), `fix` (something broken) or `docs` (docs, commands, notes only);
   - `short-topic` is a few lowercase words joined by hyphens (letters, digits, hyphens only), optionally starting with the backlog number, e.g. `feature/5-1-dance-videos`, `fix/1-3-broken-menu`, `docs/createb-rules`.
   - Check: `^(feature|fix|docs)/[a-z0-9]+(-[a-z0-9]+)*$`.
   - If the name doesn't fit (no type, capitals, spaces, underscores, a vague topic), **don't block silently and don't create it yet**: say what doesn't fit, suggest a name in the right form (pick the type from the task), and ask the owner to confirm or give another. Stop until they answer, then continue with the confirmed name.
3. **Uncommitted changes.** Check `git status`. If there are uncommitted changes, stop and tell the owner what they are; don't carry them onto the new branch.
4. **Fetch.** `git fetch origin --prune` so `origin/master` and the list of remote branches are current (if it needs a sign-in, run it in a Terminal tab so the owner can see the prompt).
5. **Name not already used.** Refuse the name if any of these is true, say which one and why, and suggest a new name (a more specific topic, or `-2` at the end), then ask the owner to confirm it and check it again:
   - it exists locally: `git show-ref --verify --quiet refs/heads/<name>` succeeds;
   - it exists on GitHub: `git ls-remote --heads origin <name>` prints a line;
   - it was merged into `master` before: it appears in `git branch -a --merged origin/master` (as `<name>` or `remotes/origin/<name>`), or `gh pr list --state merged --head <name>` lists a pull request (this also catches branches deleted after merging).
   A merged branch is finished: never reuse it, even for a follow-up on the same page.
6. **Current branch already merged?** Note the branch this session is on (`git branch --show-current`). If it was merged into `master` (`gh pr list --state merged --head <it>` lists a pull request, or `git branch --merged origin/master` lists it and it has commits of its own), tell the owner in one line ("This session was on `<branch>`, which is already merged into master; moving to the new branch.") and commit nothing more on it.
7. **Create the branch from the latest `origin/master`:** `git switch --no-track -c <name> origin/master` (works in a worktree too, where `master` itself may be checked out elsewhere). Confirm in one line: the branch name and the `master` commit it starts from.
8. **Do the task.** If there is a task after the name, do it on this branch, following `CLAUDE.md` if there is one, and keep `docs/backlog.md` up to date (mark the item `Done (<version or PR>)`, or `Partly done` with what is left). If `package.json` exists, run `npm install` once if needed and check that `npm run build` (Astro) passes. Commit on the branch when done.
9. **Preview.** Run `npm run dev` (or `npm run preview` after a build) and look at the changed pages in the browser pane, at phone and desktop width. The owner's preview is the Netlify deploy preview that appears on the pull request once `/pr` opens it.
10. **Never merge into `master` from this command** (merging into `master` publishes https://avega.dev through Netlify). Finish by showing the owner what changed and offering to open a pull request (`/pr`), which is how the work reaches the Main live session.
