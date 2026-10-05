# Dialogue Context Rules

## Canonical Rule

R. John uses double entendre only as part of optional flirtation in private or semi-private situations. Public political scenes must never present flirtatious or sexually suggestive choices.

## Contexts

### Private and semi-private

Allowed intents:
- `professional`
- `warm`
- `flirt_subtext`
- `flirt_explicit`
- `repair`

Examples:
- Closed office conversation
- Quiet side room at a fundraiser
- Private phone call
- Low-traffic corridor

### Public

Allowed intents:
- `policy_defense`
- `policy_attack`
- `evidence`
- `principle`
- `deflect`
- `damage_control`

Forbidden intents:
- `flirt_subtext`
- `flirt_explicit`
- `sexual_joke`

Public contexts include:
- `public_debate`
- `press_conference`
- `committee_hearing`
- `campaign_event`
- `crisis_statement`

## Boundary Rule

A boundary response from an NPC creates one of these results:
- Player repairs: lower risk and stronger professional trust.
- Player redirects neutrally: conversation continues without escalation.
- Player presses/dismisses: risk increases and a persistent discomfort flag is set.

## Requirements

An option may declare:

```json
{
  "intent": "flirt_subtext",
  "allowed_contexts": ["private", "semi_private"],
  "requirements": {"trust_min": 10},
  "effects": {"desire": 5, "risk": 3}
}
```

The dialogue adapter must hide options that fail context, flag, or relationship requirements. It must never substitute them into a public scene.

## Debate Rule

Debate dialogue communicates policy, reputation, evidence, political calculation, and control of public image. It contains no flirtation or double entendre.
