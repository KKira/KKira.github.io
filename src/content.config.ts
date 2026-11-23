import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Games you made or helped make. One Markdown file per game in src/content/games.
const games = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/games' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      summary: z.string(),
      year: z.number().optional(),
      platform: z.string().optional(),
      role: z.string().optional(),
      cover: image().optional(),
      trailer: z.string().optional(), // path under /public or a YouTube embed URL
      download: z.string().url().optional(),
      play: z.string().url().optional(), // e.g. itch.io page
      team: z.array(z.string()).default([]),
      tags: z.array(z.string()).default([]),
      order: z.number().default(0),
    }),
});

// Non-game work for the portfolio. One Markdown file per project in src/content/projects.
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      summary: z.string(),
      cover: image().optional(),
      repo: z.string().url().optional(),
      link: z.string().optional(),
      tags: z.array(z.string()).default([]),
      order: z.number().default(0),
    }),
});

// Coding journal entries. One Markdown file per entry in src/content/journal.
const journal = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/journal' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      order: z.number(),
      summary: z.string(),
      series: z.string().optional(),
      objectives: image().optional(),
      video: z.string().optional(),
    }),
});

export const collections = { games, projects, journal };
