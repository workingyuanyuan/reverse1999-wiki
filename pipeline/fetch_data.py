"""Fetch the game data tables this site reads, at the commits pinned in records/sources.json.

The two repositories hold the decoded client tables of Reverse: 1999:
  cn: St-Pavlov-Foundation/re1999-data         (mainland client, Simplified Chinese text inline)
  gl: St-Pavlov-Foundation/re1999-data-global  (global client, text in per-language files)
They carry no licence, so the files go to cache/ (not committed) and the pages restate facts.

  python3 -I pipeline/fetch_data.py            fetch the pinned files that are missing
  python3 -I pipeline/fetch_data.py --update   pin both repositories to their current head first
Exit 0 on success, 2 when a file could not be fetched.
"""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / 'records' / 'sources.json'
CACHE = ROOT / 'cache'

REPOS = {
	'cn': 'St-Pavlov-Foundation/re1999-data',
	'gl': 'St-Pavlov-Foundation/re1999-data-global',
}
TABLES = [
	'character', 'character_battle_tag', 'character_rank', 'character_destiny', 'character_destiny_facets',
	'skill', 'skill_effect', 'skill_ex_level', 'skill_passive_level', 'skill_eff_desc', 'equip', 'item', 'currency',
	'summon_pool', 'summon_pool_detail', 'const',  # summon rates, pity and the rule text of each banner type
	'equip_skill', 'equip_break_attr', 'equip_strengthen', 'equip_strengthen_cost', 'equip_break_cost', 'equip_tag',
	'character_recommend',  # Psychubes: effects by amplification, stats, costs, tags, the game's recommendations
	'character_cosume', 'character_level', 'character_attribute',  # level and Insight costs, stats
	'skill_bufftype', 'skill_buff', 'helppage', 'fight_const', 'loading_text',  # status types, battle rules and tips
]
FILES = {
	'cn': ['data/meta.json'] + [f'data/json/{t}.json' for t in TABLES],
	'gl': ['data/meta.json'] + [f'data/json/{t}.json' for t in TABLES]
	+ [f'data/configs/language/language_{l}.json' for l in ('en', 'jp', 'kr', 'tw', 'zh')],
}


def head(repo):
	out = subprocess.run(['gh', 'api', f'repos/{repo}/commits/main', '--jq', '.sha'],
		capture_output=True, text=True, check=True)
	return out.stdout.strip()


def path_of(key, sha, rel):
	return CACHE / key / sha / rel


def fetch(key, sha, quiet=False):
	"""Fetch the files this site reads from one repository at one commit into cache/; the number that failed."""
	failed = 0
	for rel in FILES[key]:
		dest = path_of(key, sha, rel)
		if dest.exists() and dest.stat().st_size > 0:
			continue
		dest.parent.mkdir(parents=True, exist_ok=True)
		url = f'https://raw.githubusercontent.com/{REPOS[key]}/{sha}/{rel}'
		try:
			with urllib.request.urlopen(url, timeout=120) as r:
				dest.write_bytes(r.read())
			if not quiet:
				print('fetched', key, rel)
		except Exception as e:  # noqa: BLE001
			print('FAILED', key, rel, e, file=sys.stderr)
			failed += 1
	return failed


def main():
	pins = json.loads(PINS.read_text()) if PINS.exists() else {}
	if '--update' in sys.argv or not pins:
		for key, repo in REPOS.items():
			pins[key] = {'repo': repo, 'commit': head(repo)}
	failed = 0
	for key in REPOS:
		sha = pins[key]['commit']
		failed += fetch(key, sha)
		meta = json.loads(path_of(key, sha, 'data/meta.json').read_text())
		pins[key]['build'] = meta['version']
		pins[key]['server'] = meta['server']
	PINS.write_text(json.dumps(pins, ensure_ascii=False, indent='\t') + '\n')
	print(json.dumps(pins, ensure_ascii=False))
	return 2 if failed else 0


if __name__ == '__main__':
	sys.exit(main())
