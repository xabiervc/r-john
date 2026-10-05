extends Area2D

@export var interaction_id: String = ""
@export var prompt_text: String = "Interact"
@export var one_shot: bool = false
var player_nearby: bool = false
var consumed: bool = false
signal interacted(interaction_id: String)

func _ready() -> void:
    body_entered.connect(_on_body_entered)
    body_exited.connect(_on_body_exited)

func _process(_delta: float) -> void:
    if player_nearby and not consumed and Input.is_action_just_pressed("ui_accept"):
        interacted.emit(interaction_id)
        if one_shot:
            consumed = true

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("player"):
        player_nearby = true

func _on_body_exited(body: Node2D) -> void:
    if body.is_in_group("player"):
        player_nearby = false
