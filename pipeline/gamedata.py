"""Read the pinned game tables in cache/ and the global client's text by language.

  import gamedata as g
  g.cn('equip')            rows of a mainland table (Simplified Chinese text inline)
  g.gl('equip')            rows of a global table (text fields hold language keys)
  g.text(key, 'ja')        the global client's string for a key: en, ja, ko or zh-TW
  g.gl_text('equip', 1508, 'name', 'ko')   a text field of a global row, in one language
"""
import functools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
CN, GL = PINS['cn'], PINS['gl']
LANG_FILE = {'en': 'en', 'ja': 'jp', 'ko': 'kr', 'zh-TW': 'tw', 'zh-CN': 'zh'}
CN_JSON = f'https://github.com/St-Pavlov-Foundation/re1999-data/blob/{CN["commit"]}/data/json/'
GL_JSON = f'https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/{GL["commit"]}/data/json/'
GL_LANG = f'https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/{GL["commit"]}/data/configs/language/'


def use(pins):
	"""Read the tables of other commits from now on (pipeline/upstream.py compares two pairs)."""
	global CN, GL
	CN, GL = pins['cn'], pins['gl']
	for f in (cn, gl, _lang, _index):
		f.cache_clear()


@functools.cache
def cn(table):
	return json.loads((ROOT / 'cache' / 'cn' / CN['commit'] / 'data' / 'json' / f'{table}.json').read_text())


@functools.cache
def gl(table):
	return json.loads((ROOT / 'cache' / 'gl' / GL['commit'] / 'data' / 'json' / f'{table}.json').read_text())


@functools.cache
def _lang(code):
	rows = json.loads((ROOT / 'cache' / 'gl' / GL['commit'] / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())
	return {r['key']: r['content'] for r in rows}


def clean(s):
	return re.sub(r'<[^>]+>', '', s or '').strip()


def text(key, lang):
	return clean(_lang(LANG_FILE[lang]).get(key, ''))


@functools.cache
def _index(table, server):
	rows = cn(table) if server == 'cn' else gl(table)
	return {r['id']: r for r in rows if 'id' in r}


def gl_text(table, id_, field, lang):
	r = _index(table, 'gl').get(id_)
	return text(r[field], lang) if r and r.get(field) else ''


def cn_row(table, id_):
	return _index(table, 'cn').get(id_)


def gl_row(table, id_):
	return _index(table, 'gl').get(id_)
