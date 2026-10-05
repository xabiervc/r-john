extends Control

@onready var rep_label: Label = $StatsContainer/ReputationLabel
@onready var lust_label: Label = $StatsContainer/LustLabel
@onready var risk_label: Label = $StatsContainer/RiskLabel
@onready var flags_label: Label = $StatsContainer/FlagsLabel
@onready var inventory_label: Label = $StatsContainer/InventoryLabel
@onready var continue_button: Button = $ContinueButton
@onready var restart_button: Button = $RestartButton
var state: Node

func _ready() -> void:
    state = get_node("/root/Day1State")
    rep_label.text = "Reputation: %d" % state.reputation
    lust_label.text = "Desire: %d" % state.lust
    risk_label.text = "Risk: %d" % state.risk
    flags_label.text = "Choices recorded: %d" % state.flags.size()
    inventory_label.text = "Evidence/items: " + (", ".join(state.inventory) if not state.inventory.is_empty() else "none")
    continue_button.pressed.connect(func(): pass)
    restart_button.pressed.connect(func():
        state.reset_day()
        get_tree().change_scene_to_file("res://scenes/day1_office.tscn")
    )
