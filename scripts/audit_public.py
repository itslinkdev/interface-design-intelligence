#!/usr/bin/env python3
"""Conservative local prepublication scan. Not a substitute for GitHub secret scanning."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parent.parent
problems=[]
blocked_ext={'.webp','.png','.jpg','.jpeg','.gif','.pdf','.zip','.tar','.gz','.p12','.pfx','.pem','.key','.db','.sqlite'}
blocked_names={'.env','.env.local','id_rsa','id_ed25519'}
patterns={
    'GitHub token': r'\b(?:gh[pousr]_[a-zA-Z0-9]{25,}|github_pat_[a-zA-Z0-9_]{25,})\b',
    'AWS access key': r'\b(?:AKIA|ASIA)[0-9A-Z]{16}\b',
    'Google API key': r'\bAIza[0-9A-Za-z_-]{30,}\b',
    'PEM private key': r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
    'OpenAI key': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{28,}\b',
    'Workspace path': r'(?:/mnt/data/|/Users/[^/\s]+/|C:\\Users\\[^\\\s]+\\)',
}
source_names=re.compile(r'10000539\d\d\.png|10000540\d\d\.png|Screenshot_20\d{6}',re.I)
for p in ROOT.rglob('*'):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
    relative=p.relative_to(ROOT).as_posix()
    if p.suffix.lower() in blocked_ext or p.name in blocked_names:
        problems.append(f'Prohibited file: {relative}')
        continue
    if p.suffix.lower() in ('.md','.txt','.py','.tsv','.json','.yml','.yaml','.svg','.csv','.html','.css') or p.name in ('LICENSE','.gitignore'):
        content=p.read_text(encoding='utf-8')
        for name,pat in patterns.items():
            if p.name=='audit_public.py':continue # avoid matching its own regex literals
            if re.search(pat,content):problems.append(f'{name}: {relative}')
        if source_names.search(content):problems.append(f'Private screenshot filename: {relative}')
        if p.suffix=='.svg' and re.search(r'<script\b|<foreignObject\b|(?:xlink:)?href\s*=\s*[\'\"]https?://',content,re.I):
            problems.append(f'Unsafe SVG content: {relative}')
        if p.suffix=='.md':
            for target in re.findall(r'\[[^]]*\]\(([^)]+)\)',content):
                link=target.split('#')[0].strip()
                if not link or link.startswith(('https://','http://','mailto:')):continue
                if not (p.parent/link).exists():problems.append(f'Broken Markdown link: {relative} -> {link}')
print('Public audit:', 'PASS' if not problems else 'FAIL')
for issue in problems:print(' -',issue)
sys.exit(bool(problems))
