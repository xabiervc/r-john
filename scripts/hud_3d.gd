extends CanvasLayer

@onready var stats: Label = $Stats
@onready var inventory: Label = $Inventory
@onready var prompt: Label = $Prompt
var state: Node
var transient_message := ""

func _ready() -> void:
    state = get_node("/root/Day1State")

func set_message(message: String) -> void:
    transient_message = message

func refresh() -> void:
    stats.text = "REPUTATION %d   DESIRE %d   RISK %d" % [state.reputation, state.desire, state.risk]
    inventory.text = "INVENTORY: " + (", ".join(state.inventory) if not state.inventory.is_empty() else "empty")
    if transient_message != "":
        prompt.text = transient_message
