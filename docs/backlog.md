# Backlog

Numbered, grouped by section. Mark an item done with the version or pull request that shipped it: `N.M Done (vX): ...`.
Add items with `/backlog <idea>` and start work on one with `/startb <number>` in the avega.dev - Backlog session.

## 1. Site & design
- 1.1 Partly done: rebuild the site with Astro. In progress on branch `astro-redesign` in the Main live session.
- 1.2 Custom 404 page.
- 1.3 Dark mode button in the site header (`src/layouts/Base.astro`). Starts from the device setting, remembers the choice, and doesn't flash the wrong theme on reload (inline script in `<head>`). `global.css` already supports `data-theme` light/dark.
- 1.4 Version badge: a small `vX.Y.Z` pill in the header next to the dark mode button, taken from `package.json` (the site has no version yet).
- 1.5 Release notes popup: clicking the version badge opens the notes per version, newest first; closes with ×, Esc or a click outside. Notes live in one file in the repo, and `/mp` updates it on each release. Reference: Ekeko's `#ver` button and popup.

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
- 9.2 Partly done: Netlify deploy previews for pull requests and branches. Pull request previews work (Netlify posts the link on each pull request, noindexed) and are documented in the README and `netlify.toml`. Left: switch on branch deploys in the Netlify dashboard (Branch deploys: All); the owner does that.
