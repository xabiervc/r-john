extends CanvasLayer

@onready var title: Label = $Panel/Title
@onready var body: RichTextLabel = $Panel/Body
@onready var next: Button = $Panel/Next
var state: Node

func _ready() -> void:
    state = get_node("/root/Day1State")
    title.text = "Day 1 Summary"
    var lines := []
    lines.append("You survived your first day as Senator Reginald John.")
    lines.append("")
    var boundary_flags := [
        "emma_boundary_pressed",
        "laura_boundary_pressed",
        "maria_boundary_pressed"
    ]
    var pressed_count := 0
    for flag in boundary_flags:
        if state.flags.has(flag):
            pressed_count += 1
    if pressed_count > 0:
        lines.append("Your tone with staff leaned personal. Some boundaries were tested.")
        lines.append("This may make future cooperation harder and increases the risk of leaks.")
        state.apply_effects(0, 0, pressed_count * 3)
    else:
        lines.append("You kept interactions professional. Staff trust remains intact.")
    lines.append("")
    if state.reputation >= 60:
        lines.append("Your public image is strong after the debate.")
    elif state.reputation >= 40:
        lines.append("Your public image is stable but could be sharper.")
    else:
        lines.append("Your public image is fragile. The next days will matter.")
    body.text = "\n".join(lines)
    next.pressed.connect(_on_next_pressed)

func _on_next_pressed() -> void:
    state.save_day()
    get_tree().change_scene_to_file("res://scenes/day2_hub.tscn")
