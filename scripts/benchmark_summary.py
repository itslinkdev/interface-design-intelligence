#!/usr/bin/env python3
"""Summarize recorded agent benchmark runs; does not invoke models or fabricate results.

CSV fields: scenario,variant,input_tokens,output_tokens,quality_score,notes
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results', type=Path)
    args = parser.parse_args()
    groups = defaultdict(list)
    with args.results.open(encoding='utf-8', newline='') as fp:
        reader = csv.DictReader(fp)
        required = {'scenario', 'variant', 'input_tokens', 'output_tokens', 'quality_score'}
        if not required.issubset(reader.fieldnames or []):
            parser.error('Expected CSV columns: ' + ', '.join(sorted(required)))
        for row in reader:
            if not row['scenario'] or not row['variant']:
                continue
            try:
                inp, out = int(row['input_tokens']), int(row['output_tokens'])
                quality = float(row['quality_score'])
                if inp < 0 or out < 0 or not 0 <= quality <= 12:
                    raise ValueError()
            except ValueError:
                parser.error('Each recorded run requires measured nonnegative tokens and quality_score in 0..12')
            groups[row['variant']].append((row['scenario'], inp, out, quality))
    if not groups:
        print('No completed benchmark runs; collect actual agent usage and grading first.')
        return
    for variant, items in sorted(groups.items()):
        n = len(items)
        print(f'{variant}: runs={n}, mean input={sum(x[1] for x in items)/n:.0f}, '
              f'mean output={sum(x[2] for x in items)/n:.0f}, '
              f'mean total={sum(x[1]+x[2] for x in items)/n:.0f}, '
              f'mean quality={sum(x[3] for x in items)/n:.2f}/12')
    scopes = [set(x[0] for x in items) for items in groups.values()]
    if len(scopes) > 1 and any(scope != scopes[0] for scope in scopes[1:]):
        print('WARNING: scenario sets differ; compare matched scenarios only.')
    print('These are reported usage figures, not independently measured by this script.')


if __name__ == '__main__':
    main()
