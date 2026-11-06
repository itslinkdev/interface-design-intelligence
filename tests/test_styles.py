"""Offline routing checks, using local import for fast repeated queries."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / 'scripts/find_style.py'
SPEC = importlib.util.spec_from_file_location('find_style', SCRIPT)
FINDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FINDER)

class StyleTests(unittest.TestCase):
    def test_all_five_styles_resolve(self):
        for name in ('Liquid Glass', 'Analog Grain', 'Chrome Typography', 'Pixel Accents', 'Editorial Serifs'):
            with self.subTest(name=name):
                result = FINDER.find(name, 1)
                self.assertEqual(result[0]['name'], name)
                self.assertTrue(Path(result[0]['file']).is_file())

    def test_concept_queries(self):
        for query, expected in {
            'translucent floating toolbar': 'Liquid Glass',
            'warm analog texture': 'Analog Grain',
            'metallic silver logo': 'Chrome Typography',
            'pixel cursor accent': 'Pixel Accents',
            'premium serif magazine': 'Editorial Serifs',
        }.items():
            with self.subTest(query=query):
                self.assertEqual(FINDER.find(query, 1)[0]['name'], expected)

    def test_missing_style_returns_empty(self):
        self.assertEqual(FINDER.find('unrelatedgenomexyz'), [])

    def test_list_and_public_gallery(self):
        self.assertEqual(len(FINDER.rows()), 5)
        self.assertTrue((ROOT / 'examples/style-gallery.html').is_file())
        self.assertTrue((ROOT / 'examples/style-gallery.css').is_file())
        # One subprocess additionally proves CLI works from an unrelated cwd.
        with tempfile.TemporaryDirectory() as cwd:
            r = subprocess.run([sys.executable, str(SCRIPT), '--list', '--json'],
                               cwd=cwd, capture_output=True, text=True, check=True)
        self.assertEqual(len(json.loads(r.stdout)), 5)

if __name__ == '__main__':
    unittest.main()
