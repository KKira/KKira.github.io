# avega.dev

Personal site of Alberto Vega, built with [Astro](https://astro.build) and deployed by Netlify (domain at Namecheap, DNS on Netlify).

## Run it

```
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs dist/
```

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
