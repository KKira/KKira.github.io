// Dance videos and music tracks. Add one object per item; the pages update themselves.
//
// `embed` is the player URL:
//   YouTube:    https://www.youtube-nocookie.com/embed/<VIDEO_ID>
//   Vimeo:      https://player.vimeo.com/video/<VIDEO_ID>
//   Spotify:    https://open.spotify.com/embed/track/<TRACK_ID>
//   SoundCloud: https://w.soundcloud.com/player/?url=<URL-ENCODED TRACK URL>
// or use `src` for a file in /public (e.g. '/audio/my-song.mp3' or '/videos/clip.mp4').

export type Dance = {
  title: string;
  date?: string; // '2026-11-01'
  style?: string; // 'Salsa', 'Hip-hop'…
  embed?: string;
  src?: string;
  note?: string;
};

export type Track = {
  title: string;
  date?: string;
  kind?: 'original' | 'cover' | 'mix' | 'playlist';
  embed?: string;
  src?: string;
  note?: string;
};

export const dances: Dance[] = [
  // { title: 'Showcase 2026', style: 'Salsa', embed: 'https://www.youtube-nocookie.com/embed/VIDEO_ID' },
];

export const tracks: Track[] = [
  // { title: 'First beat', kind: 'original', embed: 'https://open.spotify.com/embed/track/TRACK_ID' },
];
