"""Fetch art from the Reverse: 1999 Wiki (Fandom): arcanists into public/art/characters/, Psychubes into public/art/psychubes/.

Usage: python3 -I pipeline/fetch_art.py [slug ...]               (default: every arcanist in records/arcanists.json)
       python3 -I pipeline/fetch_art.py --psychubes [slug ...]   (default: every Psychube in records/psychubes.json)

The publisher's sites carry full-length art for the launch arcanists only, so the art comes from
the Fandom wiki, whose file <English name>.png is the arcanist's full-length art on a transparent
ground. The script reads the file's current revision, keeps it as WebP (figure whole, no frame,
nothing drawn on it), and records in records/art.json the file page, the image URL of that revision
and its upload time, which the page cites in its `art` frontmatter. It prints those lines.

A Psychube's art is the file <English name> Psychube.png: the illustration the game shows on the
Psychube's own screen, with its lettering, on a transparent ground with a brushed edge. Its record is
records/art-psychubes.json; pipeline/psychube.py writes the art line and credits from it.
"""
import json
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'src' / 'content' / 'docs'
KINDS = {
	'arcanists': dict(out=ROOT / 'public' / 'art' / 'characters', record=ROOT / 'records' / 'art.json', file='{n}.png',
		names=lambda: {a['slug']: a['names']['en'] for a in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']}),
	'psychubes': dict(out=ROOT / 'public' / 'art' / 'psychubes', record=ROOT / 'records' / 'art-psychubes.json', file='{n} Psychube.png',
		names=lambda: {p['slug']: p['en'] for p in json.loads((ROOT / 'records' / 'psychubes.json').read_text())['psychubes']}),
}
API = 'https://reverse1999.fandom.com/api.php'
UA = {'User-Agent': 'Mozilla/5.0'}
MAX_HEIGHT = 1400  # the page shows it at most 26rem high; this keeps it sharp at 3x


def get(url):
	with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
		return r.read()


def info(file):
	q = urllib.parse.urlencode({'action': 'query', 'titles': f'File:{file}', 'prop': 'imageinfo',
		'iiprop': 'url|size|timestamp|sha1', 'format': 'json'})
	page = next(iter(json.loads(get(f'{API}?{q}'))['query']['pages'].values()))
	return page.get('imageinfo', [None])[0]


def main(kind, slugs):
	k = KINDS[kind]
	names, OUT, RECORD = k['names'](), k['out'], k['record']
	record = json.loads(RECORD.read_text()) if RECORD.exists() else {}
	OUT.mkdir(parents=True, exist_ok=True)
	failed = 0
	for slug in slugs or sorted(names):
		file = k['file'].format(n=names[slug])
		ii = info(file)
		if not ii:
			print(f'{slug}: no file {file} on Fandom', file=sys.stderr)
			failed += 1
			continue
		with tempfile.TemporaryDirectory() as tmp:
			src = Path(tmp) / 'in.png'
			src.write_bytes(get(ii['url'] + '&format=original'))
			subprocess.run(['magick', str(src), '-resize', f'x{MAX_HEIGHT}>', '-quality', '86',
				'-define', 'webp:alpha-quality=100', str(OUT / f'{slug}.webp')], check=True)
		record[slug] = {
			'file': f'File:{file}',
			'page': f'https://reverse1999.fandom.com/wiki/{urllib.parse.quote(f"File:{file}".replace(" ", "_"), safe=":")}',
			'url': ii['url'],
			'uploaded': ii['timestamp'][:10],
			'size': [ii['width'], ii['height']],
			'sha1': ii['sha1'],
		}
		r = record[slug]
		print(f'{slug}:\n  - title: "Reverse: 1999 Wiki (Fandom), {r["file"]}"\n    url: {r["page"]}\n'
			f'  - title: "Image file, uploaded {r["uploaded"]}"\n    url: {r["url"]}')
	RECORD.write_text(json.dumps(dict(sorted(record.items())), ensure_ascii=False, indent='\t') + '\n')
	return 1 if failed else 0


if __name__ == '__main__':
	args = sys.argv[1:]
	kind = 'psychubes' if args[:1] == ['--psychubes'] else 'arcanists'
	sys.exit(main(kind, args[1:] if kind == 'psychubes' else args))
