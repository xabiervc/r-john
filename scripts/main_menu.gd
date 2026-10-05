extends Control

func _ready() -> void:
    $StartButton.pressed.connect(_on_start_pressed)
    $LoadButton.pressed.connect(_on_load_pressed)
    $QuitButton.pressed.connect(_on_quit_pressed)

func _on_start_pressed() -> void:
    get_node("/root/Day1State").reset_day()
    get_tree().change_scene_to_file("res://scenes/day1_office.tscn")

func _on_load_pressed() -> void:
    var state = get_node("/root/Day1State")
    if state.load_day():
        get_tree().change_scene_to_file("res://scenes/day1_office.tscn")

func _on_quit_pressed() -> void:
    get_tree().quit()
