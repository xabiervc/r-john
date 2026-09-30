#!/usr/bin/env python3
"""R-John: Power & Scandal - Premium Edition
Award-quality political drama visual novel
"""
import json, os, sys
from dialogue_engine_premium import PremiumDialogueEngine, RelationshipTracker
from narrative_engine import NarrativeEngine
from dialogue_ui import DialogueUI
from save_system import SaveSystem

class PremiumGame:
    def __init__(self):
        self.dialogue_engine = PremiumDialogueEngine()
        self.narrative_engine = NarrativeEngine()
        self.ui = DialogueUI()
        self.save_system = SaveSystem()
        
        # Game state
        self.player_stats = {"reputation": 50, "lust": 30, "risk": 30}
        self.flags = set()
        self.current_chapter = 1
        self.difficulty = "standard"
        self.accessibility = self.load_accessibility_config()
    
    def load_accessibility_config(self):
        """Load accessibility settings"""
        try:
            with open('accessibility_config.json', 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def apply_difficulty_modifier(self, value):
        """Apply difficulty multiplier to stat changes"""
        modifiers = {"story": 0.5, "standard": 1.0, "hardcore": 1.5}
        return int(value * modifiers.get(self.difficulty, 1.0))
    
    def load_all_dialogues(self):
        """Load all dialogue trees from data/dialogues"""
        dialogue_dir = "data/dialogues"
        if not os.path.exists(dialogue_dir):
            print("Warning: Dialogue directory not found")
            return
        
        for chapter_dir in os.listdir(dialogue_dir):
            chapter_path = os.path.join(dialogue_dir, chapter_dir)
            if os.path.isdir(chapter_path):
                for file in os.listdir(chapter_path):
                    if file.endswith(".json"):
                        self.dialogue_engine.load_dialogue(os.path.join(chapter_path, file))
    
    def start_chapter(self, chapter_num):
        """Display chapter introduction"""
        self.current_chapter = chapter_num
        self.ui.display_chapter_header(chapter_num, self.get_chapter_title(chapter_num))
        self.narrative_engine.display_chapter(chapter_num)
    
    def get_chapter_title(self, chapter_num):
        """Get chapter title"""
        titles = {
            1: "The Office",
            2: "The Charity Gala",
            3: "The Campaign Trail",
            4: "Capitol Hill",
            5: "The Fundraiser",
            6: "The Scandal",
            7: "Resolution"
        }
        return titles.get(chapter_num, f"Day {chapter_num}")
    
    def play_dialogue(self, npc_id):
        """Play dialogue with NPC"""
        dialogue_id = f"dialogue_{npc_id}_ch{self.current_chapter}"
        
        if dialogue_id not in self.dialogue_engine.dialogues:
            # Try premium version
            dialogue_id = f"dialogue_{npc_id}_ch{self.current_chapter}_premium"
        
        if dialogue_id in self.dialogue_engine.dialogues:
            game_state = {
                'stats': self.player_stats,
                'flags': self.flags,
                'chapter': self.current_chapter
            }
            
            def ui_callback(data):
                if data['type'] == 'dialogue_node':
                    self.ui.display_npc_text(data['npc_id'], {'text': data['text']})
                    if data.get('thoughts'):
                        self.ui.display_private_thoughts(data['thoughts'])
                    options = self.dialogue_engine.get_available_options(
                        {'publicOptions': data['options']}, 
                        game_state
                    )
                    return self.ui.display_options(options)
                elif data['type'] == 'get_choice':
                    # Get player input
                    try:
                        choice = int(input("Choose (1-{}): ".format(len(data['options'])))) - 1
                        if 0 <= choice < len(data['options']):
                            return data['options'][choice]
                    except:
                        pass
                    return data['options'][0]  # Default to first
            
            results = self.dialogue_engine.play_dialogue(dialogue_id, game_state, ui_callback)
            
            # Apply difficulty modifier to stat changes
            for effect in results.get('effects', []):
                if effect.get('type') == 'stat_change':
                    for stat, change in effect['changes'].items():
                        self.player_stats[stat] = max(0, min(100, 
                            self.player_stats[stat] + self.apply_difficulty_modifier(change)))
    
    def end_chapter(self):
        """End chapter, show stats, auto-save"""
        self.ui.display_stats(self.player_stats)
        
        # Auto-save at chapter end
        self.save_system.save_game(
            f"chapter_{self.current_chapter}_autosave",
            self.player_stats,
            self.flags,
            self.current_chapter,
            self.current_chapter,
            self.dialogue_engine.relationship_tracker.get_all_relationships()
        )
        
        if self.current_chapter < 7:
            self.current_chapter += 1
            return True
        return False
    
    def check_ending(self):
        """Determine which ending player gets"""
        rep = self.player_stats['reputation']
        risk = self.player_stats['risk']
        lust = self.player_stats['lust']
        
        if rep >= 75 and risk <= 25:
            return "Victory: Statesman"
        elif rep >= 70 and risk <= 30 and lust >= 60:
            return "Victory: Power Broker"
        elif rep >= 50 and risk <= 50:
            return "Damaged but Surviving: Cautious Politician"
        elif rep >= 40 and lust >= 70 and risk <= 40:
            return "Damaged but Surviving: Private Life"
        elif rep >= 30 and risk <= 35:
            return "Strategic Retreat: Reinvention"
        elif rep < 30 and risk >= 60:
            return "Downfall: Disgraced"
        elif rep < 20 and risk >= 70 and lust >= 80:
            return "Downfall: Destroyed"
        else:
            return "Strategic Retreat: Scandalized Exit"
    
    def get_npcs_for_chapter(self, chapter):
        """Get list of NPCs for chapter"""
        npc_map = {
            1: ["maria", "laura", "emma"],
            2: ["jessica", "olivia", "victoria"],
            3: ["isabella"],
            4: ["natalie"],
            5: ["ashley"],
            6: ["maria", "laura", "emma"],
            7: ["maria", "laura", "emma", "jessica", "olivia", "victoria", 
                "isabella", "natalie", "ashley"]
        }
        return npc_map.get(chapter, [])
    
    def show_main_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("R-JOHN: POWER & SCANDAL")
        print("Premium Edition")
        print("="*50)
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Settings")
        print("4. Quit")
        
        try:
            choice = input("\nChoose (1-4): ")
            if choice == "1":
                return "new"
            elif choice == "2":
                return "load"
            elif choice == "3":
                self.show_settings()
                return "menu"
            else:
                return "quit"
        except:
            return "quit"
    
    def show_settings(self):
        """Show settings menu"""
        print("\n--- Settings ---")
        print(f"Difficulty: {self.difficulty}")
        print("1. Change Difficulty")
        print("2. Back")
        
        try:
            choice = input("Choose (1-2): ")
            if choice == "1":
                print("\n1. Story (reduced consequences)")
                print("2. Standard (balanced)")
                print("3. Hardcore (maximum consequences)")
                diff = input("Choose (1-3): ")
                self.difficulty = {"1": "story", "2": "standard", "3": "hardcore"}.get(diff, "standard")
        except:
            pass
    
    def run(self):
        """Main game loop"""
        print("\nLoading game...")
        self.load_all_dialogues()
        
        while True:
            menu_choice = self.show_main_menu()
            
            if menu_choice == "quit":
                print("\nThank you for playing!")
                break
            elif menu_choice == "new":
                # Reset game state
                self.player_stats = {"reputation": 50, "lust": 30, "risk": 30}
                self.flags = set()
                self.current_chapter = 1
                
                # Play through chapters
                for chapter in range(1, 8):
                    self.start_chapter(chapter)
                    npcs = self.get_npcs_for_chapter(chapter)
                    for npc in npcs:
                        print(f"\n--- Talking to {npc.capitalize()} ---")
                        self.play_dialogue(npc)
                    if not self.end_chapter():
                        break
                
                # Show ending
                ending = self.check_ending()
                self.ui.display_ending(ending, "Your choices have shaped your legacy.")
                
            elif menu_choice == "load":
                saves = self.save_system.list_saves()
                if saves:
                    print("\nAvailable saves:")
                    for i, save in enumerate(saves, 1):
                        print(f"  {i}. {save}")
                    try:
                        choice = int(input("Choose save (1-{}): ".format(len(saves)))) - 1
                        if 0 <= choice < len(saves):
                            data = self.save_system.load_game(saves[choice])
                            if data:
                                self.player_stats = data.get('player_stats', self.player_stats)
                                self.flags = data.get('flags', set())
                                self.current_chapter = data.get('current_chapter', 1)
                                print(f"\nLoaded: {saves[choice]}")
                    except:
                        pass
                else:
                    print("\nNo saves found.")

if __name__ == "__main__":
    try:
        PremiumGame().run()
    except KeyboardInterrupt:
        print("\n\nGame saved. Goodbye!")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please report this issue.")
