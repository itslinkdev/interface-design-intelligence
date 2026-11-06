#!/usr/bin/env python3
"""Emit semantic CSS variables from explicit JSON tokens; stdlib only.

Example:
 python /path/to/ux-ui-design/scripts/build_tokens.py --config project.json --out tokens.css

Never infers an accessible palette, reads project source, or overwrites files by default.
"""
import argparse
import json
import re
from pathlib import Path

KEY = re.compile(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z')


def validate_dict(values, where):
    if not isinstance(values, dict) or not values:
        raise ValueError(f'{where} must be a nonempty object')
    output = {}
    for key, value in values.items():
        if not isinstance(key, str) or not KEY.fullmatch(key):
            raise ValueError(f'Invalid token key in {where}: {key!r}')
        if not isinstance(value, str) or not value.strip() or len(value) > 240 or any(s in value for s in (';', '{', '}', '\n', '\r', '/*', '*/')):
            raise ValueError(f'Unsafe or empty value for {where}.{key}')
        output[key] = value.strip()
    return output


def generate(config):
    if not isinstance(config, dict):
        raise ValueError('Root config must be an object')
    prefix = config.get('prefix', 'ui')
    if not isinstance(prefix, str) or not KEY.fullmatch(prefix):
        raise ValueError('Invalid prefix')
    tokens = validate_dict(config.get('tokens'), 'tokens')
    themes = config.get('themes')
    if not isinstance(themes, dict) or 'light' not in themes or set(themes) - {'light', 'dark'}:
        raise ValueError('themes must include light, optionally dark')
    light = validate_dict(themes['light'], 'themes.light')
    dark = validate_dict(themes['dark'], 'themes.dark') if 'dark' in themes else None
    if dark is not None and set(light) != set(dark):
        raise ValueError('Light and dark themes must define the same semantic keys')
    if set(tokens) & set(light):
        raise ValueError('Global tokens and theme tokens cannot reuse keys')

    def declaration(mapping):
        return '\n'.join(f'  --{prefix}-{key}: {value};' for key, value in sorted(mapping.items()))

    # Use explicit theme attributes; the hosting app determines active theme.
    result = ['/* Generated from explicit tokens. Validate contrast; no automatic accessibility guarantee. */',
              ':root, [data-theme="light"] {', declaration({**tokens, **light}), '}']
    if dark:
        result += ['[data-theme="dark"] {', declaration(dark), '}']
    return '\n'.join(result) + '\n', {'prefix': prefix, 'tokens': tokens, 'themes': {'light': light, **({'dark': dark} if dark else {})}}


def safe_write(path, data, force):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if force:
        path.write_text(data, encoding='utf-8')
    else:
        with path.open('x', encoding='utf-8') as fp:
            fp.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path, help='Existing JSON values to convert (never invents tokens)')
    parser.add_argument('--out', required=True, type=Path, help='Output CSS file')
    parser.add_argument('--json-out', type=Path, help='Optional normalized token manifest')
    parser.add_argument('--force', action='store_true', help='Allow overwriting outputs (only with permission)')
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding='utf-8'))
    css, data = generate(config)
    paths = [args.out] + ([args.json_out] if args.json_out else [])
    if len({p.resolve() for p in paths}) != len(paths) or any(p.resolve() == args.config.resolve() for p in paths):
        parser.error('Outputs must be distinct from one another and from input config')
    if not args.force and any(p.exists() for p in paths):
        parser.error('Output exists; refuse overwrite unless --force is provided')
    safe_write(args.out, css, args.force)
    if args.json_out:
        safe_write(args.json_out, json.dumps(data, indent=2, ensure_ascii=False) + '\n', args.force)
    print(f'Created {args.out} ({len(data["tokens"])} global + {len(data["themes"]["light"])} semantic theme tokens)')
    print('Note: contrast, font licensing and application behavior require separate validation.')


if __name__ == '__main__':
    main()
