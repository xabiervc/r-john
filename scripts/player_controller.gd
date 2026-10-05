extends CharacterBody2D

@export var speed: float = 260.0
var input_locked: bool = false

func _physics_process(_delta: float) -> void:
    if input_locked:
        velocity = Vector2.ZERO
        move_and_slide()
        return
    var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * speed
    move_and_slide()
