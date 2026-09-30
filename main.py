"""R-John Game Engine - Main Entry Point"""
import json, os
from dialogue_engine import DialogueEngine
from narrative_engine import NarrativeEngine

class Game:
    def __init__(self):
        self.dialogue_engine = DialogueEngine()
        self.narrative_engine = NarrativeEngine()
        self.current_chapter = 1
        self.player_stats = {"reputation": 50, "lust": 30, "risk": 30}
        self.flags = set()
    
    def load_game(self):
        dialogue_dir = "data/dialogues"
        for chapter_dir in os.listdir(dialogue_dir):
            chapter_path = os.path.join(dialogue_dir, chapter_dir)
            if os.path.isdir(chapter_path):
                for file in os.listdir(chapter_path):
                    if file.endswith(".json"):
                        self.dialogue_engine.load_dialogue(os.path.join(chapter_path, file))
    
    def start_chapter(self, chapter_num):
        self.current_chapter = chapter_num
        print(f"\n=== Chapter {chapter_num}: Day {chapter_num} ===\n")
        self.narrative_engine.display_chapter(chapter_num)
    
    def play_dialogue(self, npc_id):
        dialogue_id = f"dialogue_{npc_id}_ch{self.current_chapter}"
        if dialogue_id in self.dialogue_engine.dialogues:
            self.dialogue_engine.play_dialogue(dialogue_id, self.player_stats, self.flags)
    
    def end_chapter(self):
        print(f"\n=== End of Chapter {self.current_chapter} ===")
        print(f"Stats: Rep={self.player_stats['reputation']}, Lust={self.player_stats['lust']}, Risk={self.player_stats['risk']}")
        if self.current_chapter < 7:
            self.current_chapter += 1
            return True
        return False
    
    def check_ending(self):
        rep, risk = self.player_stats['reputation'], self.player_stats['risk']
        if rep >= 70 and risk <= 30: return "Victory"
        elif rep >= 50 and risk <= 50: return "Damaged but Surviving"
        elif rep < 50 and risk <= 40: return "Strategic Retreat"
        else: return "Downfall"
    
    def run(self):
        self.load_game()
        for chapter in range(1, 8):
            self.start_chapter(chapter)
            npcs = self.get_npcs(chapter)
            for npc in npcs:
                print(f"\nTalking to {npc}...")
                self.play_dialogue(npc)
            if not self.end_chapter(): break
        print(f"\n=== ENDING: {self.check_ending()} ===\n")
    
    def get_npcs(self, chapter):
        npc_map = {
            1: ["maria", "laura", "emma"],
            2: ["jessica", "olivia", "victoria"],
            3: ["isabella"],
            4: ["natalie"],
            5: ["ashley"],
            6: ["maria", "laura", "emma"],
            7: ["maria", "laura", "emma", "jessica", "olivia", "victoria", "isabella", "natalie", "ashley"]
        }
        return npc_map.get(chapter, [])

if __name__ == "__main__":
    Game().run()