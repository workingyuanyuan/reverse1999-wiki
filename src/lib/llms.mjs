// Builds each language's llms.txt and bundles from the content collection.
// Replaces starlight-llms-txt, which bundled the default language only and left
// out each page's caveat, dates and sources.

import { SITE, TITLE, LOCALES, LLMS_NOTES, localeOf, bareId, mdPath, llmsPath } from './site.mjs';
import { pageHeader, pageMarkdown } from './page-md.mjs';

/** Home page first, then by id. */
function ordered(entries) {
	const rank = (id) => (bareId(id) === 'index' ? '' : bareId(id));
	return [...entries].sort((a, b) => rank(a.id).localeCompare(rank(b.id)));
}

/** Site path of a bundle: `/llms-full.txt`, `/zh-tw/llms-small.txt`, ... */
export function bundlePath(locale, set) {
	return `${locale.dir ? '/' + locale.dir : ''}/llms-${set}.txt`;
}

/**
 * A language's `llms.txt`. What a reader gets wrong without being told comes first,
 * then the bundles and the other languages, then one link per page. A fetch tool that
 * returns 5,000 characters must reach everything above the page list.
 */
export function llmsIndex(entries, locale) {
	const t = LLMS_NOTES[locale.lang];
	const [home, ...rest] = ordered(entries.filter((e) => localeOf(e.id) === locale));
	const also = (e) => (e.data.aliases?.length ? ` (${e.data.aliases.join(', ')})` : '');
	const pages = rest.map((e) => `- [${e.data.title}](${SITE}${mdPath(e.id)})${also(e)}: ${e.data.description}`);
	const more = [
		`- [${mdPath(home.id).slice(1)}](${SITE}${mdPath(home.id)}): ${t.home}`,
		`- [llms-full.txt](${SITE}${bundlePath(locale, 'full')}): ${t.full}`,
		`- [llms-small.txt](${SITE}${bundlePath(locale, 'small')}): ${t.digest}`,
		`- [index.json](${SITE}/index.json): ${t.json}`,
		...LOCALES.filter((other) => other !== locale).map(
			(other) => `- ${t.otherLanguage} ${other.label}: <${SITE}${llmsPath(other)}>`
		),
	];
	return (
		[
			`# ${TITLE[locale.lang]}`,
			`> ${t.summary}`,
			`## ${t.heading}\n\n${t.notes.map((n) => `- ${n}`).join('\n')}`,
			`## ${t.more}\n\n${more.join('\n')}`,
			`## ${t.pages}\n\n${pages.join('\n')}`,
		].join('\n\n') + '\n'
	);
}

/** One language in one file. `full` keeps page bodies; `small` keeps the headers only. */
export function llmsBundle(entries, locale, set) {
	const allIds = new Set(entries.map((e) => e.id));
	const pages = ordered(entries.filter((e) => localeOf(e.id) === locale));
	const render = set === 'full' ? (e) => pageMarkdown(e, allIds).trim() : (e) => pageHeader(e, allIds);
	return pages.map(render).join('\n\n\n') + '\n';
}
