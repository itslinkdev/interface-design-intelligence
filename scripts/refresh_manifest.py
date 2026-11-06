#!/usr/bin/env python3
"""Regenerate SHA-256 checksums after intentionally editing the skill package."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'MANIFEST.sha256'
files = sorted(p for p in ROOT.rglob('*') if p.is_file() and p != MANIFEST
               and '__pycache__' not in p.parts and p.suffix not in ('.pyc', '.pyo'))
MANIFEST.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n' for p in files), encoding='utf-8')
print(f'Updated {MANIFEST.name}: {len(files)} files')
