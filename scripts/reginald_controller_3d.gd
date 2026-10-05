extends CharacterBody3D

@export var speed := 4.5
var click_target := Vector3.ZERO
var has_click_target := false
var pending_interaction: Interactive3D
var input_locked := false

func set_destination(destination: Vector3, target: Interactive3D = null) -> void:
    click_target = destination
    pending_interaction = target
    has_click_target = true

func _physics_process(_delta: float) -> void:
    if input_locked:
        velocity = Vector3.ZERO
        move_and_slide()
        return
    var keyboard_direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    if keyboard_direction.length() > 0.1:
        has_click_target = false
        pending_interaction = null
        var move := Vector3(keyboard_direction.x, 0, keyboard_direction.y).normalized()
        velocity = move * speed
        look_at(global_position + Vector3(move.x, 0, move.z), Vector3.UP)
        move_and_slide()
        return
    if has_click_target:
        var flat_target := Vector3(click_target.x, global_position.y, click_target.z)
        var direction := global_position.direction_to(flat_target)
        var distance := global_position.distance_to(flat_target)
        if distance < 0.18:
            velocity = Vector3.ZERO
            has_click_target = false
        else:
            velocity = Vector3(direction.x, 0, direction.z) * speed
            look_at(global_position + Vector3(direction.x, 0, direction.z), Vector3.UP)
        move_and_slide()
    else:
        velocity = Vector3.ZERO
        move_and_slide()

func consume_pending_interaction() -> Interactive3D:
    if pending_interaction and not has_click_target:
        var result := pending_interaction
        pending_interaction = null
        return result
    return null
