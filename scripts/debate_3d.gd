extends Node3D

@onready var text_label: RichTextLabel = $HUD/DebatePanel/Text
@onready var choices: VBoxContainer = $HUD/DebatePanel/Choices
@onready var status: Label = $HUD/Status
var state: Node
var step := 0

func _ready() -> void:
    state = get_node("/root/Day1State")
    state.current_location = "debate"
    show_step()

func show_step() -> void:
    for child in choices.get_children():
        child.queue_free()
    if step == 0:
        text_label.text = "MODERATOR: Senator John, Hawthorne says you abandoned women by missing the Health Subcommittee vote. Your response?"
        add_choice("I prioritized appropriations that directly fund programs for women.", 5, -3, "funding")
        add_choice("I will not apologize for voting on principle.", 3, 8, "principle")
        if state.has_item("opponent_record"):
            add_choice("Before he lectures me, let us examine Hawthorne's education funding record.", 6, 5, "record")
    elif step == 1:
        text_label.text = "HAWTHORNE: That is a convenient excuse. Your record is full of absences when it matters."
        add_choice("The briefing identifies programs my appropriations protected.", 5, -2, "briefing")
        add_choice("Voters can judge both of our records for themselves.", 2, 5, "deflect")
        if state.flags.has("maria_trust_established"):
            add_choice("Maria's research confirms the education package's impact on women.", 7, -2, "maria")
    else:
        state.save_day()
        get_tree().change_scene_to_file("res://scenes/day1_summary.tscn")

func add_choice(label: String, rep: int, risk: int, outcome: String) -> void:
    var button := Button.new()
    button.text = label
    button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
    button.pressed.connect(func():
        state.apply_effects(rep, 0, risk)
        status.text = "Outcome: " + outcome
        step += 1
        show_step()
    )
    choices.add_child(button)
