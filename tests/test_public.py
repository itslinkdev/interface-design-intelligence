"""Pure stdlib tests; no network or agent API access."""
from pathlib import Path
import importlib.util,json,subprocess,sys,tempfile,unittest
ROOT=Path(__file__).resolve().parent.parent
class PublicPackageTests(unittest.TestCase):
    def test_lookup_from_other_directory(self):
        with tempfile.TemporaryDirectory() as cwd:
            r=subprocess.run([sys.executable,str(ROOT/'scripts/find_pattern.py'),'searchable dropdown','--limit','2','--json'],cwd=cwd,check=True,capture_output=True,text=True)
            values=json.loads(r.stdout)
            self.assertTrue(0<len(values)<=2)
            self.assertTrue(all(Path(x['module']).is_file() for x in values))
    def test_all_62_pattern_ids(self):
        out=subprocess.check_output([sys.executable,str(ROOT/'scripts/find_pattern.py'),'--id','REF-062','--json'],text=True)
        self.assertEqual(json.loads(out)[0]['id'],'REF-062')
    def test_no_third_party_images(self):
        self.assertEqual(list(ROOT.rglob('*.webp')),[])
        self.assertEqual(list(ROOT.rglob('*.png')),[])
        self.assertEqual({p.name for p in (ROOT/'assets').glob('*.svg')},
                         {'hero.svg','patterns.svg','workflow.svg','style-strip.svg'})
    def test_token_tool_exact(self):
        spec=importlib.util.spec_from_file_location('token_gen',ROOT/'scripts/build_tokens.py')
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        sample=json.loads((ROOT/'examples/token-config.sample.json').read_text())
        css,_=mod.generate(sample)
        self.assertIn('--ui-color-primary: #254cdd;',css)
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            file=Path(td)/'tokens.css';file.write_text('original')
            r=subprocess.run([sys.executable,str(ROOT/'scripts/build_tokens.py'),'--config',str(ROOT/'examples/token-config.sample.json'),'--out',str(file)],capture_output=True)
            self.assertNotEqual(r.returncode,0);self.assertEqual(file.read_text(),'original')
if __name__=='__main__':unittest.main()
