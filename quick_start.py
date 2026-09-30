#!/usr/bin/env python3
"""Quick start script for R-John"""

import sys
import os

def check_requirements():
    """Check if Python version is sufficient"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version_info.major}.{sys.version_info.minor}")
        return False
    return True

def check_files():
    """Check if required files exist"""
    required = [
        "main.py",
        "dialogue_engine.py",
        "narrative_engine.py",
        "dialogue_ui.py",
        "save_system.py",
        "data/dialogues/chapter_1",
        "narrative/chapter_1_narrative.md"
    ]
    
    missing = []
    for path in required:
        if not os.path.exists(path):
            missing.append(path)
    
    if missing:
        print("Warning: Some files are missing:")
        for m in missing:
            print(f"  - {m}")
        print("\nGame may not work correctly.\n")
        return False
    
    return True

def main():
    print("="*50)
    print("R-John - Political Drama Visual Novel")
    print("="*50)
    print()
    
    if not check_requirements():
        sys.exit(1)
    
    if not check_files():
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    print("Starting game...\n")
    
    # Import and run main game
    from main import Game
    game = Game()
    game.run()

if __name__ == "__main__":
    main()