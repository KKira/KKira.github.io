---
description: Merge and publish - merge a pull request (or branch) into master, which Netlify deploys to avega.dev, and push
argument-hint: "[pull request number or branch]  (defaults to the current branch)"
---

Merge and publish. Target: `$ARGUMENTS` (a pull request number like `12`, a branch name, or empty for the current branch).

**Always name this repo in GitHub commands.** Every `gh pr …` and `gh api` call passes `-R KKira/KKira.github.io`, and a pull request is always named by its number, never left for `gh` to guess from the folder. Before changing a pull request (editing its description, commenting, closing), read it with `gh pr view <n> -R KKira/KKira.github.io --json headRefName,url` and check its branch is the one being worked on here; if not, stop and say so. Other projects have pull requests with the same numbers, and a wrong guess overwrites another project's description (this once wiped the owner's ticked test results).

The owner typing `/mp` is the approval to merge, publish and push this pull request or branch. Stop and report at the first step that fails; never skip one. This is meant to run in the **avega.dev - Main live** session (the one session that touches `master`).

Publishing = merging into `master`: Netlify builds `master` and deploys it to https://avega.dev (domain at Namecheap, DNS and hosting on Netlify). The default branch is `master` today (it may be renamed `main` later; if `origin/master` doesn't exist, use `main` everywhere below).

1. **Find the branch.** For a pull request number, read it with `gh pr view <n> -R KKira/KKira.github.io --json number,title,headRefName,state,url,body` (it must be open) and use its branch: `git fetch origin` and check the branch out locally from `origin/<branch>`. Otherwise use the branch given, or the current one. It must not be `master`. If there are uncommitted changes in this checkout, list them and stop.
2. **Save the test results** (pull requests only). From the description read in step 1, list the owner's checklist ("How to test" / "How to check"): which boxes are ticked and which aren't. If any are unticked, show them and ask the owner whether to merge anyway; stop if they say wait. Then post the results as a comment, so they survive any later change to the description: `gh pr comment <n> -R KKira/KKira.github.io --body "Tested by the owner: ✓ 1, 2, 3 · not ticked: 4 (merged anyway)"`. Skip this when the description has no checklist or says there is nothing to see, and say so.
3. **Bring it up to date with `master`:** merge `origin/master` into the branch. If that conflicts, resolve it by keeping both sides' work (in `docs/backlog.md` keep every item; renumber if two branches claimed the same number), and tell the owner what conflicted.
4. **Build check.** If `package.json` exists, run `npm run build` (Astro; `npm install` first if needed). If it fails, show the output and stop. If there is no `package.json`, skip this and say so.
5. **Merge:** switch to `master`, make sure it matches `origin/master`, and fast-forward it to the branch (`git merge --ff-only <branch>`). A fast-forward makes GitHub mark the pull request as merged by itself.
6. **Push** `master` and the branch to GitHub (`origin`). This publishes the site: Netlify starts a production deploy. If git asks for a sign-in, run the push in a Terminal tab so the owner can see the prompt.
7. **Check the pull request** (if there is one): `gh pr view <n> -R KKira/KKira.github.io --json state` should say MERGED. If it doesn't, close it with a comment naming the merge commit.
8. **Check the deploy.** Once Netlify has had a minute, open https://avega.dev in the browser pane and check the changed pages show the new version. If the site still shows the old version or errors, say so and point the owner to the Netlify deploy log.
9. **Report** in a few lines: what is now live on https://avega.dev, the pull request link, and what is still waiting (`gh pr list -R KKira/KKira.github.io --state open`, and `git branch --no-merged master`).
