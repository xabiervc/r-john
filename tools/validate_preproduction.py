#!/usr/bin/env python3
"""Offline preproduction validator for dialogue JSON and chapter references."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIALOGUES = ROOT / 'data' / 'dialogues'

def load(path: Path):
    with path.open(encoding='utf-8') as fh:
        return json.load(fh)

def validate_tree(path: Path):
    data = load(path)
    errors = []
    nodes = data.get('nodes', [])
    ids = [node.get('id') for node in nodes]
    known = set(ids)
    if not data.get('dialogue_id'):
        errors.append('missing dialogue_id')
    if not data.get('npc_id'):
        errors.append('missing npc_id')
    if len(ids) != len(known):
        errors.append('duplicate node IDs')
    for node in nodes:
        node_id = node.get('id', '<missing>')
        choices = node.get('choices', [])
        if not choices and not node.get('ending'):
            errors.append(f'{node_id}: non-terminal node without choices')
        for choice in choices:
            target = choice.get('next')
            if target not in known:
                errors.append(f'{node_id}: unknown target {target!r}')
    return errors

def main():
    failures = 0
    for path in sorted(DIALOGUES.rglob('*.json')):
        try:
            errors = validate_tree(path)
        except Exception as exc:
            errors = [f'cannot parse JSON: {exc}']
        if errors:
            failures += 1
            print(f'FAIL {path.relative_to(ROOT)}')
            for error in errors:
                print(f'  - {error}')
        else:
            print(f'PASS {path.relative_to(ROOT)}')
    raise SystemExit(1 if failures else 0)

if __name__ == '__main__':
    main()
