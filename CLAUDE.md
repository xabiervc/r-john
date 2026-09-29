# Claude Instructions - R. John: Public Servant

**Project:** R. John: Public Servant - Narrative Stealth Adventure  
**Version:** 1.0  
**Last Updated:** 2026-09-29

---

## Project Overview

R. John: Public Servant is a narrative stealth adventure where you play as a 52-year-old widower politician with a perfect public image and a degenerate private life. The goal: sleep with as many women as possible without getting caught, while maintaining your career and avoiding #MeToo scandals.

**Key Mechanics:**
- Triple Bar System: Reputation (public), Lust (private), Exposure Risk (hidden)
- Mask System: Switch between public persona and private degenerate
- Mood System: NPCs have dynamic moods (Relaxed, Stressed, Flirty, Angry, Neutral)
- Seduction System: 5-phase mini-game (Approach, Conversation, Escalation, Climax, Aftermath)
- Bribery & Cover-Up: Pay off witnesses, destroy evidence, blackmail investigators
- 7 Chapters: One per day, with days 3, 5, 7 as sandbox (more freedom)
- 8 Endings: From "Ultimate Degenerate Victory" to "#MeToo Headline"

---

## Repository Structure

```
/r-john
├── CLAUDE.md                    ← This file
├── GDD_v3_lean.md              ← Full Game Design Document
├── README.md                    ← Project overview
├── /data
│   ├── characters.json          ← All 13 NPCs with complete profiles
│   ├── locations.json           ← 12 locations (public/private)
│   ├── chapters.json            ← 7 chapters (days) with events
│   └── endings.json             ← 8 endings with conditions
├── /prompts
│   ├── README.md                ← How to use prompts
│   ├── phase_00_core_systems.md
│   ├── phase_01_day1_debate_prep.md
│   ├── phase_02_day2_gala.md
│   ├── phase_03_day3_congress_travel.md
│   ├── phase_04_day4_congress_keynote.md
│   ├── phase_05_day5_party.md
│   ├── phase_06_day6_crisis.md
│   ├── phase_07_day7_final.md
│   └── phase_08_endings.md
├── /schemas
│   ├── character.schema.json
│   ├── location.schema.json
│   ├── chapter.schema.json
│   └── dialogue.schema.json
└── /tests
    └── narrative_consistency.md
```

---

## How to Use This Repo

### For Pre-Implementation (Current Phase)

1. **Start with GDD_v3_lean.md** - Understand the full vision
2. **Review data files** - characters.json, locations.json, chapters.json, endings.json
3. **Follow prompts in order** - phase_00 → phase_08
4. **Validate against schemas** - Ensure all outputs match JSON schemas
5. **Test narrative consistency** - Run tests in /tests

### For Implementation (Future Phase)

1. **Reference GDD section 6** - Technical specifications
2. **Use Claude_Opus_Prompts.md** - Code generation prompts
3. **Implement systems in order:**
   - Core: GameManager, Reputation, Lust, Exposure Risk
   - Mechanics: Mask, Mood, Seduction, Bribery, Evidence
   - UI: HUD, Dialogue, Phone Menu
   - Content: Chapters, Endings

---

## Key Design Principles

### 1. Player Agency
- Multiple paths through each chapter
- Meaningful choices with real consequences
- 8 distinct endings encourage replayability

### 2. Tension & Risk
- Triple bar system creates constant trade-offs
- Hidden risk meter adds uncertainty
- Every conquest brings you closer to exposure

### 3. Satire & Tone
- Dark comedy, not preachy
- Political satire (The Boys effect)
- Self-aware degeneracy (Larry, but modern)

### 4. Narrative Consistency
- All NPCs have consistent personalities, moods, schedules
- Events in chapters align with character profiles
- Endings match player actions throughout the week

---

## Current Status

**Phase:** Pre-Implementation Complete  
**Completed:**
- ✅ GDD v3.0 (Lean)
- ✅ characters.json (13 NPCs)
- ✅ locations.json (12 locations)
- ✅ chapters.json (7 chapters)
- ✅ endings.json (8 endings)
- ✅ Prompts phase_00 to phase_08

**Next Steps:**
- [ ] Generate dialogue trees for all NPCs (phase_01-07)
- [ ] Create art briefs for characters and locations
- [ ] Write full narrative script for each chapter
- [ ] Implement in Unity/Godot (future phase)

---

## Claude Best Practices

### When Generating Content

1. **Always reference the GDD** - Start prompts with "Based on GDD section X.X..."
2. **Use data files as source of truth** - characters.json, locations.json, chapters.json
3. **Follow schemas strictly** - Validate output against /schemas
4. **Maintain consistency** - Cross-reference NPCs, locations, events
5. **Iterate** - Generate → Review → Refine → Regenerate

### Example Prompts

```
Based on GDD section 2.2 (Characters - Maria) and data/characters.json,
generate a complete dialogue tree for Maria in Chapter 1 (Debate Preparation).

Requirements:
- 5 public dialogue options with reputation effects
- 5 private thoughts (inner monologue) with lust effects
- Mood-based variations (Stressed morning vs Relaxed evening)
- Personality-based responses (Maria is Ambitious type)
- Branching paths based on player choices

Output: JSON matching schemas/dialogue.schema.json
```

```
Based on data/chapters.json (Day 2: Charity Gala) and data/locations.json,
generate a detailed narrative script for the gala sequence.

Requirements:
- Opening scene: R. John arrives at gala
- Mandatory event: TV interview with Jessica
- Optional events: Seduce Jessica, Olivia, or Victoria
- Crisis point: Paparazzi photos
- Closing scene: End of gala, reputation/risk update

Output: Markdown narrative script with dialogue, descriptions, and choices
```

---

## Contact

- **GitHub:** @xabiervc
- **Project:** r-john
- **GDD Reference:** GDD_v3_lean.md

---

*Last updated: September 29, 2026*