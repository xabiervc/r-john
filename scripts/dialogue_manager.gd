extends Node2D

@onready var dialogue_text: RichTextLabel = $UI/TextBox/DialogueText
@onready var character_name: Label = $UI/TextBox/CharacterName
@onready var choices_container: VBoxContainer = $UI/TextBox/ChoicesContainer
@onready var character_portrait: Sprite2D = $CharacterPortrait
@onready var stats_ui: CanvasLayer = $StatsUI
@onready var reputation_bar: ProgressBar = $StatsUI/ReputationBar
@onready var lust_bar: ProgressBar = $StatsUI/LustBar
@onready var risk_bar: ProgressBar = $StatsUI/RiskBar

var day_flow: Dictionary = {}
var current_npc: String = ""
var current_dialogue: Dictionary = {}
var current_node_id: String = ""
var player_stats: Dictionary = {"reputation": 50, "lust": 30, "risk": 30}
var npc_relationships: Dictionary = {}
var flags: Array = []

func _ready():
    load_day_flow("res://data/dialogues/chapter_1/dialogue_day1.json")
    update_stats_ui()

func load_day_flow(file_path: String):
    var file = FileAccess.open(file_path, FileAccess.READ)
    var json_string = file.get_as_text()
    file.close()
    var json = JSON.new()
    if json.parse(json_string) == OK:
        day_flow = json.data
        start_npc(day_flow["sequence"][0])
    else:
        push_error("Failed to load day flow: " + json.get_error_message())

func start_npc(npc_id: String):
    current_npc = npc_id
    var file_path = day_flow["files"][npc_id]
    var file = FileAccess.open(file_path, FileAccess.READ)
    var json_string = file.get_as_text()
    file.close()
    var json = JSON.new()
    if json.parse(json_string) == OK:
        current_dialogue = json.data
        current_node_id = "start"
        show_node(current_node_id)
    else:
        push_error("Failed to load dialogue for npc: " + npc_id)

func show_node(node_id: String):
    current_node_id = node_id
    var nodes = current_dialogue.get("nodes", [])
    var node = null
    for n in nodes:
        if n.get("id") == node_id:
            node = n
            break
    if node == null:
        push_error("Node not found: " + node_id)
        return

    character_name.text = current_npc.capitalize()
    dialogue_text.text = node.get("text", "")

    # Clear previous choices
    for child in choices_container.get_children():
        child.queue_free()

    # Create choice buttons
    var options = node.get("publicOptions", [])
    if options.size() == 0:
        # No choices: auto-advance to next NPC or end
        await get_tree().create_timer(2.0).timeout
        advance_or_finish()
        return

    for opt in options:
        var button = Button.new()
        button.text = opt.get("text", "")
        button.pressed.connect(_on_choice_selected.bind(opt))
        choices_container.add_child(button)

func _on_choice_selected(option: Dictionary):
    # Apply effects
    var rep = option.get("reputationEffect", 0)
    var lust = option.get("lustEffect", 0)
    var risk = option.get("riskEffect", 0)
    player_stats["reputation"] = clamp(player_stats["reputation"] + rep, 0, 100)
    player_stats["lust"] = clamp(player_stats["lust"] + lust, 0, 100)
    player_stats["risk"] = clamp(player_stats["risk"] + risk, 0, 100)

    # Flags
    var flag = option.get("flagSet", "")
    if flag != "" and not flags.has(flag):
        flags.append(flag)

    update_stats_ui()

    # Move to next node
    var next_id = option.get("nextNode", null)
    if next_id:
        show_node(next_id)
    else:
        advance_or_finish()

func advance_or_finish():
    var idx = day_flow["sequence"].find(current_npc)
    if idx >= 0 and idx < day_flow["sequence"].size() - 1:
        start_npc(day_flow["sequence"][idx + 1])
    else:
        finish_day()

func finish_day():
    # Save simple state
    save_game()
    # Load summary scene
    var ending_scene = day_flow.get("ending", {}).get("scene", "res://scenes/day1_summary.tscn")
    get_tree().change_scene_to_file(ending_scene)

func update_stats_ui():
    reputation_bar.value = player_stats["reputation"]
    lust_bar.value = player_stats["lust"]
    risk_bar.value = player_stats["risk"]

func save_game():
    var save_data = {
        "stats": player_stats,
        "flags": flags,
        "day": 1
    }
    var file = FileAccess.open("user://day1_save.json", FileAccess.WRITE)
    file.store_string(JSON.stringify(save_data))
    file.close()

func load_game():
    var file = FileAccess.open("user://day1_save.json", FileAccess.READ)
    if not file:
        return
    var text = file.get_as_text()
    file.close()
    var json = JSON.new()
    if json.parse(text) == OK:
        var data = json.data
        player_stats = data.get("stats", player_stats)
        flags = data.get("flags", [])
        update_stats_ui()
