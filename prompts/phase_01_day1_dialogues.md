# Phase 01: Day 1 Dialogue Trees

**Chapter:** Day 1 - Debate Preparation  
**NPCs:** Maria, Laura, Emma  
**Location:** Government Building, Party HQ  
**Duration:** 45 minutes

---

## Context

R. John is preparing for the televised debate on gender equality. Maria is coordinating his schedule and press strategy. Laura is organizing logistics. Emma is the young intern helping with research.

**Key Events:**
- Morning: Debate prep meeting with Maria, Laura, Emma
- Afternoon: Press conference with Sophie, Jessica
- Evening: Optional seduction opportunities with Emma or Laura

---

## Task

Generate complete dialogue trees for **Maria**, **Laura**, and **Emma** for Chapter 1 (Day 1).

---

## Requirements

### For Each NPC:

1. **5 Public Dialogue Options** with reputation effects:
   - Professional/Polite: +5 reputation
   - Widowhood mention ("Margaret would approve..."): +8 reputation
   - Dismissive: -3 reputation
   - Charming: +4 reputation
   - Strategic (ask about press/debate): +6 reputation

2. **5 Private Thoughts (Inner Monologue)** with lust effects:
   - Degenerate thought ("She's hot when she's serious"): +8 lust, +5 risk
   - Strategic thought ("She knows too much, need to keep her close"): +3 lust, -5 risk
   - Lonely widower thought ("I need companionship"): +5 lust, +3 risk
   - Calculating thought ("If I flatter her, she'll work harder"): +4 lust, +2 risk
   - Impatient thought ("Just get on with it"): -2 lust, +0 risk

3. **Mood-Based Variations:**
   - **Stressed (morning):** More direct, less patient dialogue
   - **Relaxed (evening):** More open, slightly flirty dialogue
   - **Neutral:** Standard dialogue

4. **Personality-Based Responses:**
   - **Maria (Ambitious):** Responds to career promises, flattery about work, power displays
   - **Laura (Naive):** Responds to attention, flattery, career promises
   - **Emma (Naive):** Responds to flattery, mentorship, encouragement

5. **Branching Paths:**
   - If player is charming + mentions widowhood: NPC becomes more sympathetic (unlock "personal" path)
   - If player is dismissive: NPC becomes suspicious (unlock "investigative" path)
   - If player is professional: Standard path continues

---

## Output Format

Generate **3 JSON files** matching the dialogue schema:

### 1. `dialogue_maria_day1.json`

```json
{
  "id": "dialogue_maria_day1",
  "npcId": "maria",
  "chapter": 1,
  "context": "Debate prep meeting, morning, Government Building",
  "nodes": [
    {
      "id": "start",
      "text": "Mr. John, we need to finalize your debate strategy. The journalists will be asking about your stance on women's issues.",
      "publicOptions": [
        {
          "id": "professional",
          "text": "Yes, Maria. Let's go over the key points.",
          "reputationEffect": 5,
          "lustEffect": 0,
          "riskEffect": 0,
          "nextNode": "key_points"
        },
        {
          "id": "widowhood",
          "text": "My late wife Margaret would have wanted me to fight for this. It's personal for me.",
          "reputationEffect": 8,
          "lustEffect": -5,
          "riskEffect": 0,
          "nextNode": "margaret_discussion"
        },
        {
          "id": "dismissive",
          "text": "I know what I'm doing, Maria. Just handle the press.",
          "reputationEffect": -3,
          "lustEffect": 0,
          "riskEffect": 5,
          "nextNode": "maria_suspicious"
        },
        {
          "id": "charming",
          "text": "You always keep me on track, Maria. I don't know what I'd do without you.",
          "reputationEffect": 4,
          "lustEffect": 3,
          "riskEffect": 0,
          "nextNode": "maria_flattered"
        },
        {
          "id": "strategic",
          "text": "What are the journalists expecting? What's the angle here?",
          "reputationEffect": 6,
          "lustEffect": 0,
          "riskEffect": 0,
          "nextNode": "press_strategy"
        }
      ],
      "privateThoughts": [
        {
          "id": "degenerate",
          "text": "She's hot when she's serious. That focused look... How do I pivot to asking her out?",
          "lustEffect": 8,
          "riskEffect": 5
        },
        {
          "id": "strategic",
          "text": "She knows too much. If she ever talks, I'm done. Need to keep her close.",
          "lustEffect": 3,
          "riskEffect": -5
        },
        {
          "id": "lonely",
          "text": "God, I'm lonely. Margaret's been gone three years. Maybe I need... companionship.",
          "lustEffect": 5,
          "riskEffect": 3
        },
        {
          "id": "calculating",
          "text": "If I flatter her enough, she'll work even harder. Worth the effort.",
          "lustEffect": 4,
          "riskEffect": 2
        },
        {
          "id": "impatient",
          "text": "Just get on with it. I have better things to do than debate prep.",
          "lustEffect": -2,
          "riskEffect": 0
        }
      ]
    },
    {
      "id": "key_points",
      "text": "Good. The key points are: equal pay, reproductive rights, and workplace harassment. You've been vocal on all three.",
      "moodVariations": {
        "Stressed": "Look, the key points: equal pay, reproductive rights, harassment. We're behind schedule.",
        "Relaxed": "Perfect. So, equal pay, reproductive rights, workplace harassment. You've been great on all three.",
        "Neutral": "Good. The key points are: equal pay, reproductive rights, and workplace harassment."
      },
      "publicOptions": [
        {
          "id": "agree",
          "text": "Those are the right issues. I'll emphasize them.",
          "reputationEffect": 5,
          "nextNode": "closing"
        },
        {
          "id": "expand",
          "text": "What about childcare policy? That affects working women too.",
          "reputationEffect": 7,
          "nextNode": "childcare_discussion"
        }
      ]
    }
  ]
}
```

### 2. `dialogue_laura_day1.json`

Similar structure, but Laura's dialogue is more naive, eager to please.

### 3. `dialogue_emma_day1.json`

Similar structure, but Emma's dialogue is very expressive, nervous around authority.

---

## Additional Instructions

1. **Cross-reference data files:**
   - Use `data/characters.json` for NPC personalities, moods, schedules
   - Use `data/locations.json` for location context
   - Use `data/chapters.json` for chapter events

2. **Maintain consistency:**
   - Maria is Ambitious type → responds to career talk
   - Laura is Naive type → responds to attention
   - Emma is Naive type → responds to flattery/mentorship

3. **Include mood triggers:**
   - Maria: Stressed in morning, Relaxed in evening
   - Laura: Stressed before deadlines, Flirty when praised
   - Emma: Nervous around authority, Flirty when given advice

4. **Add seduction flags:**
   - If player chooses certain dialogue paths, set flags for seduction opportunities
   - Example: `"setFlag": "maria_interest_+10"` or `"setFlag": "emma_seduction_available"`

5. **Validate against schema:**
   - Ensure output matches `schemas/dialogue.schema.json` (create if doesn't exist)

---

## Expected Output

Generate **3 complete JSON files**:
- `data/dialogues/dialogue_maria_day1.json`
- `data/dialogues/dialogue_laura_day1.json`
- `data/dialogues/dialogue_emma_day1.json`

Each file should have:
- 10+ dialogue nodes
- 5 public options per node (with reputation/lust/risk effects)
- 5 private thoughts per node (with lust/risk effects)
- Mood variations for each NPC
- Branching paths based on player choices
- Flags for seduction opportunities

---

*Generated for R. John: Public Servant - Pre-Implementation Phase 01*
