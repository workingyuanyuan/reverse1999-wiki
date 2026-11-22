import { defineRouteMiddleware } from '@astrojs/starlight/route-data';
import { getCollection } from 'astro:content';
import { SITE, BASE, LOCALES, pageId, localeOf, idInLocale, htmlPath, mdPath, isoDate } from './lib/site.mjs';

/** Ids of every page that exists, in every language (`index`, `zh-tw`, `ja/arcanists/sonetto`). */
const existing = new Set((await getCollection('docs', (doc) => !doc.data.draft)).map((doc) => doc.id));

/** Page id behind a site path such as `/reverse1999-wiki/ja/arcanists/` (with or without BASE). */
function idFromPath(path: string): string {
	const local = BASE && path.startsWith(BASE + '/') ? path.slice(BASE.length) : path;
	const trimmed = local.replace(/^\/+|\/+$/g, '');
	return trimmed === '' ? 'index' : trimmed;
}

type SidebarEntry = { type: 'link'; href: string } | { type: 'group'; entries: SidebarEntry[] };

/**
 * Drops links to pages a language does not have, and groups left empty. Starlight would
 * otherwise list its English fallback for a page that Japanese or Korean lack.
 */
function pruneSidebar(entries: SidebarEntry[]): SidebarEntry[] {
	return entries.flatMap((entry) => {
		if (entry.type === 'group') {
			const kept = pruneSidebar(entry.entries);
			return kept.length ? [{ ...entry, entries: kept }] : [];
		}
		if (/^[a-z]+:/i.test(entry.href)) return [entry];
		return existing.has(idFromPath(entry.href)) ? [entry] : [];
	});
}

/**
 * Adds the Markdown alternate link and JSON-LD to every page's <head>, keeps hreflang links
 * to the languages in which the page exists, and marks Starlight's fallback pages noindex.
 */
export const onRequest = defineRouteMiddleware((context) => {
	const route = context.locals.starlightRoute;
	route.sidebar = pruneSidebar(route.sidebar as SidebarEntry[]) as typeof route.sidebar;

	const { data } = route.entry;
	const id = pageId(route.entry.id);
	// Starlight's built-in 404 page has no contract fields and no Markdown twin.
	if (!data.lastVerified || !data.sources) return;

	if (route.isFallback) {
		// An English page served at a Japanese or Korean address because that language does
		// not have it yet (records/pending.json). Not a page of that language: no index entry,
		// no hreflang links, no JSON-LD, not in that language's site search. Its Markdown
		// alternate is the English twin it shows. (route is a per-page copy.)
		route.entry.data.pagefind = false;
		route.head =route.head.filter((tag) => !(tag.tag === 'link' && tag.attrs?.hreflang));
		route.head.push({ tag: 'meta', attrs: { name: 'robots', content: 'noindex' }, content: '' });
		route.head.push({
			tag: 'link',
			attrs: { rel: 'alternate', type: 'text/markdown', href: SITE + mdPath(id) },
			content: '',
		});
		return;
	}

	// Starlight links every language; keep those in which this page exists.
	route.head = route.head.filter((tag) => {
		const lang = tag.tag === 'link' ? tag.attrs?.hreflang : undefined;
		if (!lang || lang === 'x-default') return true;
		const locale = LOCALES.find((l) => l.lang === lang);
		return Boolean(locale && existing.has(idInLocale(id, locale)));
	});

	route.head.push({
		tag: 'link',
		attrs: { rel: 'alternate', type: 'text/markdown', href: SITE + mdPath(id) },
		content: '',
	});

	const jsonLd = {
		'@context': 'https://schema.org',
		'@type': 'Article',
		headline: data.title,
		description: data.description,
		inLanguage: localeOf(id).lang,
		url: SITE + htmlPath(id),
		dateModified: isoDate(data.lastVerified),
		...(data.effectiveDate ? { datePublished: isoDate(data.effectiveDate) } : {}),
		...(data.aliases?.length ? { alternativeHeadline: data.aliases.join(', ') } : {}),
		about: {
			'@type': 'VideoGame',
			name: 'Reverse: 1999',
			alternateName: ['Reverse 1999', '重返未來：1999', '重返未来：1999', 'リバース：1999', '리버스: 1999'],
		},
		citation: data.sources.map((s: { url: string }) => s.url),
		encoding: { '@type': 'MediaObject', encodingFormat: 'text/markdown', contentUrl: SITE + mdPath(id) },
	};
	route.head.push({
		tag: 'script',
		attrs: { type: 'application/ld+json' },
		content: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
	});
});
