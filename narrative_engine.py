"""Narrative Engine for R-John"""
import os

class NarrativeEngine:
    def __init__(self):
        self.chapters = {}
    
    def load_chapter(self, filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        filename = os.path.basename(filepath)
        try:
            num = int(filename.split('_')[1].split('.')[0])
            self.chapters[num] = content
        except (ValueError, IndexError):
            pass
    
    def display_chapter(self, chapter_num):
        if chapter_num not in self.chapters:
            print(f"Narrative chapter {chapter_num} not found.")
            return
        print(self.chapters[chapter_num])