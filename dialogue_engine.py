"""Dialogue Engine for R-John"""
import json

class DialogueEngine:
    def __init__(self):
        self.dialogues = {}
    
    def load_dialogue(self, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.dialogues[data.get('id')] = data
    
    def get_node(self, dialogue_id, node_id):
        if dialogue_id not in self.dialogues: return None
        for node in self.dialogues[dialogue_id].get('nodes', []):
            if node.get('id') == node_id: return node
        return None
    
    def process_choice(self, option, stats, flags):
        stats['reputation'] = max(0, min(100, stats['reputation'] + option.get('reputationEffect', 0)))
        stats['lust'] = max(0, min(100, stats['lust'] + option.get('lustEffect', 0)))
        stats['risk'] = max(0, min(100, stats['risk'] + option.get('riskEffect', 0)))
        if 'setFlag' in option: flags.add(option['setFlag'])
        return option.get('nextNode')
    
    def display_node(self, node, mood="Neutral"):
        if not node: return
        text = node.get('moodVariations', {}).get(mood, node.get('text', ''))
        print(f"\nNPC: {text}")
    
    def display_options(self, node):
        if not node: return []
        options = node.get('publicOptions', [])
        print("\nYour options:")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt.get('text', '')}")
        return options
    
    def play_dialogue(self, dialogue_id, stats, flags):
        if dialogue_id not in self.dialogues: return
        current_node_id = "start"
        while current_node_id:
            node = self.get_node(dialogue_id, current_node_id)
            if not node: break
            self.display_node(node)
            options = self.display_options(node)
            if not options: break
            try:
                choice = int(input("Choose (1-{}): ".format(len(options)))) - 1
                if 0 <= choice < len(options):
                    current_node_id = self.process_choice(options[choice], stats, flags)
                else: print("Invalid.")
            except ValueError: print("Enter a number.")