// Central place for site-wide info. Edit here, every page picks it up.

export const site = {
  name: 'Alberto Vega',
  short: 'A. Vega',
  tagline: 'Software engineer · game developer · dancer · cook',
  description:
    'Alberto Vega: software engineer specializing in games. CV, portfolio, games, dance, music and hobbies.',
  email: 'albertovega22@gmail.com',
  cv: '/cv/avega_cv.pdf',
};

export const nav = [
  { href: '/portfolio', label: 'Portfolio' },
  { href: '/games', label: 'Games' },
  { href: '/dance', label: 'Dance' },
  { href: '/music', label: 'Music' },
  { href: '/hobbies', label: 'Hobbies' },
  { href: '/journal', label: 'Journal' },
  { href: '/cv', label: 'CV' },
];

export type SocialIcon = 'github' | 'twitch' | 'instagram' | 'mail' | 'book';

export const socials: { href: string; label: string; icon: SocialIcon }[] = [
  { href: 'https://github.com/KKira', label: 'GitHub', icon: 'github' },
  { href: 'https://www.twitch.tv/kiraxxiii', label: 'Twitch', icon: 'twitch' },
  { href: 'https://www.instagram.com/kkiraxxiii/', label: 'Instagram', icon: 'instagram' },
  { href: `mailto:${site.email}`, label: 'Email', icon: 'mail' },
];
