extends Node2D

@onready var dialogue_text: RichTextLabel = $UI/TextBox/DialogueText
@onready var character_name: Label = $UI/TextBox/CharacterName
@onready var choices_container: VBoxContainer = $UI/TextBox/ChoicesContainer
@onready var character_portrait: Sprite2D = $CharacterPortrait
@onready var stats_ui: CanvasLayer = $StatsUI

var current_dialogue: Dictionary = {}
var current_segment: String = ""
var player_stats: Dictionary = {"reputation": 50, "lust": 30, "risk": 30}
var npc_relationships: Dictionary = {}

func _ready():
    load_dialogue("res://data/dialogues/chapter_1/dialogue_maria_ch1.json")
    update_stats_ui()

func load_dialogue(file_path: String):
    var file = FileAccess.open(file_path, FileAccess.READ)
    var json_string = file.get_as_text()
    file.close()
    
    var json = JSON.new()
    var parse_result = json.parse(json_string)
    if parse_result == OK:
        current_dialogue = json.data
        start_segment("greeting")
    else:
        print("Error loading dialogue: ", json.get_error_message())

func start_segment(segment_id: String):
    current_segment = segment_id
    var segment = current_dialogue["segments"].filter(func(s): return s["id"] == segment_id)[0]
    
    character_name.text = segment["speaker"].capitalize()
    dialogue_text.text = segment["text"]
    
    # Clear previous choices
    for child in choices_container.get_children():
        child.queue_free()
    
    # Create choice buttons
    for choice in segment["choices"]:
        var button = Button.new()
        button.text = choice["text"]
        button.pressed.connect(_on_choice_selected.bind(choice))
        choices_container.add_child(button)

func _on_choice_selected(choice: Dictionary):
    # Apply effects
    if "effect" in choice:
        for stat in choice["effect"].keys():
            if stat in player_stats:
                player_stats[stat] += choice["effect"][stat]
            else:
                npc_relationships[stat] = choice["effect"][stat]
    
    update_stats_ui()
    
    # Move to next segment
    if "next" in choice:
        start_segment(choice["next"])

func update_stats_ui():
    $StatsUI/ReputationBar.value = player_stats["reputation"]
    $StatsUI/LustBar.value = player_stats["lust"]
    $StatsUI/RiskBar.value = player_stats["risk"]
