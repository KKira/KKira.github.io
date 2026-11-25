# avega.dev

Personal site of Alberto Vega, built with [Astro](https://astro.build) and deployed by Netlify (domain at Namecheap, DNS on Netlify).

## Run it

```
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs dist/
```

## Previews

Netlify deploys `master` to https://avega.dev. Every pull request into `master` gets its own **Deploy Preview** (a full copy of the site with the changes), linked on the pull request as the `netlify/.../deploy-preview` check: `https://deploy-preview-<PR number>--quirky-goldwasser-4e5c20.netlify.app`. It rebuilds on every push to the branch.

**Branch deploys** (a preview for every pushed branch, even without a pull request) are switched on in the Netlify dashboard, not in the repo: *Project configuration → Build & deploy → Continuous deployment → Branches and deploy contexts → Branch deploys: All*. The URL is then `https://<branch with / as ->--quirky-goldwasser-4e5c20.netlify.app`, e.g. `feature-9-2-netlify-deploy-previews--quirky-goldwasser-4e5c20.netlify.app`.

To get the link for the branch you are on, run `/preview` (it pushes the branch and prints the Deploy Preview or branch deploy URL).

Previews are not indexed by search engines (Netlify sends `X-Robots-Tag: noindex`), and their canonical links point to avega.dev.

## Add content

| What | Where |
| --- | --- |
| A game | new `.md` file in `src/content/games/` (copy an existing one) |
| A portfolio project | new `.md` file in `src/content/projects/` |
| A journal entry | new `.md` file in `src/content/journal/` (math with `$...$`) |
| A dance video / music track | add an object in `src/data/media.ts` |
| A food photo | drop the image in `src/assets/food/` |
| CV | replace `public/cv/avega_cv.pdf` |
| Name, nav, social links | `src/config/site.ts` |

Images under `src/assets/` are resized and optimized at build time. Large videos are better hosted on YouTube/Vimeo and embedded.

Old URLs (`/projects`, `/food`, `/casualties_report`…) redirect to the new pages via `netlify.toml`.
