// Site settings for scripts/prose-review.mjs (the prose ledger).
//
// - derived: locales a script writes from another (Simplified Chinese from Traditional, by
//   scripts/to-zh-cn.py); their prose is the Traditional Chinese prose, converted, and is read there.
// - skip(path, lang): text the page shows as the game gives it, which is not the site's prose:
//   - a story stage: everything below its field table (pipeline/story.py);
//   - an arcanist's profile: everything below the cover heading but the table header of the
//     voice lines (pipeline/profile.py);
//   - the kit of an arcanist page and the effect of a Psychube page: the sections from the first
//     heading to the names table (pipeline/kit_text.py, pipeline/psychube.py), tables left out,
//     since the Insight materials table is ours;
//   - the effect column of the Statuses page (pipeline/write_systems.py).
//   The strings are read from the built page, as the ledger reads it: tags dropped, entities
//   decoded, and the text of a link to one of the site's pages replaced by the mark the ledger
//   puts there.

import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const NAMES = new Set(['Names', '名稱', '名称', '名前', '이름']);
const ENTITIES = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' };

const decode = (s) =>
	s.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (m, e) =>
		e[0] === '#' ? String.fromCodePoint(e[1] === 'x' || e[1] === 'X' ? parseInt(e.slice(2), 16) : Number(e.slice(1))) : (ENTITIES[e] ?? m)
	);
/** An element's text as the ledger reads it (textContent, internal link texts masked). */
const text = (html) =>
	decode(
		html
			.replace(/<a [^>]*href="(?:\/|#)[^"]*"[^>]*>[\s\S]*?<\/a>/g, '⟨名⟩')
			.replace(/<[^>]+>/g, '')
	)
		.replace(/\s+/g, ' ')
		.trim();
/**
 * The text of each element of the given tags. A list item's own text stops where a nested list
 * starts, as the ledger reads it; the nested items are elements of their own.
 */
const elements = (html, tags) => {
	const out = [...html.matchAll(new RegExp(`<(${tags})(?:\\s[^>]*)?>([\\s\\S]*?)</\\1>`, 'g'))].filter((m) => m[1] !== 'li').map((m) => text(m[2]));
	if (tags.split('|').includes('li')) {
		for (const m of html.matchAll(/<li(?:\s[^>]*)?>([\s\S]*?)(?=<\/?li[\s>]|<ul|<ol)/g)) out.push(text(m[1]));
	}
	return out.filter(Boolean);
};

/** The page's content: from the start of the Markdown content to the page notes. */
function content(path) {
	const file = join(DIST, path, 'index.html');
	if (!existsSync(file)) return '';
	const html = readFileSync(file, 'utf8');
	const start = html.indexOf('<div class="sl-markdown-content');
	if (start < 0) return '';
	const end = html.indexOf('<dl class="not-content facts"', start);
	return html.slice(start, end < 0 ? undefined : end);
}

/** Splits content at its h2 headings: [{ head, html }], the part before the first heading has head null. */
function sections(html) {
	const parts = html.split(/(?=<div class="sl-heading-wrapper level-h2")/);
	return parts.map((p, i) => ({ head: i ? text((/<h2[^>]*>([\s\S]*?)<\/h2>/.exec(p) || [])[1] || '') : null, html: p }));
}

export default {
	derived: ['zh-cn'],
	skip(path) {
		const bare = path.replace(/^(zh-tw|zh-cn|ja|ko)\//, '');
		if (/^story\/[^/]+\/[^/]+\/$/.test(bare)) {
			return sections(content(path)).slice(1).flatMap((s) => elements(s.html, 'p|li|h3|h4|td'));
		}
		if (/^arcanists\/[^/]+\/profile\/$/.test(bare)) {
			return sections(content(path)).slice(1).flatMap((s) => elements(s.html, 'p|li|h3|h4|td'));
		}
		if (/^(arcanists|psychubes)\/[^/]+\/$/.test(bare)) {
			const out = [];
			for (const s of sections(content(path)).slice(1)) {
				if (NAMES.has(s.head)) break;
				out.push(...elements(s.html.replace(/<table[\s\S]*?<\/table>/g, ''), 'p|li|h3|h4'));
			}
			return out;
		}
		if (bare === 'systems/statuses/') {
			return [...content(path).matchAll(/<tr>\s*<td>[\s\S]*?<\/td>\s*<td>([\s\S]*?)<\/td>/g)].map((m) => text(m[1]));
		}
		return [];
	},
};
