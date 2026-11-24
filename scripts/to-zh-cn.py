# Writes the Simplified Chinese pages (src/content/docs/zh-cn/) from the Traditional
# Chinese pages (src/content/docs/zh-tw/). Run it after every change to a zh-tw page:
#
#   uv run --with opencc-python-reimplemented scripts/to-zh-cn.py
#
# Steps: replace Taiwan wording with the wording of the mainland official site (VOC), convert the characters (OpenCC tw2s), swap the title with its
# Simplified alias, and point links at /zh-cn/. Source URLs are kept as they are.
# OpenCC's phrase mode (tw2sp) is not used: it rewrites game terms.

import glob
import os
import re
import sys

from opencc import OpenCC

cc = OpenCC('tw2s')
root = sys.argv[1] if len(sys.argv) > 1 else 'src/content/docs'

# Taiwan wording -> wording of the mainland official site (re.bluepoch.com) and of the
# mainland client's text. Applied in order, before the character conversion. Names of
# arcanists, skills, statuses and items whose mainland string is not the plain conversion of
# the global Traditional Chinese one are added from records/names-voc.json.
VOC = [
    # Wording
    ('機率', '概率'), ('伺服器', '服务器'), ('透過', '通过'), ('帳號', '账号'), ('登入', '登录'),
    ('介面', '界面'), ('用戶端', '客户端'), ('遊戲資料', '游戏数据'), ('網路', '网络'), ('資訊', '信息'),
    ('計畫', '计划'), ('中國大陸', '中国大陆'),
]

# Sentences that quote a Traditional Chinese name: put the name back after conversion.
# Names whose Simplified form in the game is not the plain conversion of the Traditional one
# (written by pipeline/names_voc.py from the records). Longest first, before the wording list.
import json  # noqa: E402
_names = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'records', 'names-voc.json')
if os.path.exists(_names):
    VOC = [tuple(p) for p in json.load(open(_names, encoding='utf-8')) if tuple(p) not in VOC] + VOC

FIXES = {}


def conv(s):
    for a, b in VOC:
        s = s.replace(a, b)
    return cc.convert(s)


def page(src, rel):
    text = open(src, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    lines, body = m.group(1).split('\n'), m.group(2)

    title = next(l for l in lines if l.startswith('title:'))[6:].strip()
    start = next((k for k, l in enumerate(lines) if l.startswith('aliases:')), None)
    aliases, end = [], None
    if start is not None:
        end = start + 1
        while end < len(lines) and lines[end].startswith('  - '):
            aliases.append(lines[end][4:])
            end += 1
    # The Simplified name is an alias of the zh-tw page: it becomes the title, and the
    # Traditional title takes its place among the aliases.
    simplified = conv(title)
    if simplified != title:
        if simplified not in aliases:
            sys.exit(f'{rel}: add the alias "{simplified}" to the zh-tw page')
        aliases = [title if a == simplified else a for a in aliases]
        title = simplified

    out = []
    for k, l in enumerate(lines):
        if l.startswith('title:'):
            out.append('title: ' + title)
        elif start is not None and start < k < end:
            out.append('  - ' + aliases[k - start - 1])
        elif l.lstrip().startswith('url:'):
            out.append(l)
        else:
            out.append(conv(l))
    front = '\n'.join(out)

    if '```' in body:
        sys.exit(f'{rel}: code blocks are not handled; keep them unconverted before using them')
    # A table whose header names both scripts holds names in each script: its rows stay
    # as written and only the header is converted.
    out_lines, keep = [], False
    for l in body.split('\n'):
        if not l.startswith('|'):
            keep = False
        elif '繁體中文' in l and '簡體中文' in l:
            keep = True
            out_lines.append(conv(l))
            continue
        out_lines.append(l if keep else conv(l))
    body = '\n'.join(out_lines)
    for a, b in FIXES.get(rel, []):
        if a not in front + body:
            sys.exit(f'{rel}: FIXES entry no longer matches: {a}')
        front, body = front.replace(a, b), body.replace(a, b)
    body = body.replace('/zh-tw/', '/zh-cn/')

    dst = os.path.join(root, 'zh-cn', rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'w', encoding='utf-8').write('---\n' + front + '\n---\n' + body)


base = os.path.join(root, 'zh-tw')
files = sorted(glob.glob(base + '/**/*.md', recursive=True))
# The story and profile pages of zh-cn hold the mainland client's own text: pipeline/story.py
# and pipeline/profile.py write them.
files = [f for f in files if not os.path.relpath(f, base).startswith('story' + os.sep)
    and not re.match(r'arcanists/[^/]+/profile\.md$', os.path.relpath(f, base).replace(os.sep, '/'))]
for f in files:
    page(f, os.path.relpath(f, base))
print(len(files), 'pages written to', os.path.join(root, 'zh-cn'))
