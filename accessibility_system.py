"""Accessibility System - Full implementation of accessibility features"""
import json
import os

class AccessibilitySystem:
    """Complete accessibility implementation"""
    
    def __init__(self):
        self.config = self.load_config()
        self.active_warnings = set()
    
    def load_config(self):
        """Load accessibility configuration"""
        try:
            with open('accessibility_config.json', 'r') as f:
                return json.load(f)
        except:
            return self.get_default_config()
    
    def get_default_config(self):
        """Get default accessibility config"""
        return {
            'accessibility': {
                'features': {
                    'visual': {
                        'textScaling': {'enabled': True, 'default': 1.0},
                        'highContrast': {'enabled': True, 'default': False},
                        'colorblindMode': {'enabled': True, 'default': False}
                    },
                    'cognitive': {
                        'clearChoiceDescriptions': {'enabled': True, 'default': True},
                        'contentWarnings': {'enabled': True, 'default': True}
                    },
                    'motor': {
                        'keyboardNavigation': {'enabled': True, 'fullSupport': True}
                    }
                },
                'difficulty': {
                    'default': 'standard'
                }
            }
        }
    
    def is_feature_enabled(self, feature_path):
        """Check if accessibility feature is enabled"""
        parts = feature_path.split('.')
        config = self.config
        
        for part in parts:
            if isinstance(config, dict):
                config = config.get(part, {})
            else:
                return False
        
        if isinstance(config, dict):
            return config.get('enabled', False) or config.get('default', False)
        return config
    
    def get_difficulty_modifier(self, difficulty=None):
        """Get stat change modifier for difficulty"""
        if difficulty is None:
            difficulty = self.config.get('difficulty', {}).get('default', 'standard')
        
        modifiers = {
            'story': 0.5,
            'standard': 1.0,
            'hardcore': 1.5
        }
        
        return modifiers.get(difficulty, 1.0)
    
    def get_content_warnings_for_chapter(self, chapter_num):
        """Get content warnings for specific chapter"""
        warnings = {
            1: [],
            2: ["Social pressure", "Political themes"],
            3: ["Workplace stress"],
            4: ["Political themes"],
            5: ["Romantic content", "Power dynamics"],
            6: ["Political scandal", "Mental health themes", "Crisis situations"],
            7: ["Consequences", "Relationship endings"]
        }
        
        return warnings.get(chapter_num, [])
    
    def should_show_warning(self, warning_type):
        """Check if warning type should be shown"""
        if not self.is_feature_enabled('accessibility.features.cognitive.contentWarnings'):
            return False
        
        return warning_type not in self.active_warnings
    
    def mark_warning_shown(self, warning_type):
        """Mark warning as shown (don't show again this session)"""
        self.active_warnings.add(warning_type)
    
    def get_keyboard_shortcuts(self):
        """Get keyboard shortcuts"""
        return {
            'next': ['Enter', 'Space', 'RightArrow'],
            'back': ['Escape', 'LeftArrow'],
            'save': ['Ctrl+S'],
            'load': ['Ctrl+L'],
            'settings': ['Ctrl+P'],
            'quit': ['Ctrl+Q']
        }
    
    def is_keyboard_navigation_enabled(self):
        """Check if keyboard navigation is enabled"""
        return self.is_feature_enabled('accessibility.features.motor.keyboardNavigation')
    
    def get_text_scale(self):
        """Get text scale factor"""
        return self.config.get('accessibility', {}).get('features', {}).get('visual', {}).get('textScaling', {}).get('default', 1.0)
    
    def is_high_contrast_enabled(self):
        """Check if high contrast mode is enabled"""
        return self.config.get('accessibility', {}).get('features', {}).get('visual', {}).get('highContrast', {}).get('default', False)
    
    def is_colorblind_mode_enabled(self):
        """Check if colorblind mode is enabled"""
        return self.config.get('accessibility', {}).get('features', {}).get('visual', {}).get('colorblindMode', {}).get('default', False)
    
    def should_show_stat_effects(self):
        """Check if stat effects should be shown in choices"""
        return self.config.get('accessibility', {}).get('features', {}).get('cognitive', {}).get('clearChoiceDescriptions', {}).get('showStatEffects', True)
    
    def update_setting(self, setting_path, value):
        """Update accessibility setting"""
        parts = setting_path.split('.')
        config = self.config
        
        for i, part in enumerate(parts[:-1]):
            if part not in config:
                config[part] = {}
            config = config[part]
        
        config[parts[-1]] = value
        
        # Save updated config
        self.save_config()
    
    def save_config(self):
        """Save accessibility config to file"""
        with open('accessibility_config.json', 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get_settings_dict(self):
        """Get current settings as dict for UI"""
        return {
            'text_scale': self.get_text_scale(),
            'high_contrast': self.is_high_contrast_enabled(),
            'colorblind_mode': self.is_colorblind_mode_enabled(),
            'show_stat_effects': self.should_show_stat_effects(),
            'content_warnings': self.is_feature_enabled('accessibility.features.cognitive.contentWarnings'),
            'difficulty': self.config.get('difficulty', {}).get('default', 'standard'),
            'keyboard_navigation': self.is_keyboard_navigation_enabled()
        }
