// Reads page frontmatter straight from disk, for scripts that run outside Astro
// (scripts/check-dist.mjs, the sitemap options).

import { readdirSync, readFileSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse } from 'yaml';

const DOCS_DIR = fileURLToPath(new URL('../content/docs/', import.meta.url));

function walk(dir) {
	return readdirSync(dir, { withFileTypes: true }).flatMap((e) =>
		e.isDirectory() ? walk(join(dir, e.name)) : e.name.endsWith('.md') ? [join(dir, e.name)] : []
	);
}

/** Every page as `{ id, data, body }`, with ids matching the content collection ids. */
export function readPages() {
	return walk(DOCS_DIR)
		.map((file) => {
			const rel = relative(DOCS_DIR, file).replace(/\\/g, '/').replace(/\.md$/, '');
			const id = rel === 'index' ? 'index' : rel.replace(/\/index$/, '');
			const text = readFileSync(file, 'utf8');
			const match = /^---\n([\s\S]*?)\n---\n?/.exec(text);
			return { id, data: match ? parse(match[1]) : {}, body: match ? text.slice(match[0].length) : text };
		})
		.filter((page) => !page.data.draft)
		.sort((a, b) => a.id.localeCompare(b.id));
}

/** Pages that a partial language does not have yet: `{ ja: [id, ...], ko: [...] }`, by content folder. */
export function readPending() {
	return JSON.parse(readFileSync(fileURLToPath(new URL('../../records/pending.json', import.meta.url)), 'utf8'));
}
