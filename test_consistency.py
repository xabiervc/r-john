"""Basic consistency tests for R-John"""
import json, os

def test_dialogue_consistency():
    errors = []
    base = 'data/dialogues'
    if not os.path.exists(base): return ['Dialogue directory missing']
    for root, _, files in os.walk(base):
        for filename in files:
            if filename.endswith('.json'):
                path = os.path.join(root, filename)
                with open(path) as f: data = json.load(f)
                for key in ('id', 'npcId', 'chapter', 'nodes'):
                    if key not in data: errors.append(f'{path}: missing {key}')
                ids = set()
                for node in data.get('nodes', []):
                    if node.get('id') in ids: errors.append(f'{path}: duplicate node')
                    ids.add(node.get('id'))
                    for key in ('id', 'text', 'publicOptions'):
                        if key not in node: errors.append(f'{path}: node missing {key}')
    return errors

def test_character_stats():
    with open('data/npcs.json') as f: npcs = json.load(f)
    errors = []
    for npc in npcs.get('npcs', []):
        for stat in ('reputation', 'lust', 'risk'):
            value = npc.get('stats', {}).get(stat, -1)
            if not 0 <= value <= 100: errors.append(f"{npc['id']}: invalid {stat}")
    return errors

if __name__ == '__main__':
    errors = test_dialogue_consistency() + test_character_stats()
    if errors:
        print('FAILED')
        print('\n'.join(errors))
    else:
        print('PASSED')