extends Node

var reputation: int = 50
var lust: int = 30
var risk: int = 30
var inventory: Array[String] = []
var flags: Array[String] = []
var completed_talks: Array[String] = []
var debate_prepared: bool = false
var current_location: String = "office"

func reset_day() -> void:
    reputation = 50
    lust = 30
    risk = 30
    inventory.clear()
    flags.clear()
    completed_talks.clear()
    debate_prepared = false
    current_location = "office"

func add_item(item_id: String) -> void:
    if not inventory.has(item_id):
        inventory.append(item_id)

func has_item(item_id: String) -> bool:
    return inventory.has(item_id)

func add_flag(flag_id: String) -> void:
    if flag_id != "" and not flags.has(flag_id):
        flags.append(flag_id)

func apply_effects(rep_delta: int = 0, lust_delta: int = 0, risk_delta: int = 0) -> void:
    reputation = clampi(reputation + rep_delta, 0, 100)
    lust = clampi(lust + lust_delta, 0, 100)
    risk = clampi(risk + risk_delta, 0, 100)

func can_leave_for_debate() -> bool:
    return has_item("briefing") and completed_talks.has("maria")

func save_day() -> void:
    var data := {
        "reputation": reputation,
        "lust": lust,
        "risk": risk,
        "inventory": inventory,
        "flags": flags,
        "completed_talks": completed_talks,
        "debate_prepared": debate_prepared,
        "current_location": current_location
    }
    var file := FileAccess.open("user://day1_save.json", FileAccess.WRITE)
    if file:
        file.store_string(JSON.stringify(data))

func load_day() -> bool:
    if not FileAccess.file_exists("user://day1_save.json"):
        return false
    var file := FileAccess.open("user://day1_save.json", FileAccess.READ)
    if file == null:
        return false
    var parser := JSON.new()
    if parser.parse(file.get_as_text()) != OK:
        return false
    var data: Dictionary = parser.data
    reputation = int(data.get("reputation", 50))
    lust = int(data.get("lust", 30))
    risk = int(data.get("risk", 30))
    inventory.assign(data.get("inventory", []))
    flags.assign(data.get("flags", []))
    completed_talks.assign(data.get("completed_talks", []))
    debate_prepared = bool(data.get("debate_prepared", false))
    current_location = str(data.get("current_location", "office"))
    return true
