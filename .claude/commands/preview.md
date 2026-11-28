---
description: Push the current branch and give the owner its Netlify preview link to try before it goes live
argument-hint: "(no arguments)"
---

Put the current branch on a Netlify preview so the owner can try it before `/mp` publishes it to avega.dev. Netlify site: `quirky-goldwasser-4e5c20` (see `netlify.toml` and the README "Previews" section).

The default branch is `master` today (it may be renamed `main` later; if `origin/master` doesn't exist, use `main` below).

1. The current branch must not be `master` (that is the live site; it goes through `/mp`). If it is, say so and stop.
2. Uncommitted changes: list them and stop (commit first).
3. **Build check.** Run `npm run build` (`npm install` first if `node_modules` is missing). If it fails, show the output and stop. If the local Node is too old for Astro, say so and continue: Netlify builds with its own Node 22.
4. Push the branch: `git push -u origin <branch>` (if git asks for a sign-in, run it in a Terminal tab).
5. Find the preview link, naming the repo in every `gh` call (`--repo KKira/KKira.github.io`):
   - **Pull request open for this branch** (`gh pr list --repo KKira/KKira.github.io --head <branch> --json number,url`): the Deploy Preview `https://deploy-preview-<number>--quirky-goldwasser-4e5c20.netlify.app`. Check its state with `gh pr checks <number> --repo KKira/KKira.github.io` (the `netlify/.../deploy-preview` check).
   - **No pull request**: the branch deploy `https://<branch, with "/" and "." as "-">--quirky-goldwasser-4e5c20.netlify.app`. This only exists if branch deploys are switched on in the Netlify dashboard (backlog 9.2). If the link doesn't load, say so and offer `/pr`, which always gets a Deploy Preview.
6. Reply with the preview link, the branch it shows, whether Netlify is still building it, and one line on what to try. Remind the owner the preview is not indexed by search engines and that `/mp` (in the Main live session) is what publishes avega.dev. Don't merge anything.
