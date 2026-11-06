"""Slider guidance, routing and package checks; not a substitute for browser/a11y testing."""
from pathlib import Path
import importlib.util
import unittest
import csv

ROOT = Path(__file__).resolve().parent.parent

class SliderTests(unittest.TestCase):
    def test_explicit_route_without_core_example(self):
        core=(ROOT/'SKILL.md').read_text()
        self.assertIn('references/slider-interactions.md', core)
        self.assertNotIn('overshoot/elastic/bounce',core.lower())
        guide=(ROOT/'references/slider-interactions.md').read_text()
        for word in ('without a transition', 'prefers', 'Home/End','screen readers','reduced-motion'):
            self.assertTrue(word in guide or (word=='prefers' and 'reduced-motion' in guide),word)

    def test_slider_pattern_routes_without_growth(self):
        with (ROOT/'assets/pattern-catalog.tsv').open() as f: rows=list(csv.DictReader(f,delimiter='\t'))
        self.assertEqual(len(rows),62)
        entry=next(r for r in rows if r['id']=='REF-059')
        self.assertEqual(entry['module'],'references/slider-interactions.md')
        spec=importlib.util.spec_from_file_location('patterns',ROOT/'scripts/find_pattern.py')
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        hits=mod.search('slider drag easing',2)
        self.assertTrue(hits and any('slider-interactions.md' in r['module'] for r in hits), hits)

    def test_offline_demo_controls_and_no_remote_assets(self):
        html=(ROOT/'examples/slider-motion-demo.html').read_text()
        for feature in ('type="range"','min="0"','max="100"','input', 'prefers-reduced-motion', 'aria-hidden', 'Home'):
            self.assertIn(feature,html)
        self.assertNotIn('<script src=',html)
        self.assertNotIn('<link rel="stylesheet"',html)

    def test_skill_frontmatter_compatible_name(self):
        top=(ROOT/'SKILL.md').read_text().split('---',2)[1]
        self.assertIn('name: interface-design-intelligence',top)
        self.assertIn('license: MIT',top)
        self.assertIn('version: "1.3.0"',top)

if __name__=='__main__':unittest.main()
