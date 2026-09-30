"""Dialogue UI for R-John - Handles rendering and user input"""

class DialogueUI:
    def __init__(self):
        self.current_mood = "Neutral"
    
    def set_mood(self, mood):
        """Set the current mood for dialogue variations"""
        valid_moods = ["Stressed", "Relaxed", "Neutral"]
        if mood in valid_moods:
            self.current_mood = mood
        else:
            self.current_mood = "Neutral"
    
    def display_npc_text(self, npc_name, node, mood=None):
        """Display NPC dialogue with mood variation"""
        if mood is None:
            mood = self.current_mood
        
        text = node.get('moodVariations', {}).get(mood, node.get('text', ''))
        print(f"\n{npc_name}: {text}")
    
    def display_options(self, options):
        """Display player choices and return selection"""
        if not options:
            return None
        
        print("\nYour options:")
        for i, opt in enumerate(options, 1):
            text = opt.get('text', '')
            rep = opt.get('reputationEffect', 0)
            lust = opt.get('lustEffect', 0)
            risk = opt.get('riskEffect', 0)
            
            effects = []
            if rep != 0: effects.append(f"Rep {rep:+d}")
            if lust != 0: effects.append(f"Lust {lust:+d}")
            if risk != 0: effects.append(f"Risk {risk:+d}")
            
            if effects:
                print(f"  {i}. {text} [{', '.join(effects)}]")
            else:
                print(f"  {i}. {text}")
        
        while True:
            try:
                choice = input(f"Choose (1-{len(options)}): ")
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return options[idx]
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number")
    
    def display_stats(self, stats):
        """Display current player stats"""
        print(f"\n=== Stats ===")
        print(f"Reputation: {stats.get('reputation', 50)}/100")
        print(f"Lust: {stats.get('lust', 30)}/100")
        print(f"Risk: {stats.get('risk', 30)}/100")
        print(f"=============\n")
    
    def display_private_thoughts(self, thoughts):
        """Display character's private thoughts"""
        if not thoughts:
            return
        
        print("\n[Private thoughts]")
        for thought in thoughts:
            text = thought.get('text', '')
            mood = thought.get('mood', 'Neutral')
            print(f"  ({mood}) {text}")
        print()
    
    def display_chapter_header(self, chapter_num, title):
        """Display chapter transition"""
        print(f"\n{'='*50}")
        print(f"CHAPTER {chapter_num}: {title}")
        print(f"{'='*50}\n")
    
    def display_ending(self, ending_name, description):
        """Display game ending"""
        print(f"\n{'='*50}")
        print(f"ENDING: {ending_name}")
        print(f"{'='*50}")
        print(f"\n{description}\n")