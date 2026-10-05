extends Node

@export var camera_path: NodePath
@export var player_path: NodePath
@export var office_path: NodePath
@onready var camera: Camera3D = get_node(camera_path)
@onready var player: CharacterBody3D = get_node(player_path)
@onready var office: Node = get_node(office_path)

func _unhandled_input(event: InputEvent) -> void:
    if not (event is InputEventMouseButton and event.pressed):
        return
    var hit := _mouse_hit(event.position)
    if hit.is_empty():
        return
    var collider := hit.get("collider")
    if event.button_index == MOUSE_BUTTON_RIGHT:
        office.examine_target(collider)
        return
    if event.button_index == MOUSE_BUTTON_LEFT:
        if collider is Interactive3D:
            player.set_destination(collider.interaction_point(), collider)
        else:
            player.set_destination(hit.get("position"))

func _mouse_hit(screen_position: Vector2) -> Dictionary:
    var origin := camera.project_ray_origin(screen_position)
    var end := origin + camera.project_ray_normal(screen_position) * 2000.0
    var query := PhysicsRayQueryParameters3D.create(origin, end)
    return camera.get_world_3d().direct_space_state.intersect_ray(query)
