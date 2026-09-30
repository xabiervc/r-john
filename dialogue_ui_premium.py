"""Premium UI System with stat bars, accessibility, and polished interface"""
import json
import os

class PremiumUI:
    """Premium UI with visual stat bars, accessibility features"""
    
    def __init__(self):
        self.config = self.load_accessibility_config()
        self.text_scale = self.config.get('accessibility', {}).get('features', {}).get('visual', {}).get('textScaling', {}).get('default', 1.0)
        self.high_contrast = self.config.get('accessibility', {}).get('features', {}).get('visual', {}).get('highContrast', {}).get('default', False)
        self.show_stat_effects = self.config.get('accessibility', {}).get('features', {}).get('cognitive', {}).get('clearChoiceDescriptions', {}).get('showStatEffects', True)
        self.content_warnings_enabled = self.config.get('accessibility', {}).get('features', {}).get('cognitive', {}).get('contentWarnings', {}).get('default', True)
    
    def load_accessibility_config(self):
        try:
            with open('accessibility_config.json', 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def scale_text(self, text):
        """Scale text based on accessibility settings"""
        # In a real implementation, this would affect font size
        # For console, we just return the text
        return text
    
    def get_stat_bar(self, stat_name, value, max_value=100, width=20):
        """Create visual stat bar"""
        filled = int((value / max_value) * width)
        empty = width - filled
        
        # Color-blind safe colors
        if self.high_contrast:
            bar_char = '█'
            empty_char = '░'
        else:
            bar_char = '▓' if stat_name in ['reputation', 'trust'] else '▒'
            empty_char = '░'
        
        bar = bar_char * filled + empty_char * empty
        return f"[{bar}] {value:3d}/{max_value}"
    
    def display_stats(self, stats):
        """Display stats with visual bars"""
        print("\n" + "="*50)
        print("CHARACTER STATUS")
        print("="*50)
        
        # Reputation (blue in color, but we use text for colorblind)
        rep_bar = self.get_stat_bar('reputation', stats.get('reputation', 50))
        print(f"REPUTATION: {rep_bar}")
        
        # Lust (pink/red in color)
        lust_bar = self.get_stat_bar('lust', stats.get('lust', 30))
        print(f"LUST:       {lust_bar}")
        
        # Risk (orange/yellow in color)
        risk_bar = self.get_stat_bar('risk', stats.get('risk', 30))
        print(f"RISK:       {risk_bar}")
        
        print("="*50 + "\n")
    
    def display_choice_with_effects(self, option, index):
        """Display choice with stat effect preview"""
        text = option.get('text', '')
        
        if not self.show_stat_effects:
            print(f"  {index}. {text}")
            return
        
        # Build effect string
        effects = []
        if option.get('reputationEffect', 0) != 0:
            change = option['reputationEffect']
            sign = '+' if change > 0 else ''
            effects.append(f"Rep {sign}{change}")
        
        if option.get('lustEffect', 0) != 0:
            change = option['lustEffect']
            sign = '+' if change > 0 else ''
            effects.append(f"Lust {sign}{change}")
        
        if option.get('riskEffect', 0) != 0:
            change = option['riskEffect']
            sign = '+' if change > 0 else ''
            effects.append(f"Risk {sign}{change}")
        
        if effects:
            print(f"  {index}. {text} [{', '.join(effects)}]")
        else:
            print(f"  {index}. {text}")
    
    def display_content_warning(self, chapter_num):
        """Display content warning before sensitive chapters"""
        if not self.content_warnings_enabled:
            return
        
        warnings = {
            6: ["Political scandal", "Mental health themes", "Crisis situations"]
        }
        
        if chapter_num in warnings:
            print("\n" + "="*50)
            print("CONTENT WARNING")
            print("="*50)
            print(f"Chapter {chapter_num} contains:")
            for warning in warnings[chapter_num]:
                print(f"  ⚠ {warning}")
            print("\nThis chapter deals with mature themes.")
            print("Player discretion is advised.")
            print("="*50 + "\n")
            
            response = input("Continue? (y/n): ")
            if response.lower() != 'y':
                return False
        
        return True
    
    def display_chapter_header(self, chapter_num, title):
        """Display chapter transition with style"""
        print("\n")
        print("╔" + "═"*48 + "╗")
        print(f"║  CHAPTER {chapter_num}: {title:<35} ║")
        print("╚" + "═"*48 + "╝")
        print()
    
    def display_npc_text(self, npc_name, node, mood="Neutral"):
        """Display NPC dialogue with formatting"""
        text = node.get('text', '')
        if node.get('moodVariations'):
            text = node['moodVariations'].get(mood, text)
        
        print(f"\n{npc_name}: {text}")
    
    def display_private_thoughts(self, thoughts):
        """Display private thoughts with formatting"""
        if not thoughts:
            return
        
        print("\n[Private Thoughts]")
        for thought in thoughts:
            text = thought.get('text', '')
            mood = thought.get('mood', 'Neutral')
            print(f"  ({mood}) {text}")
        print()
    
    def display_options(self, options):
        """Display player choices with effects"""
        if not options:
            return None
        
        print("\nYour options:")
        for i, opt in enumerate(options, 1):
            self.display_choice_with_effects(opt, i)
        
        return options
    
    def get_player_choice(self, options):
        """Get player choice with validation"""
        while True:
            try:
                choice = input(f"\nChoose (1-{len(options)}): ")
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return options[idx]
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                print("\n\nGame saved. Goodbye!")
                exit(0)
    
    def display_ending(self, ending_name, description):
        """Display game ending with style"""
        print("\n")
        print("╔" + "═"*48 + "╗")
        print(f"║  ENDING: {ending_name:<37} ║")
        print("╚" + "═"*48 + "╝")
        print(f"\n{description}\n")
        print("Thank you for playing R-John: Power & Scandal\n")
    
    def display_settings_menu(self, current_settings):
        """Display settings menu"""
        print("\n" + "="*50)
        print("SETTINGS")
        print("="*50)
        print(f"1. Text Scale: {current_settings.get('text_scale', 1.0)}x")
        print(f"2. High Contrast: {'ON' if current_settings.get('high_contrast', False) else 'OFF'}")
        print(f"3. Show Stat Effects: {'ON' if current_settings.get('show_stat_effects', True) else 'OFF'}")
        print(f"4. Content Warnings: {'ON' if current_settings.get('content_warnings', True) else 'OFF'}")
        print(f"5. Difficulty: {current_settings.get('difficulty', 'standard')}")
        print(f"6. Back")
        print("="*50)
        
        return input("Choose (1-6): ")
