extends Node3D

@onready var player: CharacterBody3D = $ReginaldJohn
@onready var hud: CanvasLayer = $HUD
@onready var dialogue: CanvasLayer = $DialoguePortrait
var state: Node
var conversation_data := {
    "emma": [
        {"id":"start","text":"Emma stands beside her desk with a folder held close. \"Good morning, Senator John. I found voting data Maria asked for.\"","publicOptions":[
            {"text":"Good work. Show me the key point.","intent":"professional","reputationEffect":5,"lustEffect":2,"nextNode":"research","flagSet":"emma_encouraged"},
            {"text":"Call me John. We are all friends here.","intent":"flirt_subtext","allowed_contexts":["private","semi_private"],"reputationEffect":-3,"lustEffect":8,"riskEffect":10,"nextNode":"boundary","flagSet":"emma_informal_invited"},
            {"text":"Leave it with Maria.","intent":"professional","riskEffect":3,"nextNode":"end","flagSet":"emma_dismissed"}
        ]},
        {"id":"research","text":"\"Your education record helps women more than the Family Act would have, statistically speaking.\"","publicOptions":[
            {"text":"That is useful. Put it in the briefing.","intent":"professional","reputationEffect":5,"nextNode":"end","flagSet":"emma_empowered"},
            {"text":"I will use that in the debate.","intent":"professional","reputationEffect":2,"riskEffect":3,"nextNode":"end","flagSet":"emma_credit_taken"}
        ]},
        {"id":"boundary","text":"Emma looks uncomfortable. \"I do not think that would be appropriate, Senator.\"","publicOptions":[
            {"text":"You are right. Senator John, then.","intent":"repair","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"research","flagSet":"emma_boundary_respected"},
            {"text":"It helps communication. Relax.","intent":"flirt_explicit","allowed_contexts":["private"],"lustEffect":4,"riskEffect":10,"nextNode":"research","flagSet":"emma_boundary_pressed"}
        ]},
        {"id":"end","text":"\"Thank you, Senator. I will get back to work.\"","publicOptions":[{"text":"Carry on.","intent":"professional","nextNode":null}]}
    ],
    "laura": [
        {"id":"start","text":"Laura checks the schedule at her desk. \"Your ten o'clock is confirmed. Maria left the debate briefing on your desk.\"","publicOptions":[
            {"text":"You are a lifesaver, Laura.","intent":"warm","reputationEffect":3,"lustEffect":4,"nextNode":"schedule","flagSet":"laura_warmth_reciprocated"},
            {"text":"Thank you. Let me see the schedule.","intent":"professional","reputationEffect":3,"nextNode":"schedule","flagSet":"laura_professional_treated"},
            {"text":"You keep my day remarkably well arranged.","intent":"flirt_subtext","allowed_contexts":["private","semi_private"],"reputationEffect":-2,"lustEffect":5,"riskEffect":6,"nextNode":"boundary","flagSet":"laura_subtext_used"}
        ]},
        {"id":"schedule","text":"\"Debate prep at eleven, lunch at one. Do not forget the briefing.\"","publicOptions":[
            {"text":"Perfect. You always keep me organized.","intent":"professional","reputationEffect":3,"nextNode":"end","flagSet":"laura_trusted"},
            {"text":"You have a talent for keeping me exactly where I need to be.","intent":"flirt_subtext","allowed_contexts":["private","semi_private"],"reputationEffect":-3,"lustEffect":8,"riskEffect":10,"nextNode":"boundary","flagSet":"laura_flirtation_initiated"}
        ]},
        {"id":"boundary","text":"Laura lowers her voice. \"Senator, I think we should keep this professional.\"","publicOptions":[
            {"text":"Of course. You are right.","intent":"repair","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"schedule","flagSet":"laura_boundary_respected"},
            {"text":"Relax. It was a compliment.","intent":"flirt_explicit","allowed_contexts":["private"],"lustEffect":3,"riskEffect":8,"nextNode":"schedule","flagSet":"laura_boundary_dismissed"}
        ]},
        {"id":"end","text":"\"I will be at my desk if you need anything.\"","publicOptions":[{"text":"Thanks, Laura.","intent":"professional","nextNode":null}]}
    ],
    "maria": [
        {"id":"start","text":"Maria waits by the briefing packet. \"The rival will attack your Family Act vote. We need a clean answer before you leave.\"","publicOptions":[
            {"text":"Walk me through your strongest argument.","intent":"professional","reputationEffect":5,"nextNode":"briefing","flagSet":"maria_professional_respect"},
            {"text":"You always know exactly where to apply pressure.","intent":"flirt_subtext","allowed_contexts":["private","semi_private"],"reputationEffect":2,"lustEffect":5,"riskEffect":3,"nextNode":"briefing","flagSet":"maria_subtext_used"},
            {"text":"With you this close, I may forget this is a briefing.","intent":"flirt_explicit","allowed_contexts":["private"],"reputationEffect":-3,"lustEffect":10,"riskEffect":10,"nextNode":"boundary","flagSet":"maria_flirtation_initiated"}
        ]},
        {"id":"boundary","text":"Maria does not smile. \"Focus on the briefing, Senator.\"","publicOptions":[
            {"text":"You are right. Professionalism first.","intent":"repair","reputationEffect":5,"lustEffect":-5,"riskEffect":-5,"nextNode":"briefing","flagSet":"maria_boundary_respected"},
            {"text":"Just stating facts. Let us work.","intent":"flirt_explicit","allowed_contexts":["private"],"reputationEffect":-3,"lustEffect":5,"riskEffect":5,"nextNode":"briefing","flagSet":"maria_boundary_pressed"}
        ]},
        {"id":"briefing","text":"\"Lead with education funding. It helps women directly and answers the health-vote absence without sounding evasive.\"","publicOptions":[
            {"text":"Good. Add that to the debate briefing.","intent":"professional","reputationEffect":5,"riskEffect":-3,"nextNode":"end","flagSet":"maria_trust_established"},
            {"text":"No apology. I will defend the vote on principle.","intent":"principle","reputationEffect":3,"riskEffect":8,"nextNode":"end","flagSet":"maria_principled_noted"}
        ]},
        {"id":"end","text":"Maria closes the folder. \"You have enough to face him. Do not waste it.\"","publicOptions":[{"text":"Let us go to the debate.","intent":"professional","nextNode":null}]}
    ]
}

func _ready() -> void:
    state = get_node("/root/Day1State")
    state.current_location = "office"
    hud.set_message("Click the floor to walk. Click people or objects to interact. Right-click to examine.")
    hud.refresh()

func _process(_delta: float) -> void:
    hud.refresh()
    var pending := player.consume_pending_interaction()
    if pending:
        interact_with(pending)

func interact_with(target: Interactive3D) -> void:
    match target.interaction_id:
        "briefing":
            state.add_item("briefing")
            hud.set_message("Collected: Debate Briefing. Speak with Maria before leaving.")
        "archive":
            state.add_item("opponent_record")
            hud.set_message("Collected: Hawthorne's funding record. This may help during the debate.")
        "phone":
            state.add_item("donor_card")
            state.apply_effects(0, 0, 3)
            hud.set_message("Collected: Donor card. Keeping it creates a little risk.")
        "door":
            if state.can_leave_office():
                state.save_day()
                get_tree().change_scene_to_file("res://scenes/day1_debate_3d.tscn")
            else:
                hud.set_message("You need the briefing and Maria's debate preparation before leaving.")
        "emma", "laura", "maria":
            begin_conversation(target.interaction_id)

func begin_conversation(npc_id: String) -> void:
    if state.completed_talks.has(npc_id):
        hud.set_message("You have already spoken with " + npc_id.capitalize() + ".")
        return
    player.input_locked = true
    dialogue.begin(npc_id, conversation_data[npc_id], func():
        if not state.completed_talks.has(npc_id):
            state.completed_talks.append(npc_id)
        player.input_locked = false
        hud.set_message("Conversation complete: " + npc_id.capitalize() + ".")
    , "private")

func examine_target(target: Variant) -> void:
    if target is Interactive3D:
        var details := {"briefing":"A marked debate briefing. It looks important.","archive":"The archive contains a folder on Hawthorne's donors.","phone":"A secure campaign line. A donor card lies beside it.","door":"The exit to the debate hall.","emma":"Emma is new, alert and trying to impress.","laura":"Laura has organized your day down to the minute.","maria":"Maria has already anticipated the attack line."}
        hud.set_message(details.get(target.interaction_id, target.examine()))
