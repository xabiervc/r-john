"""Save/Load System for R-John"""
import json
import os

SAVE_DIR = "saves"

class SaveSystem:
    def __init__(self):
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
    
    def create_save_data(self, player_stats, flags, current_chapter, current_day, npc_states):
        """Create save data dictionary"""
        return {
            "player_stats": player_stats,
            "flags": list(flags),
            "current_chapter": current_chapter,
            "current_day": current_day,
            "npc_states": npc_states,
            "version": "1.0"
        }
    
    def save_game(self, save_name, player_stats, flags, current_chapter, current_day, npc_states):
        """Save game to file"""
        save_data = self.create_save_data(player_stats, flags, current_chapter, current_day, npc_states)
        filepath = os.path.join(SAVE_DIR, f"{save_name}.json")
        
        with open(filepath, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        return filepath
    
    def load_game(self, save_name):
        """Load game from file"""
        filepath = os.path.join(SAVE_DIR, f"{save_name}.json")
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            save_data = json.load(f)
        
        # Convert flags list back to set
        save_data["flags"] = set(save_data.get("flags", []))
        
        return save_data
    
    def list_saves(self):
        """List all available save files"""
        if not os.path.exists(SAVE_DIR):
            return []
        
        saves = []
        for filename in os.listdir(SAVE_DIR):
            if filename.endswith('.json'):
                saves.append(filename[:-5])  # Remove .json extension
        
        return saves
    
    def delete_save(self, save_name):
        """Delete a save file"""
        filepath = os.path.join(SAVE_DIR, f"{save_name}.json")
        
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False
    
    def get_save_info(self, save_name):
        """Get basic info about a save without loading full data"""
        filepath = os.path.join(SAVE_DIR, f"{save_name}.json")
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return {
            "name": save_name,
            "chapter": data.get("current_chapter", 1),
            "day": data.get("current_day", 1),
            "reputation": data.get("player_stats", {}).get("reputation", 50),
            "lust": data.get("player_stats", {}).get("lust", 30),
            "risk": data.get("player_stats", {}).get("risk", 30)
        }