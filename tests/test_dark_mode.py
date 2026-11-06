"""Cheap tests for optional dark mode and motion routing; no extra dependencies."""
from pathlib import Path
import importlib.util
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent

class DarkModeTests(unittest.TestCase):
    def test_dark_guide_is_optional_and_routed(self):
        core = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/dark-mode-design.md', core)
        self.assertIn('Start with **this file only**', core)
        self.assertIn('Skip for unrelated UI tasks', (ROOT / 'references/dark-mode-design.md').read_text(encoding='utf-8'))

    def test_contrast_examples(self):
        spec = importlib.util.spec_from_file_location('contrast', ROOT / 'scripts/check_contrast.py')
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertGreaterEqual(mod.ratio(mod.rgb('#F4F4F5'), mod.rgb('#19191D')), 4.5)
        self.assertLess(mod.ratio(mod.rgb('#FFFFFF'), mod.rgb('#121212'), .30), 4.5)
        self.assertGreaterEqual(mod.ratio(mod.rgb('#BFC0CA'), mod.rgb('#19191D')), 4.5)

    def test_cli_failing_pair_exits_nonzero(self):
        tool = ROOT / 'scripts/check_contrast.py'
        r = subprocess.run([sys.executable, str(tool), '#FFFFFF', '#121212', '--alpha', '.30'], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn('FAIL', r.stdout)

    def test_easing_reference_from_video(self):
        ref = (ROOT / 'references/motion-performance.md').read_text(encoding='utf-8')
        for word in ('linear', 'ease-in', 'ease-out', 'ease-in-out', 'overshoot', 'elastic', 'bounce', 'steps'):
            self.assertIn(word, ref)

    def test_original_demo_exists(self):
        demo = (ROOT / 'examples/dark-ui-demo.html').read_text(encoding='utf-8')
        self.assertIn('prefers-reduced-motion', demo)
        self.assertNotIn('http://', demo)
        self.assertNotIn('https://', demo)

if __name__ == '__main__':
    unittest.main()
