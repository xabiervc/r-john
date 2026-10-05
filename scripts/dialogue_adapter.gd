extends Control

@onready var speaker_label: Label = $Panel/Speaker
@onready var text_label: RichTextLabel = $Panel/Text
@onready var choices: VBoxContainer = $Panel/Choices

var active_nodes: Dictionary = {}
var on_finished: Callable
var state: Node

func _ready() -> void:
    visible = false

func start_conversation(speaker: String, nodes: Array, day_state: Node, finished_callback: Callable) -> void:
    state = day_state
    on_finished = finished_callback
    active_nodes.clear()
    for node in nodes:
        active_nodes[node.get("id", "")] = node
    visible = true
    show_node("start", speaker)

func show_node(node_id: String, speaker: String) -> void:
    if node_id == "" or not active_nodes.has(node_id):
        finish()
        return
    var node: Dictionary = active_nodes[node_id]
    speaker_label.text = speaker
    text_label.text = str(node.get("text", ""))
    for child in choices.get_children():
        child.queue_free()
    for option in node.get("publicOptions", []):
        var button := Button.new()
        button.text = str(option.get("text", "Continue"))
        button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
        button.pressed.connect(_choose.bind(option, speaker))
        choices.add_child(button)

func _choose(option: Dictionary, speaker: String) -> void:
    state.apply_effects(int(option.get("reputationEffect", 0)), int(option.get("lustEffect", 0)), int(option.get("riskEffect", 0)))
    state.add_flag(str(option.get("flagSet", "")))
    show_node(str(option.get("nextNode", "")), speaker)

func finish() -> void:
    visible = false
    if on_finished.is_valid():
        on_finished.call()
