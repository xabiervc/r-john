extends Control

func _ready():
    $StartButton.pressed.connect(_on_start_pressed)
    $QuitButton.pressed.connect(_on_quit_pressed)

func _on_start_pressed():
    get_tree().change_scene_to_file("res://scenes/dialogue_scene.tscn")

func _on_quit_pressed():
    get_tree().quit()
