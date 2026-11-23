# Backlog

Numbered, grouped by section. Mark an item done with the version or pull request that shipped it: `N.M Done (vX): ...`.
Add items with `/backlog <idea>` and start work on one with `/startb <number>` in the avega.dev - Backlog session.

## 1. Site & design
- 1.1 Partly done: rebuild the site with Astro. In progress on branch `astro-redesign` in the Main live session.
- 1.2 Custom 404 page.

## 2. CV
- 2.1 Add GitHub and LinkedIn links to the CV.

## 3. Portfolio

## 4. Games

## 5. Dance
- 5.1 Dance page: add dance videos, hosted on YouTube or Vimeo and embedded.

## 6. Music
- 6.1 Music page: add tracks (SoundCloud, Spotify or YouTube embeds, or audio files).

## 7. Hobbies (food, manga, streaming)

## 8. Journal

## 9. Hosting & SEO
- 9.1 Done (PR): Videos slimmed down. The 7 journal clips (tutorial screen recordings, ~12 MB) were removed; the Casualties Report trailer stays self-hosted (school project with copyrighted material, which YouTube could take down), re-encoded from 21 MB to 2.9 MB. New `Video` component (`src/components/Video.astro`) embeds YouTube links or IDs through youtube-nocookie for future videos, and still plays files from `/public`. The old files stay in git history.
- 9.2 Netlify deploy previews for pull requests and branches.
