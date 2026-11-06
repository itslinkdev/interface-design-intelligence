#!/usr/bin/env python3
"""Optional dependency-free WCAG 2.2 sRGB pair checker (not a full UI audit)."""
import argparse
import re
import sys


def rgb(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', value):
        raise argparse.ArgumentTypeError('Use opaque #RGB or #RRGGBB hex colors')
    digits = value[1:]
    if len(digits) == 3:
        digits = ''.join(c * 2 for c in digits)
    return tuple(int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(color):
    v = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in color]
    return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]


def ratio(fg, bg, alpha=1.0):
    composited = tuple(alpha * f + (1 - alpha) * b for f, b in zip(fg, bg))
    a, b = sorted((luminance(composited), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('foreground', type=rgb)
    parser.add_argument('background', type=rgb)
    parser.add_argument('--alpha', type=float, default=1.0, help='Foreground alpha in [0,1], blended over solid background')
    parser.add_argument('--target', choices=['normal', 'large', 'ui'], default='normal')
    args = parser.parse_args()
    if not 0 <= args.alpha <= 1:
        parser.error('--alpha must be within [0,1]')
    threshold = 4.5 if args.target == 'normal' else 3.0
    score = ratio(args.foreground, args.background, args.alpha)
    passing = score + 1e-9 >= threshold
    print(f'{score:.2f}:1 against {threshold:g}:1 WCAG AA {args.target} target: {"PASS" if passing else "FAIL"}')
    print('Solid sRGB pair only. Validate real rendered gradients, overlays, and UI states separately.')
    return 0 if passing else 1


if __name__ == '__main__':
    sys.exit(main())
