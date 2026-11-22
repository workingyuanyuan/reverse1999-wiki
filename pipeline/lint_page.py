"""Check one page without a build: the check a writer runs on each page before handing it over.

Usage: python3 -I pipeline/lint_page.py <page.md> [...]
A page under zh-tw/, zh-cn/, ja/ or ko/ is checked as that language, any other as English.
Checks: required frontmatter as plain text, description length, aliases, headings without
quotation marks, links to pages that exist in the same language, images that exist in public/,
and the prose patterns of check_prose.py. The build checks (pnpm verify) still run on the whole site.
Exit 1 when a page has an error.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'pipeline'))
import check_prose  # noqa: E402

DOCS = os.path.join(ROOT, 'src', 'content', 'docs')
# aliases is not required: a name that is the same in every language (37) has none.
REQUIRED = ['title', 'description', 'appliesTo', 'caveat', 'lastVerified', 'sources']
LANGS = ('zh-tw', 'zh-cn', 'ja', 'ko')
MAX_DESC = {'en': 110, 'zh-tw': 70, 'zh-cn': 70, 'ja': 70, 'ko': 70}


def lang_of(path):
	m = re.search(r'src/content/docs/(zh-tw|zh-cn|ja|ko)/', path.replace(os.sep, '/'))
	return m.group(1) if m else 'en'


def frontmatter(text):
	m = re.match(r'---\n(.*?)\n---\n', text, flags=re.S)
	if not m:
		return None, text
	data, key = {}, None
	for line in m.group(1).split('\n'):
		if re.match(r'^[A-Za-z]+:', line):
			key, _, value = line.partition(':')
			data[key] = value.strip().strip('"') or []
		elif line.startswith('  - ') and isinstance(data.get(key), list):
			data[key].append(line[4:].strip('"'))
	return data, text[m.end():]


def page_exists(lang, target):
	path = target.split('#')[0].strip('/')
	if lang != 'en':
		if not path.startswith(lang):
			return False
		path = path[len(lang):].strip('/')
	base = os.path.join(DOCS, *([lang] if lang != 'en' else []), path or 'index')
	return os.path.exists(base + '.md') or os.path.exists(os.path.join(base, 'index.md'))


def lint(path):
	errors = []
	lang = lang_of(path)
	text = open(path, encoding='utf8').read()
	data, body = frontmatter(text)
	if data is None:
		return ['no frontmatter']
	for key in REQUIRED:
		if not data.get(key):
			errors.append(f'frontmatter: {key} missing or empty')
	for key in ('title', 'description', 'caveat', 'appliesTo'):
		if isinstance(data.get(key), str) and re.search(r'[*_`\[\]]', data[key]):
			errors.append(f'frontmatter: {key} has Markdown; values are plain text')
	desc = data.get('description') or ''
	if len(desc) > MAX_DESC[lang]:
		errors.append(f'description: {len(desc)} characters, at most {MAX_DESC[lang]}')
	if data.get('title') in (data.get('aliases') or []):
		errors.append('aliases: the title is listed as an alias')
	in_code = False
	for n, line in enumerate(body.split('\n'), 1):
		if line.startswith('```'):
			in_code = not in_code
		if in_code:
			continue
		if re.match(r'#{2,6} .*["“”「」『』‘’]', line):
			errors.append(f'line {n}: heading with quotation marks: {line[:60]}')
		for target in re.findall(r'(?<!!)\[[^\]]*\]\((/[^)\s]*)\)', line):
			if not page_exists(lang, target):
				errors.append(f'line {n}: link to a page that does not exist in this language: {target}')
		for target in re.findall(r'!\[[^\]]*\]\((/[^)\s]*)\)', line):
			if not os.path.exists(os.path.join(ROOT, 'public', target.lstrip('/'))):
				errors.append(f'line {n}: image not in public/: {target}')
		if ':::' in line:
			errors.append(f'line {n}: a ::: directive; pages are plain Markdown')
	for hit in check_prose.check(path):
		errors.append(f'prose: {hit}')
	return errors


def main(paths):
	failed = 0
	for path in paths:
		errors = lint(path)
		for e in errors:
			print(f'{path}: {e}')
		failed += bool(errors)
	print(f'{len(paths) - failed} of {len(paths)} pages pass')
	return 1 if failed else 0


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(__doc__)
		sys.exit(2)
	sys.exit(main(sys.argv[1:]))
