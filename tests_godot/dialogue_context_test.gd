extends RefCounted

# Manual/CI content contract for dialogue context rules.
# Run from a Godot test harness when one is configured.

const PUBLIC_CONTEXTS := ["public_debate", "press_conference", "committee_hearing", "campaign_event", "crisis_statement"]
const FORBIDDEN_PUBLIC_INTENTS := ["flirt_subtext", "flirt_explicit", "sexual_joke"]

static func public_option_is_valid(option: Dictionary) -> bool:
    return not str(option.get("intent", "professional")) in FORBIDDEN_PUBLIC_INTENTS

static func private_subtext_is_valid(option: Dictionary) -> bool:
    return str(option.get("intent", "")) == "flirt_subtext" and option.get("allowed_contexts", []).has("private")

static func validate_public_options(options: Array) -> bool:
    for option in options:
        if not public_option_is_valid(option):
            return false
    return true
