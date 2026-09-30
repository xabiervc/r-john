"""Premium Dialogue Engine with relationship tracking and consequences"""
import json, os
from typing import Dict, List, Optional, Set, Tuple

class RelationshipTracker:
    def __init__(self):
        self.relationships = {}
        self.default_stats = {'trust': 50, 'respect': 50, 'attraction': 30, 'loyalty': 50}
    
    def get_relationship(self, npc_id: str) -> Dict[str, int]:
        if npc_id not in self.relationships:
            self.relationships[npc_id] = self.default_stats.copy()
        return self.relationships[npc_id]
    
    def update_relationship(self, npc_id: str, stat: str, change: int):
        rel = self.get_relationship(npc_id)
        if stat in rel:
            rel[stat] = max(0, min(100, rel[stat] + change))

class ConsequenceEngine:
    def __init__(self):
        self.delayed_consequences = []
    
    def add_delayed_consequence(self, consequence: Dict):
        self.delayed_consequences.append(consequence)
    
    def check_and_trigger(self, current_chapter: int, game_state: Dict) -> List[Dict]:
        triggered = []
        remaining = []
        for consequence in self.delayed_consequences:
            if consequence.get('chapter') == current_chapter:
                triggered.append(consequence)
            else:
                remaining.append(consequence)
        self.delayed_consequences = remaining
        return triggered

class PremiumDialogueEngine:
    def __init__(self):
        self.dialogues = {}
        self.relationship_tracker = RelationshipTracker()
        self.consequence_engine = ConsequenceEngine()
        self.current_mood = "Neutral"
    
    def load_dialogue(self, filepath: str):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.dialogues[data.get('id')] = data
    
    def process_choice(self, option: Dict, game_state: Dict) -> Tuple[Optional[str], List[Dict]]:
        effects = []
        for stat in ['reputationEffect', 'lustEffect', 'riskEffect']:
            if stat in option:
                stat_name = stat.replace('Effect', '')
                change = option[stat]
                current = game_state['stats'].get(stat_name, 50)
                game_state['stats'][stat_name] = max(0, min(100, current + change))
        if 'flagSet' in option:
            game_state['flags'].add(option['flagSet'])
        return option.get('nextNode'), effects
