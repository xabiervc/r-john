extends Node2D

@onready var player: CharacterBody2D = $ReginaldJohn
@onready var dialogue: Control = $CanvasLayer/DialogueAdapter
@onready var status_label: Label = $CanvasLayer/StatusLabel
@onready var stats_label: Label = $CanvasLayer/StatsLabel
@onready var inventory_ui: Panel = $CanvasLayer/Inventory

var state: Node
var conversations := {
    "emma": [
        {"id":"start","text":"Emma looks up from her corner desk, clutching a folder. \"Good morning, Senator John. I found voting data Maria asked for.\"","publicOptions":[
            {"text":"Good work. Show me the key point.","reputationEffect":5,"lustEffect":2,"nextNode":"research","flagSet":"emma_encouraged"},
            {"text":"Call me John. We are all friends here.","reputationEffect":-3,"lustEffect":8,"riskEffect":10,"nextNode":"boundary","flagSet":"emma_informal_invited"},
            {"text":"Leave it with Maria.","riskEffect":3,"nextNode":"end","flagSet":"emma_dismissed"}
        ]},
        {"id":"research","text":"\"Your education record helps women more than the Family Act would have, statistically speaking.\"","publicOptions":[
            {"text":"That is useful. Put it in the briefing.","reputationEffect":5,"nextNode":"end","flagSet":"emma_empowered"},
            {"text":"I will use that in the debate.","reputationEffect":2,"riskEffect":3,"nextNode":"end","flagSet":"emma_credit_taken"}
        ]},
        {"id":"boundary","text":"Emma shifts uneasily. \"I do not think that would be appropriate, Senator.\"","publicOptions":[
            {"text":"You are right. Senator John, then.","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"research","flagSet":"emma_boundary_respected"},
            {"text":"It helps communication. Relax.","lustEffect":4,"riskEffect":10,"nextNode":"research","flagSet":"emma_boundary_pressed"}
        ]},
        {"id":"end","text":"\"Thank you, Senator. I will get back to work.\"","publicOptions":[{"text":"Carry on.","nextNode":null}]}
    ],
    "laura": [
        {"id":"start","text":"Laura has your schedule arranged with military precision. \"Your ten o'clock is confirmed, Senator. Maria left the debate briefing on your desk.\"","publicOptions":[
            {"text":"You are a lifesaver, Laura.","reputationEffect":3,"lustEffect":4,"nextNode":"schedule","flagSet":"laura_warmth_reciprocated"},
            {"text":"Thank you. Let me see the schedule.","reputationEffect":3,"nextNode":"schedule","flagSet":"laura_professional_treated"},
            {"text":"You are so eager. It is refreshing.","reputationEffect":-3,"lustEffect":4,"riskEffect":8,"nextNode":"boundary","flagSet":"laura_patronized"}
        ]},
        {"id":"schedule","text":"\"Debate prep at eleven, lunch with the education committee at one. Do not forget the debate briefing.\"","publicOptions":[
            {"text":"Perfect. You always keep me organized.","reputationEffect":3,"nextNode":"end","flagSet":"laura_trusted"},
            {"text":"You are more than just my assistant.","reputationEffect":-3,"lustEffect":8,"riskEffect":10,"nextNode":"boundary","flagSet":"laura_flirtation_initiated"}
        ]},
        {"id":"boundary","text":"Laura lowers her voice. \"Senator, I think we should keep this professional.\"","publicOptions":[
            {"text":"Of course. You are right.","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"schedule","flagSet":"laura_boundary_respected"},
            {"text":"Relax. It was a compliment.","lustEffect":3,"riskEffect":8,"nextNode":"schedule","flagSet":"laura_boundary_dismissed"}
        ]},
        {"id":"end","text":"\"I will be at my desk if you need anything.\"","publicOptions":[{"text":"Thanks, Laura.","nextNode":null}]}
    ],
    "maria": [
        {"id":"start","text":"Maria stands beside the briefing packet. \"The rival will attack your Family Act vote. We need a clean answer before you leave for the debate.\"","publicOptions":[
            {"text":"Walk me through your strongest argument.","reputationEffect":5,"nextNode":"briefing","flagSet":"maria_professional_respect"},
            {"text":"You are always one step ahead, Maria.","reputationEffect":3,"lustEffect":5,"nextNode":"briefing","flagSet":"maria_warmth_acknowledged"},
            {"text":"You are far more than my press secretary.","reputationEffect":-3,"lustEffect":10,"riskEffect":10,"nextNode":"boundary","flagSet":"maria_flirtation_initiated"}
        ]},
        {"id":"boundary","text":"Maria does not smile. \"Focus on the briefing, Senator. The debate is tomorrow.\"","publicOptions":[
            {"text":"You are right. Professionalism first.","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"briefing","flagSet":"maria_boundary_respected"},
            {"text":"Just stating facts. Let us work.","reputationEffect":-3,"lustEffect":5,"riskEffect":5,"nextNode":"briefing","flagSet":"maria_boundary_pressed"}
        ]},
        {"id":"briefing","text":"\"Lead with education funding. It helps women directly, and it lets you answer the absence from the health vote without sounding evasive.\"","publicOptions":[
            {"text":"Good. Add that to the debate briefing.","reputationEffect":5,"riskEffect":-3,"nextNode":"end","flagSet":"maria_trust_established"},
            {"text":"No apology. I will defend the vote on principle.","reputationEffect":3,"riskEffect":8,"nextNode":"end","flagSet":"maria_principled_noted"}
        ]},
        {"id":"end","text":"Maria closes the folder. \"You have enough to face him. Do not waste it.\"","publicOptions":[{"text":"Let us go to the debate.","nextNode":null}]}
    ]
}

func _ready() -> void:
    state = get_node("/root/Day1State")
    state.current_location = "office"
    player.add_to_group("player")
    for node in get_tree().get_nodes_in_group("interactable"):
        if node.has_signal("interacted"):
            node.interacted.connect(_on_interacted)
    refresh_ui()

func _process(_delta: float) -> void:
    refresh_ui()

func _on_interacted(interaction_id: String) -> void:
    match interaction_id:
        "briefing":
            state.add_item("briefing")
            state.debate_prepared = true
            status_label.text = "Collected: Debate Briefing. Maria can now help you prepare."
        "archive":
            state.add_item("opponent_record")
            status_label.text = "Collected: Opponent Record. It may unlock a debate response."
        "phone":
            state.add_item("donor_card")
            state.apply_effects(0, 0, 3)
            status_label.text = "Collected: Donor Card. Useful, but carrying it creates risk."
        "emma", "laura", "maria":
            if state.completed_talks.has(interaction_id):
                status_label.text = "You have already spoken with " + interaction_id.capitalize() + "."
                return
            start_talk(interaction_id)
        "door":
            if state.can_leave_for_debate():
                state.save_day()
                get_tree().change_scene_to_file("res://scenes/day1_debate.tscn")
            else:
                status_label.text = "Before leaving, collect the briefing and speak with Maria."

func start_talk(npc_id: String) -> void:
    player.input_locked = true
    status_label.text = "Talking with " + npc_id.capitalize() + "."
    dialogue.start_conversation(npc_id.capitalize(), conversations[npc_id], state, func():
        state.completed_talks.append(npc_id)
        player.input_locked = false
        status_label.text = "Conversation complete: " + npc_id.capitalize() + "."
    )

func refresh_ui() -> void:
    stats_label.text = "REPUTATION %d   DESIRE %d   RISK %d" % [state.reputation, state.lust, state.risk]
    inventory_ui.refresh(state.inventory)
