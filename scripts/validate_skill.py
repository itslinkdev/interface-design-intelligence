#!/usr/bin/env python3
"""Check packaging, bounded core instructions, textual index and hashes (offline)."""
from pathlib import Path
import csv,hashlib,re,sys
ROOT=Path(__file__).resolve().parent.parent
errors=[]
core=(ROOT/'SKILL.md').read_text(encoding='utf-8')
front=re.match(r'^---\n(.*?)\n---\n',core,re.S)
if not front:errors.append('Missing YAML frontmatter')
else:
    fields=dict(re.findall(r'^([a-z][a-z-]*):\s*(.*)$',front.group(1),re.M))
    name=fields.get('name','').strip()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64 or name!=ROOT.name:errors.append('Invalid skill name/directory')
    if not (1<=len(fields.get('description','').strip())<=1024):errors.append('Invalid skill description')
if len(core)>4400:errors.append('SKILL.md exceeds 4400-character target')
for path in re.findall(r'`((?:references|stacks|styles|assets|scripts)/[^`]+\.(?:md|py|tsv))`',core):
    if not (ROOT/path).is_file():errors.append(f'Broken route: {path}')
for p in [*(ROOT/'references').glob('*.md'),*(ROOT/'stacks').glob('*.md'),*(ROOT/'styles').glob('*.md')]:
    if len(p.read_text(encoding='utf-8'))>4400:errors.append(f'Long module: {p.name}')
    if '**Use when:**' not in p.read_text(encoding='utf-8'):errors.append(f'Missing applicability: {p.name}')
with (ROOT/'assets/style-catalog.tsv').open(encoding='utf-8',newline='') as f:
    styles=list(csv.DictReader(f,delimiter='\t'))
if len(styles)!=5 or len(set(r['id'] for r in styles))!=len(styles):errors.append('Style catalog size/IDs')
if not (ROOT/'references/dark-mode-design.md').is_file():errors.append('Missing optional dark-mode guide')
if not (ROOT/'references/slider-interactions.md').is_file():errors.append('Missing optional slider guide')
if not (ROOT/'examples/slider-motion-demo.html').is_file():errors.append('Missing offline slider motion demo')
if not (ROOT/'scripts/check_contrast.py').is_file():errors.append('Missing contrast utility')
for r in styles:
    if not (ROOT/r['file']).is_file():errors.append('Missing style: '+r['file'])
    if not r['name'] or not r['aliases'] or not r['best_for']:errors.append('Incomplete style: '+r['id'])
if not (ROOT/'examples/dark-ui-demo.html').is_file():errors.append('Missing dark UI demo')
if not (ROOT/'examples/style-gallery.html').is_file() or not (ROOT/'examples/style-gallery.css').is_file():
    errors.append('Missing optional original style demo')
with (ROOT/'assets/pattern-catalog.tsv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
if len(rows)!=62 or len(set(r['id'] for r in rows))!=len(rows):errors.append('Catalog size/IDs')
for r in rows:
    if not (ROOT/r['module']).is_file():errors.append('Missing module: '+r['module'])
for forbidden in ('visual-examples','source_filename','visible_credit'):
    for p in ROOT.rglob('*'):
        if p.is_file() and p.suffix in ('.md','.tsv','.py') and 'MANIFEST' not in p.name:
            if forbidden in p.read_text(encoding='utf-8') and p.name!='validate_skill.py':errors.append(f'Stale private reference {forbidden} in {p.relative_to(ROOT)}')
manifest=ROOT/'MANIFEST.sha256'
if not manifest.is_file():errors.append('Missing manifest')
else:
    entries={}
    for line in manifest.read_text().splitlines():
        sha,sep,rel=line.partition('  ')
        if not sep:errors.append('Bad manifest entry');continue
        entries[rel]=sha
    actual={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*') if p.is_file() and p!=manifest and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    if entries!=actual:errors.append('Manifest does not match package contents')
print(f"Core: {len(core)} characters (~{(len(core)+3)//4} token proxy; NOT measured tokens)")
print(f"Modules: {len(list((ROOT/'references').glob('*.md')))}; adapters: {len(list((ROOT/'stacks').glob('*.md')))}; patterns: {len(rows)}; styles: {len(styles)}")
print('PASS' if not errors else 'FAIL: '+'; '.join(errors))
sys.exit(bool(errors))
