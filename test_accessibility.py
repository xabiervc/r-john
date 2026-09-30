"""Accessibility Tests - Ensure all accessibility features work"""
import json
import os
from accessibility_system import AccessibilitySystem

def test_accessibility_config_exists():
    """Test that accessibility config file exists"""
    assert os.path.exists('accessibility_config.json'), "accessibility_config.json must exist"
    print("✓ Accessibility config exists")

def test_accessibility_config_valid():
    """Test that accessibility config is valid JSON"""
    with open('accessibility_config.json', 'r') as f:
        config = json.load(f)
    
    assert 'accessibility' in config, "Config must have 'accessibility' key"
    assert 'features' in config['accessibility'], "Must have 'features' section"
    print("✓ Accessibility config is valid JSON")

def test_visual_features():
    """Test visual accessibility features"""
    with open('accessibility_config.json', 'r') as f:
        config = json.load(f)
    
    visual = config['accessibility']['features']['visual']
    
    assert 'textScaling' in visual, "Must have text scaling"
    assert 'highContrast' in visual, "Must have high contrast mode"
    assert 'colorblindMode' in visual, "Must have colorblind mode"
    
    assert visual['textScaling']['enabled'] == True, "Text scaling must be enabled"
    assert visual['highContrast']['enabled'] == True, "High contrast must be enabled"
    assert visual['colorblindMode']['enabled'] == True, "Colorblind mode must be enabled"
    
    print("✓ Visual features configured")

def test_cognitive_features():
    """Test cognitive accessibility features"""
    with open('accessibility_config.json', 'r') as f:
        config = json.load(f)
    
    cognitive = config['accessibility']['features']['cognitive']
    
    assert 'clearChoiceDescriptions' in cognitive, "Must have clear choice descriptions"
    assert 'contentWarnings' in cognitive, "Must have content warnings"
    
    assert cognitive['clearChoiceDescriptions']['enabled'] == True, "Choice descriptions must be enabled"
    assert cognitive['contentWarnings']['enabled'] == True, "Content warnings must be enabled"
    
    print("✓ Cognitive features configured")

def test_motor_features():
    """Test motor accessibility features"""
    with open('accessibility_config.json', 'r') as f:
        config = json.load(f)
    
    motor = config['accessibility']['features']['motor']
    
    assert 'keyboardNavigation' in motor, "Must have keyboard navigation"
    assert motor['keyboardNavigation']['enabled'] == True, "Keyboard navigation must be enabled"
    assert motor['keyboardNavigation']['fullSupport'] == True, "Full keyboard support required"
    
    print("✓ Motor features configured")

def test_difficulty_modes():
    """Test difficulty modes exist"""
    with open('accessibility_config.json', 'r') as f:
        config = json.load(f)
    
    difficulty = config['difficulty']
    
    assert 'modes' in difficulty, "Must have difficulty modes"
    assert 'story' in difficulty['modes'], "Must have story mode"
    assert 'standard' in difficulty['modes'], "Must have standard mode"
    assert 'hardcore' in difficulty['modes'], "Must have hardcore mode"
    
    print("✓ Difficulty modes configured")

def test_accessibility_system_class():
    """Test AccessibilitySystem class works"""
    system = AccessibilitySystem()
    
    # Test config loading
    config = system.load_config()
    assert config is not None, "Config must load"
    
    # Test feature checks
    assert system.is_feature_enabled('accessibility.features.visual.textScaling') == True
    assert system.is_feature_enabled('accessibility.features.motor.keyboardNavigation') == True
    
    # Test difficulty modifier
    assert system.get_difficulty_modifier('story') == 0.5
    assert system.get_difficulty_modifier('standard') == 1.0
    assert system.get_difficulty_modifier('hardcore') == 1.5
    
    # Test content warnings
    warnings = system.get_content_warnings_for_chapter(6)
    assert len(warnings) > 0, "Chapter 6 must have warnings"
    
    # Test settings dict
    settings = system.get_settings_dict()
    assert 'text_scale' in settings
    assert 'difficulty' in settings
    
    print("✓ AccessibilitySystem class works")

def test_content_warnings_all_chapters():
    """Test content warnings for all chapters"""
    system = AccessibilitySystem()
    
    for chapter in range(1, 8):
        warnings = system.get_content_warnings_for_chapter(chapter)
        assert isinstance(warnings, list), f"Chapter {chapter} warnings must be list"
    
    print("✓ Content warnings for all chapters")

def test_keyboard_shortcuts():
    """Test keyboard shortcuts are defined"""
    system = AccessibilitySystem()
    shortcuts = system.get_keyboard_shortcuts()
    
    assert 'next' in shortcuts, "Must have 'next' shortcut"
    assert 'back' in shortcuts, "Must have 'back' shortcut"
    assert 'save' in shortcuts, "Must have 'save' shortcut"
    assert 'load' in shortcuts, "Must have 'load' shortcut"
    assert 'quit' in shortcuts, "Must have 'quit' shortcut"
    
    print("✓ Keyboard shortcuts defined")

if __name__ == "__main__":
    print("\nRunning Accessibility Tests...\n")
    
    tests = [
        test_accessibility_config_exists,
        test_accessibility_config_valid,
        test_visual_features,
        test_cognitive_features,
        test_motor_features,
        test_difficulty_modes,
        test_accessibility_system_class,
        test_content_warnings_all_chapters,
        test_keyboard_shortcuts
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Accessibility Tests: {passed}/{len(tests)} passed")
    if failed == 0:
        print("ALL ACCESSIBILITY TESTS PASSED ✓")
    else:
        print(f"FAILED: {failed} tests")
    print(f"{'='*50}\n")
