// Prints the IndexNow request body for pages whose content changed, or nothing.
//
// Run after `pnpm verify` and before the deploy. A page counts as changed when the hash of its
// Markdown twin in dist/ differs from the hash the live site published at the last deploy
// (`/indexnow.json`, written here into dist/), or the page is new. One request to the live site:
// fetching every live twin (about 9,500 with the story) gets HTTP 429 from GitHub Pages. The
// twin is built from the content only, so a change to the skin submits nothing. Before the live
// site has the file, every page counts as changed.
//
// The key file lives at the root of the domain (served by the user site), which
// authorizes every URL on the host, project sites included.
//
// Usage: node scripts/indexnow.mjs > body.json   (empty output: nothing to submit)
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join } from 'node:path';
import { SITE as SITE_RAW } from '../src/lib/site.mjs';

const INDEXNOW_KEY = '633317ad5747c8e6a159c88e888ec920';
const SITE = SITE_RAW.replace(/\/+$/, '');
const DIST = 'dist';
const origin = new URL(SITE).origin;

const locs = readdirSync(DIST)
	.filter((f) => /^sitemap-\d+\.xml$/.test(f))
	.flatMap((f) => [...readFileSync(join(DIST, f), 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]));
if (locs.length === 0) throw new Error('indexnow: no URLs in dist/sitemap-*.xml');

/** `${SITE}/a/b/` -> `${SITE}/a/b.md`; the site root -> `${SITE}/index.md`. */
function twinUrl(loc) {
	const trimmed = loc.replace(/\/+$/, '');
	return (trimmed === SITE ? `${SITE}/index` : trimmed) + '.md';
}

const hashes = Object.fromEntries(
	locs.map((loc) => {
		const twin = twinUrl(loc);
		const local = readFileSync(join(DIST, twin.slice(SITE.length + 1)), 'utf8');
		return [loc, createHash('sha256').update(local).digest('hex').slice(0, 16)];
	})
);
// 404: the live site has no hashes yet. Any other failure stops the run: an outage is not a change.
const res = await fetch(`${SITE}/indexnow.json`, { signal: AbortSignal.timeout(30000) });
if (!res.ok && res.status !== 404) throw new Error(`indexnow: ${SITE}/indexnow.json returned ${res.status}`);
const live = res.ok ? await res.json() : {};
const changed = locs.filter((loc) => live[loc] !== hashes[loc]);
writeFileSync(join(DIST, 'indexnow.json'), JSON.stringify(hashes) + '\n');

console.error(`indexnow: ${changed.length} of ${locs.length} pages changed`);
for (const url of changed) console.error(`  ${url}`);
if (changed.length > 0) {
	console.log(
		JSON.stringify({
			host: new URL(SITE).host,
			key: INDEXNOW_KEY,
			keyLocation: `${origin}/${INDEXNOW_KEY}.txt`,
			// IndexNow takes at most 10,000 URLs in one request.
			urlList: changed.slice(0, 10000),
		})
	);
}
