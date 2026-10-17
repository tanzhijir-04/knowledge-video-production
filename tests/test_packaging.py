import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class PackagingTests(unittest.TestCase):
    def test_install_both_agents_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            for agent in ['codex', 'claude-code']:
                target = Path(temp) / agent
                result = installer.install(agent, target)
                self.assertEqual(result.name, installer.NAME)
                self.assertTrue((result / 'references/project-structure.md').is_file())
                self.assertTrue((result / 'scripts/init_project.py').is_file())
                with self.assertRaises(FileExistsError):
                    installer.install(agent, target)

    def test_codex_home_override(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, {'CODEX_HOME': temp}):
            result = installer.install('codex')
            self.assertEqual(result, Path(temp).resolve() / 'skills' / installer.NAME)

    def test_claude_default_root(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(Path, 'home', return_value=Path(temp)):
            result = installer.install('claude-code')
            self.assertEqual(result, Path(temp).resolve() / '.claude/skills' / installer.NAME)

    def test_structured_project_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / 'film'
            args = [sys.executable, str(ROOT / 'skills' / installer.NAME / 'scripts/init_project.py'), str(dest), '--topic', 'Test']
            subprocess.run(args, check=True, capture_output=True)
            for folder in ['research', 'script', 'design/storyboard', 'project/data', 'project/media/audio/music', 'delivery', 'evidence']:
                self.assertTrue((dest / folder).is_dir())
            self.assertEqual(json.loads((dest / 'project/data/assets.json').read_text())['assets'], [])
            config = json.loads((dest / 'production.json').read_text(encoding='utf-8'))
            self.assertEqual(config['video']['fps'], 60)
            self.assertFalse(config['video']['burnNarrationSubtitles'])
            self.assertFalse((dest / 'project/data/timeline.json').exists())
            self.assertNotEqual(subprocess.run(args, capture_output=True).returncode, 0)

if __name__ == '__main__':
    unittest.main()
