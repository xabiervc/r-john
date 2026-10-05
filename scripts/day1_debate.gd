extends Node2D

@onready var text_label: RichTextLabel = $CanvasLayer/DebatePanel/Text
@onready var choices: VBoxContainer = $CanvasLayer/DebatePanel/Choices
@onready var status_label: Label = $CanvasLayer/StatusLabel
var state: Node
var step := 0

func _ready() -> void:
    state = get_node("/root/Day1State")
    state.current_location = "debate"
    show_step()

func show_step() -> void:
    for child in choices.get_children():
        child.queue_free()
    match step:
        0:
            text_label.text = "MODERATOR: Senator John, your opponent says you abandoned women by missing the Health Subcommittee vote. How do you respond?"
            add_choice("I prioritized appropriations funding programs that directly support women.", 5, 0, -3, "funding_frame")
            add_choice("I stand by my principles. I will not apologize.", 3, 0, 8, "principle_frame")
            if state.has_item("opponent_record"):
                add_choice("Before he lectures me, let us discuss his record on education funding.", 6, 0, 5, "opponent_record")
        1:
            text_label.text = "RIVAL: That is a convenient excuse. Your record is full of absences when it matters."
            add_choice("The briefing shows exactly which programs my appropriations protected.", 5, 0, -2, "briefing_use")
            add_choice("This is political theater. Voters can judge for themselves.", 2, 0, 5, "deflect")
            if state.flags.has("maria_trust_established"):
                add_choice("Maria's research confirms the education package has a measurable impact on women.", 7, 0, -2, "maria_support")
        _:
            finish_debate()

func add_choice(label: String, rep: int, lust: int, risk: int, outcome: String) -> void:
    var button := Button.new()
    button.text = label
    button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
    button.pressed.connect(func():
        state.apply_effects(rep, lust, risk)
        status_label.text = "Outcome recorded: " + outcome
        step += 1
        show_step()
    )
    choices.add_child(button)

func finish_debate() -> void:
    state.save_day()
    get_tree().change_scene_to_file("res://scenes/day1_summary.tscn")
