extends Panel

@onready var label: Label = $Label

func refresh(items: Array[String]) -> void:
    if items.is_empty():
        label.text = "Inventory: empty"
    else:
        label.text = "Inventory: " + ", ".join(items)
