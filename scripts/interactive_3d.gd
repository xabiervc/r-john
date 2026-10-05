class_name Interactive3D
extends StaticBody3D

@export var interaction_id := ""
@export var display_name := ""
@export var interaction_point_offset := Vector3(0, 0, 1.2)

func interaction_point() -> Vector3:
    return global_position + global_transform.basis * interaction_point_offset

func examine() -> String:
    return "You examine " + display_name + "."
