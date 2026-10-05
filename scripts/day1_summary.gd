extends Control

@onready var rep_label: Label = $StatsContainer/ReputationLabel
@onready var lust_label: Label = $StatsContainer/LustLabel
@onready var risk_label: Label = $StatsContainer/RiskLabel
@onready var flags_label: Label = $StatsContainer/FlagsLabel
@onready var continue_button: Button = $ContinueButton

var save_path = "user://day1_save.json"

func _ready():
    continue_button.pressed.connect(_on_continue_pressed)
    load_and_show()

func load_and_show():
    var file = FileAccess.open(save_path, FileAccess.READ)
    if not file:
        rep_label.text = "Reputation: (no save)"
        lust_label.text = "Lust: (no save)"
        risk_label.text = "Risk: (no save)"
        flags_label.text = "Flags: (no save)"
        return
    var text = file.get_as_text()
    file.close()
    var json = JSON.new()
    if json.parse(text) == OK:
        var data = json.data
        var stats = data.get("stats", {})
        rep_label.text = "Reputation: " + str(stats.get("reputation", 0))
        lust_label.text = "Lust: " + str(stats.get("lust", 0))
        risk_label.text = "Risk: " + str(stats.get("risk", 0))
        var flags_arr = data.get("flags", [])
        flags_label.text = "Flags: " + str(flags_arr.size()) + " set"
    else:
        rep_label.text = "Reputation: (corrupt save)"
        lust_label.text = "Lust: (corrupt save)"
        risk_label.text = "Risk: (corrupt save)"
        flags_label.text = "Flags: (corrupt save)"

func _on_continue_pressed():
    # Placeholder: Day 2 not implemented yet
    pass
