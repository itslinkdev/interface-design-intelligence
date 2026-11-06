#!/usr/bin/env python3
"""Search optional visual styles with bounded output; no third-party dependencies."""
import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / 'assets/style-catalog.tsv'
STOP = {'a', 'the', 'and', 'in', 'for', 'with', 'an', 'to', 'on', 'of', 'style', 'design', 'ui', 'ux'}

def words(value):
    return set(re.findall(r'[a-z0-9]+', value.lower())) - STOP

def rows():
    with CATALOG.open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle, delimiter='\t'))

def find(query, limit=2):
    q = query.lower().strip()
    terms = words(q)
    scored = []
    for row in rows():
        name = row['name'].lower()
        name_terms = words(name)
        aliases = words(row['aliases'])
        purpose = words(row['best_for'])
        # Strong whole-phrase match, then weighted lexical overlap.
        match = 20 if q == name or (len(q) >= 5 and q in name) else 0
        match += 5 * len(terms & name_terms) + 3 * len(terms & aliases) + len(terms & purpose)
        if match:
            scored.append((match, row))
    scored.sort(key=lambda x: (-x[0], x[1]['id']))
    return [format_row(r) for _, r in scored[:max(1, min(5, limit))]]

def format_row(row):
    return {'id': row['id'], 'name': row['name'], 'best_for': row['best_for'],
            'file': str((ROOT / row['file']).resolve())}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--limit', type=int, default=2)
    parser.add_argument('--list', action='store_true', help='Show available style names')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    if args.list:
        result = [format_row(r) for r in rows()]
    elif args.query.strip():
        result = find(args.query, args.limit)
    else:
        parser.error('Provide a style query or --list')
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for r in result:
            print(f"{r['id']} | {r['name']} | {r['best_for']}\n  {r['file']}")
        if not result:
            print('No suitable style: retain the existing design language.')

if __name__ == '__main__':
    main()
