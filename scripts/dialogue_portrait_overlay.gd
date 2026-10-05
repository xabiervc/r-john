extends CanvasLayer

@onready var panel: Panel = $Panel
@onready var portrait: ColorRect = $Panel/Portrait
@onready var speaker: Label = $Panel/Speaker
@onready var expression: Label = $Panel/Expression
@onready var text_label: RichTextLabel = $Panel/Text
@onready var choices: VBoxContainer = $Panel/Choices
var state: Node
var nodes := {}
var npc_id := ""
var on_finished: Callable

const PORTRAIT_COLORS := {
    "emma": Color(0.76, 0.62, 0.75, 1),
    "laura": Color(0.72, 0.75, 0.49, 1),
    "maria": Color(0.55, 0.70, 0.86, 1)
}

func _ready() -> void:
    state = get_node("/root/Day1State")
    hide_dialogue()

func begin(npc: String, dialogue_nodes: Array, finished: Callable) -> void:
    npc_id = npc
    on_finished = finished
    nodes.clear()
    for node in dialogue_nodes:
        nodes[node.get("id", "")] = node
    portrait.color = PORTRAIT_COLORS.get(npc_id, Color.WHITE)
    panel.visible = true
    show_node("start")

func show_node(node_id: String) -> void:
    if node_id == "" or not nodes.has(node_id):
        hide_dialogue()
        if on_finished.is_valid():
            on_finished.call()
        return
    var node: Dictionary = nodes[node_id]
    speaker.text = npc_id.to_upper()
    expression.text = _expression_for(node_id)
    text_label.text = str(node.get("text", ""))
    for child in choices.get_children():
        child.queue_free()
    for option in node.get("publicOptions", []):
        var button := Button.new()
        button.text = str(option.get("text", "Continue"))
        button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
        button.pressed.connect(_select.bind(option))
        choices.add_child(button)

func _select(option: Dictionary) -> void:
    state.apply_effects(int(option.get("reputationEffect", 0)), int(option.get("lustEffect", 0)), int(option.get("riskEffect", 0)))
    state.add_flag(str(option.get("flagSet", "")))
    show_node(str(option.get("nextNode", "")))

func _expression_for(node_id: String) -> String:
    if "boundary" in node_id:
        return "Expression: guarded"
    if "briefing" in node_id or "research" in node_id:
        return "Expression: focused"
    return "Expression: neutral"

func hide_dialogue() -> void:
    panel.visible = false
