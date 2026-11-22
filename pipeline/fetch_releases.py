"""Read each arcanist's release dates from the English Fandom wiki's infobox (CC BY-SA).

The game data gives no release dates. The Fandom infobox field `release` gives the mainland (CN)
and global dates, e.g. "May 31st, 2023 (CN) <br> October 26th, 2023 (Global)". This reads it
through the MediaWiki API, 10 titles a request, and writes records/releases.json with the
revision id of each page, so a later run can tell which pages changed.

  python3 -I pipeline/fetch_releases.py
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = 'https://reverse1999.fandom.com/api.php'
UA = 'Mozilla/5.0 (compatible; docs-site-builder)'
MONTH_DATE = re.compile(r'([A-Z][a-z]+) (\d{1,2})(?:st|nd|rd|th)?,? (\d{4})\s*\((CN|Global)\)')


def query(titles):
	params = {'action': 'query', 'titles': '|'.join(titles), 'prop': 'revisions', 'rvprop': 'ids|content',
		'rvslots': 'main', 'redirects': '1', 'format': 'json'}
	req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
	with urllib.request.urlopen(req, timeout=60) as r:
		return json.load(r)['query']


def parse_release(text):
	m = re.search(r'\|\s*release\s*=([^\n]*)', text)
	if not m:
		return {}
	out = {}
	for month, day, year, side in MONTH_DATE.findall(m.group(1)):
		out[side.lower()] = datetime.strptime(f'{month} {day} {year}', '%B %d %Y').date().isoformat()
	# One date with no service named: the arcanist came out on both services that day
	# (collaboration arcanists and the special versions S01 and S02 ran on both at once).
	one = re.fullmatch(r'\s*([A-Z][a-z]+) (\d{1,2})(?:st|nd|rd|th)?,? (\d{4})\s*', m.group(1))
	if not out and one:
		date = datetime.strptime(' '.join(one.groups()), '%B %d %Y').date().isoformat()
		out = {'cn': date, 'global': date}
	return out


def main():
	records = json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']
	names = {r['names']['en']: r['slug'] for r in records}
	out = {}
	titles = list(names)
	for i in range(0, len(titles), 10):
		q = query(titles[i:i + 10])
		back = {n['to']: n['from'] for n in q.get('normalized', []) + q.get('redirects', [])}
		for p in q['pages'].values():
			title = back.get(p['title'], p['title'])
			title = back.get(title, title)
			slug = names.get(title)
			if not slug or 'missing' in p or 'revisions' not in p:
				continue
			rev = p['revisions'][0]
			out[slug] = {'page': p['title'], 'revid': rev['revid'], **parse_release(rev['slots']['main']['*'])}
		time.sleep(1)
	missing = sorted(set(names.values()) - set(out))
	(ROOT / 'records' / 'releases.json').write_text(json.dumps(
		{'source': 'https://reverse1999.fandom.com/', 'read': datetime.now().date().isoformat(), 'arcanists': out},
		ensure_ascii=False, indent='\t') + '\n')
	print(len(out), 'pages read; no page for:', missing or 'none')
	print('no CN date:', sorted(s for s, v in out.items() if 'cn' not in v))
	return 0


if __name__ == '__main__':
	sys.exit(main())
