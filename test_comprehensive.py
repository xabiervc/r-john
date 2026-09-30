"""Comprehensive tests for R-John"""
import json
import os

def test_all_dialogues_exist():
    """Test that all expected dialogue files exist"""
    expected = {
        "chapter_1": ["dialogue_maria_ch1.json", "dialogue_laura_ch1.json", "dialogue_emma_ch1.json"],
        "chapter_2": ["dialogue_jessica_ch2.json", "dialogue_olivia_ch2.json", "dialogue_victoria_ch2.json"],
        "chapter_3": ["dialogue_isabella_ch3.json"],
        "chapter_4": ["dialogue_natalie_ch4.json"],
        "chapter_5": ["dialogue_ashley_ch5.json"],
        "chapter_6": ["dialogue_maria_ch6.json", "dialogue_laura_ch6.json", "dialogue_emma_ch6.json"],
        "chapter_7": [
            "dialogue_maria_ch7.json", "dialogue_laura_ch7.json", "dialogue_emma_ch7.json",
            "dialogue_jessica_ch7.json", "dialogue_olivia_ch7.json", "dialogue_victoria_ch7.json",
            "dialogue_isabella_ch7.json", "dialogue_natalie_ch7.json", "dialogue_ashley_ch7.json"
        ]
    }
    
    errors = []
    base = "data/dialogues"
    
    for chapter, files in expected.items():
        chapter_path = os.path.join(base, chapter)
        if not os.path.exists(chapter_path):
            errors.append(f"Missing directory: {chapter_path}")
            continue
        
        for filename in files:
            filepath = os.path.join(chapter_path, filename)
            if not os.path.exists(filepath):
                errors.append(f"Missing file: {filepath}")
    
    return errors

def test_dialogue_schema():
    """Test that all dialogue files match the expected schema"""
    errors = []
    base = "data/dialogues"
    
    required_keys = ["id", "npcId", "chapter", "nodes"]
    node_required_keys = ["id", "text", "publicOptions"]
    option_required_keys = ["id", "text", "nextNode"]
    
    for root, _, files in os.walk(base):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            for key in required_keys:
                if key not in data:
                    errors.append(f"{filepath}: missing top-level key '{key}'")
            
            for node in data.get('nodes', []):
                for key in node_required_keys:
                    if key not in node:
                        errors.append(f"{filepath}: node missing key '{key}'")
                
                for option in node.get('publicOptions', []):
                    for key in option_required_keys:
                        if key not in option:
                            errors.append(f"{filepath}: option missing key '{key}'")
    
    return errors

def test_node_references():
    """Test that all nextNode references point to existing nodes"""
    errors = []
    base = "data/dialogues"
    
    for root, _, files in os.walk(base):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            node_ids = {node['id'] for node in data.get('nodes', [])}
            
            for node in data.get('nodes', []):
                for option in node.get('publicOptions', []):
                    next_node = option.get('nextNode')
                    if next_node is not None and next_node not in node_ids:
                        errors.append(f"{filepath}: option '{option.get('id')}' references non-existent node '{next_node}'")
    
    return errors

def test_no_duplicate_node_ids():
    """Test that there are no duplicate node IDs within a dialogue"""
    errors = []
    base = "data/dialogues"
    
    for root, _, files in os.walk(base):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            node_ids = []
            for node in data.get('nodes', []):
                node_id = node.get('id')
                if node_id in node_ids:
                    errors.append(f"{filepath}: duplicate node ID '{node_id}'")
                node_ids.append(node_id)
    
    return errors

def test_stat_values_in_range():
    """Test that all stat effects are within reasonable bounds"""
    errors = []
    base = "data/dialogues"
    
    for root, _, files in os.walk(base):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            for node in data.get('nodes', []):
                for option in node.get('publicOptions', []):
                    for stat in ['reputationEffect', 'lustEffect', 'riskEffect']:
                        value = option.get(stat, 0)
                        if not isinstance(value, int):
                            errors.append(f"{filepath}: {stat} is not an integer")
                        elif abs(value) > 50:
                            errors.append(f"{filepath}: {stat} value {value} seems too high")
    
    return errors

def test_narrative_files_exist():
    """Test that all narrative files exist"""
    expected = [
        "narrative/chapter_1_narrative.md",
        "narrative/chapter_2_narrative.md",
        "narrative/chapter_3_narrative.md",
        "narrative/chapter_4_narrative.md",
        "narrative/chapter_5_narrative.md",
        "narrative/chapter_6_narrative.md",
        "narrative/chapter_7_narrative.md"
    ]
    
    errors = []
    for filepath in expected:
        if not os.path.exists(filepath):
            errors.append(f"Missing narrative file: {filepath}")
    
    return errors

def test_python_modules_import():
    """Test that all Python modules can be imported"""
    errors = []
    modules = [
        "main",
        "dialogue_engine",
        "narrative_engine",
        "dialogue_ui",
        "save_system"
    ]
    
    for module in modules:
        try:
            __import__(module)
        except ImportError as e:
            errors.append(f"Cannot import {module}: {e}")
    
    return errors

if __name__ == "__main__":
    all_errors = []
    
    print("Running comprehensive tests...\n")
    
    print("1. Testing dialogue files exist...")
    errors = test_all_dialogues_exist()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("2. Testing dialogue schema...")
    errors = test_dialogue_schema()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("3. Testing node references...")
    errors = test_node_references()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("4. Testing for duplicate node IDs...")
    errors = test_no_duplicate_node_ids()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("5. Testing stat values in range...")
    errors = test_stat_values_in_range()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("6. Testing narrative files exist...")
    errors = test_narrative_files_exist()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("7. Testing Python modules import...")
    errors = test_python_modules_import()
    all_errors.extend(errors)
    print(f"   {'✓ PASS' if not errors else '✗ FAIL'} - {len(errors)} errors\n")
    
    print("="*50)
    if all_errors:
        print(f"FAILED - {len(all_errors)} total errors:\n")
        for error in all_errors:
            print(f"  - {error}")
    else:
        print("ALL TESTS PASSED ✓")
    print("="*50)