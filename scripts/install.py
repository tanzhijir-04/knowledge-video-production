"""Copy the portable skill into an agent skill root; refuse overwrites."""
import argparse
import os
from pathlib import Path
import shutil

NAME = 'knowledge-video-production'

def install(agent, target=None):
    source = Path(__file__).resolve().parents[1] / 'skills' / NAME
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Repository skill source is missing')
    if target is not None:
        base = Path(target).expanduser()
    elif agent == 'codex':
        base = Path(os.environ.get('CODEX_HOME') or str(Path.home() / '.codex')).expanduser() / 'skills'
    else:
        base = Path.home() / '.claude' / 'skills'
    dest = base.resolve() / NAME
    if dest.exists() or dest.is_symlink():
        raise FileExistsError(f'Refusing to overwrite existing skill: {dest}')
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    return dest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=['codex', 'claude-code'], required=True)
    parser.add_argument('--target', type=Path, help='Override agent skill root, not the final skill folder')
    args = parser.parse_args()
    try:
        dest = install(args.agent, args.target)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')
    print(f'Installed {NAME} for {args.agent}: {dest}')
    print('Reload skill discovery or start a new agent session. External tools are not installed.')

if __name__ == '__main__':
    main()
