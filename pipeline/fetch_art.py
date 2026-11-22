"""Fetch the full-length art of arcanists from the Reverse: 1999 Wiki (Fandom) into public/art/characters/.

Usage: python3 -I pipeline/fetch_art.py [slug ...]     (default: every arcanist in records/arcanists.json)

The publisher's sites carry full-length art for the launch arcanists only, so the art comes from
the Fandom wiki, whose file <English name>.png is the arcanist's full-length art on a transparent
ground. The script reads the file's current revision, keeps it as WebP (figure whole, no frame,
nothing drawn on it), and records in records/art.json the file page, the image URL of that revision
and its upload time, which the page cites in its `art` frontmatter. It prints those lines.
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
OUT = ROOT / 'public' / 'art' / 'characters'
RECORD = ROOT / 'records' / 'art.json'
NAMES = {a['slug']: a['names']['en'] for a in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']}
API = 'https://reverse1999.fandom.com/api.php'
UA = {'User-Agent': 'Mozilla/5.0'}
MAX_HEIGHT = 1400  # the page shows it at most 26rem high; this keeps it sharp at 3x


def get(url):
	with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
		return r.read()


def title_of(slug):
	"""The English name, which is the Fandom file name."""
	return NAMES[slug]


def info(name):
	q = urllib.parse.urlencode({'action': 'query', 'titles': f'File:{name}.png', 'prop': 'imageinfo',
		'iiprop': 'url|size|timestamp|sha1', 'format': 'json'})
	page = next(iter(json.loads(get(f'{API}?{q}'))['query']['pages'].values()))
	return page.get('imageinfo', [None])[0]


def main(slugs):
	record = json.loads(RECORD.read_text()) if RECORD.exists() else {}
	OUT.mkdir(parents=True, exist_ok=True)
	failed = 0
	for slug in slugs:
		name = title_of(slug)
		ii = info(name)
		if not ii:
			print(f'{slug}: no file {name}.png on Fandom', file=sys.stderr)
			failed += 1
			continue
		with tempfile.TemporaryDirectory() as tmp:
			src = Path(tmp) / 'in.png'
			src.write_bytes(get(ii['url'] + '&format=original'))
			subprocess.run(['magick', str(src), '-resize', f'x{MAX_HEIGHT}>', '-quality', '86',
				'-define', 'webp:alpha-quality=100', str(OUT / f'{slug}.webp')], check=True)
		record[slug] = {
			'file': f'File:{name}.png',
			'page': f'https://reverse1999.fandom.com/wiki/{urllib.parse.quote(f"File:{name}.png".replace(" ", "_"), safe=":")}',
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
	args = sys.argv[1:] or sorted(NAMES)
	sys.exit(main(args))
