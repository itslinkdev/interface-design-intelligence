#!/usr/bin/env python3
"""Reproducible static file footprint. Character/4 is only a rough proxy, NOT actual model tokens."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
for group,paths in [('core',[ROOT/'SKILL.md']),
                    ('modules',list((ROOT/'references').glob('*.md'))),
                    ('adapters',list((ROOT/'stacks').glob('*.md'))),
                    ('catalog',[ROOT/'assets/pattern-catalog.tsv']),
                    ('styles',list((ROOT/'styles').glob('*.md'))),
                    ('style index',[ROOT/'assets/style-catalog.tsv'])]:
    chars=[len(p.read_text(encoding='utf-8')) for p in paths]
    size=sum(p.stat().st_size for p in paths)
    print(f'{group}: files={len(paths)}, bytes={size}, chars={sum(chars)}, char/4 proxy≈{(sum(chars)+3)//4}')
    if len(chars)>1:print(f'  one-file range: {min(chars)}–{max(chars)} characters')
print('Not a tokenizer, end-to-end model benchmark, or output-quality measurement.')
