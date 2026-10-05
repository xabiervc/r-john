extends Control

func _ready():
    $StartButton.pressed.connect(_on_start_pressed)
    $LoadButton.pressed.connect(_on_load_pressed)
    $QuitButton.pressed.connect(_on_quit_pressed)

func _on_start_pressed():
    get_tree().change_scene_to_file("res://scenes/dialogue_scene.tscn")

func _on_load_pressed():
    # Switch to dialogue scene; it will load save if exists
    get_tree().change_scene_to_file("res://scenes/dialogue_scene.tscn")
    # DialogueManager will call load_game() in _ready()

func _on_quit_pressed():
    get_tree().quit()
