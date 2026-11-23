// Runs scripts/check-dist.mjs in several processes, each on every n-th page, and merges the
// result. One process over the whole site (about 9,500 pages with the story) passes Node's heap
// and takes too long; the checks of the whole site run in the first process.

import { spawn } from 'node:child_process';
import { availableParallelism } from 'node:os';
import { fileURLToPath } from 'node:url';

const n = Math.max(1, Math.min(availableParallelism(), 8));
const script = fileURLToPath(new URL('./check-dist.mjs', import.meta.url));
const runs = await Promise.all(
	[...Array(n).keys()].map(
		(i) =>
			new Promise((resolve) => {
				const child = spawn(process.execPath, ['--max-old-space-size=4096', script], { env: { ...process.env, CHECK_SHARD: `${i}/${n}` } });
				let out = '';
				let err = '';
				child.stdout.on('data', (d) => (out += d));
				child.stderr.on('data', (d) => (err += d));
				child.on('close', (code) => resolve({ i, code, out, err }));
			})
	)
);
const failures = new Set();
let pages = '';
for (const { i, code, out, err } of runs) {
	for (const line of out.split('\n')) {
		if (line.startsWith('note:') && i === 0) console.log(line);
		const m = /^PASS: (\d+) pages/.exec(line);
		if (m) pages = m[1];
	}
	const listed = err.split('\n').filter((l) => l.startsWith('- ') || l.startsWith('    '));
	for (const l of listed) failures.add(l);
	if (code !== 0 && !listed.length) failures.add(`- check-dist.mjs process ${i}/${n} exited with ${code}:\n${err.slice(-2000)}`);
	const m = /FAIL: \d+ problem\(s\) in (\d+) pages/.exec(err);
	if (m) pages = m[1];
}
if (failures.size) {
	console.error(`FAIL: ${[...failures].filter((f) => f.startsWith('- ')).length} problem(s) in ${pages} pages (${n} processes)\n`);
	for (const f of failures) console.error(f);
	process.exit(1);
}
console.log(`PASS: ${pages} pages, each with a Markdown twin; all checks passed (${n} processes).`);
