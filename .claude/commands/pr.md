---
description: Push the current branch and open a GitHub pull request for it (task sessions end with this)
argument-hint: "[short title]  (defaults to the latest commit's subject)"
---

Open a pull request for the current branch. Title: `$ARGUMENTS` (if empty, use the subject of the branch's latest commit).

The default branch is `master` today (it may be renamed `main` later; if `origin/master` doesn't exist, use `main` everywhere below).

1. The current branch must not be `master`. If it is, say so and stop.
2. Uncommitted changes: list them and stop (commit first).
3. Bring in the latest `master` so the pull request is up to date: `git fetch origin` then `git merge origin/master`. If that conflicts, resolve it by keeping both sides' work, commit, and say what conflicted.
4. **Build check.** If `package.json` exists, run `npm run build` (Astro; `npm install` first if `node_modules` is missing). If it fails, show the output and stop. If there is no `package.json`, skip this and say so.
5. Push the branch: `git push -u origin <branch>` (if git asks for a sign-in, run it in a Terminal tab).
6. Open the pull request into `master` with `gh pr create --base master --head <branch> --title "<title>" --body-file <file>`. If one is already open for this branch, update its description instead (`gh pr edit`). Write the description in plain language for the owner:
   - **What changes** (what a visitor to avega.dev will notice, page by page)
   - **Why** (the owner's request, the backlog number, or the bug)
   - **How to check on the preview**: Netlify builds a deploy preview for the pull request and posts its link on the pull request (`deploy-preview-<n>--<site>.netlify.app`). Give a numbered checklist of `- [ ]` boxes: which page to open, what to click, what should appear. Include a phone-width check and a light/dark check where the change has layout or colours. Cover what the change might break nearby (menus, links, other pages). If nothing is visible on the site, write "Nothing to see on the site" instead.
   - **Checked by Claude**: tick what was actually done (`npm run build` passes; looked at the pages in the browser at phone and desktop width); leave unticked and say why for anything not done.
   - **Backlog**: the item number and how it is marked now (`Done`, `Partly done`), or "No backlog item".
   End the description with: `🤖 Generated with [Claude Code](https://claude.com/claude-code)`
7. Reply with the pull request link, the Netlify deploy preview link once it shows up on the pull request (`gh pr checks <n>` or `gh pr view <n> --comments`; say it is still building if it isn't there yet), and one line saying it is waiting for the Main live session (`/mp <number>` there merges it, which publishes avega.dev). Do not merge it yourself.
