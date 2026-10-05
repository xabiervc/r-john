extends Node3D

const PUBLIC_CONTEXT := "public_debate"
const FORBIDDEN_INTENTS := ["flirt_subtext", "flirt_explicit", "sexual_joke"]

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
        add_choice({"text":"I prioritized appropriations that directly fund programs for women.","intent":"policy_defense","reputation":5,"risk":-3,"outcome":"funding"})
        add_choice({"text":"I will not apologize for voting on principle.","intent":"principle","reputation":3,"risk":8,"outcome":"principle"})
        if state.has_item("opponent_record"):
            add_choice({"text":"Before he lectures me, let us examine Hawthorne's education funding record.","intent":"evidence","reputation":6,"risk":5,"outcome":"record"})
    elif step == 1:
        text_label.text = "HAWTHORNE: That is a convenient excuse. Your record is full of absences when it matters."
        add_choice({"text":"The briefing identifies programs my appropriations protected.","intent":"evidence","reputation":5,"risk":-2,"outcome":"briefing"})
        add_choice({"text":"Voters can judge both of our records for themselves.","intent":"deflect","reputation":2,"risk":5,"outcome":"deflect"})
        if state.flags.has("maria_trust_established"):
            add_choice({"text":"Maria's research confirms the education package's impact on women.","intent":"evidence","reputation":7,"risk":-2,"outcome":"maria"})
    else:
        state.save_day()
        get_tree().change_scene_to_file("res://scenes/day1_summary.tscn")

func add_choice(choice: Dictionary) -> void:
    if str(choice.get("intent", "")) in FORBIDDEN_INTENTS:
        push_error("Forbidden flirt intent in public debate: " + str(choice.get("intent")))
        return
    var button := Button.new()
    button.text = str(choice.get("text", ""))
    button.autowray_mode = TextServer.AUTOWRAP_WORD_SMART
    button.pressed.connect(func():
        state.apply_effects(int(choice.get("reputation", 0)), 0, int(choice.get("risk", 0)))
        status.text = "Outcome: " + str(choice.get("outcome", ""))
        step += 1
        show_step()
    )
    choices.add_child(button)
