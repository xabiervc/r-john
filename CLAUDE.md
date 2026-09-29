# R. John: Public Servant - Claude Context

## Project Overview

**R. John: Public Servant** is a narrative stealth adventure / dark comedy / political satire.

**Premise:** You play as R. John, a 52-year-old widower politician with a perfect public image (intellectual, feminist ally, grieving widower) but a degenerate private life obsessed with sexual conquest.

**Goal:** Maximize conquests without getting exposed (career destruction) or settling down (personal failure).

## Key Files

- `GDD_v3_lean.md` - Full game design document
- `config/` - Game configuration (narrative, chapters, consequences)
- `data/` - World data (NPCs, locations, story objects)
- `schemas/` - JSON schemas for validation
- `prompts/` - Prompts for Claude Opus 5.5

## Core Mechanics

### Triple Bar System
- **Reputation (0-100, visible):** Public image. Critical if <20.
- **Lust (0-100, visible):** Sexual frustration. Critical if <20 (reckless).
- **Exposure Risk (0-100, hidden):** Shown as "Pressure" (Low/Med/High/Crit). Scandal if >=81.

### Mask System
- **Public Mask:** +Rep, -Lust, -Risk. Cannot seduce.
- **Private Mask:** -Rep (if seen), +Lust, +Risk. Can seduce.
- Switch takes 2 seconds, cannot switch in front of witnesses.

### Mood System (5 states)
- **Relaxed:** Interest +10, Suspicion -10
- **Stressed:** Interest -20, Suspicion +15
- **Flirty:** Interest +30, Suspicion -20 (golden opportunity)
- **Angry:** Interest -40, Suspicion +30 (DO NOT approach)
- **Neutral:** No modifiers

### Seduction (5 Phases)
1. **Approach:** Check location, mood, risk
2. **Conversation:** Personality-based dialogue
3. **Escalation:** Gradual advances, watch for resistance
4. **Climax:** Roll success chance (5-95%)
5. **Aftermath:** Manage evidence, exit cleanly

**Success Formula:**
```
Base = (Interest/100)*50 + ((100-Suspicion)/100)*30 + (ApproachMatch?20:0)
Mood Modifier: Relaxed +10, Stressed -20, Flirty +30, Angry -40, Neutral 0
Final = min(95, max(5, Base + Mood Modifier))
```

### Win/Lose Conditions
- **LOSE A:** Exposure Risk >=100 OR Reputation <20 (exposed, career destroyed)
- **LOSE B:** Enter stable relationship (personal failure)
- **WIN:** 5+ conquests, Exposure <30, Reputation >70 (ultimate degenerate victory)

## NPCs (11 seduceable)

| Name | Age | Role | Personality | Risk | Difficulty |
|------|-----|------|-------------|------|------------|
| Emma | 24 | Intern | Naive | Low | 0.3 (easy) |
| Laura | 26 | Assistant | Naive | Med-High | 0.4 |
| Isabella | 27 | Hotel Staff | Venal | Low | 0.2 (easiest) |
| Rachel | 26 | Volunteer | Naive | Low | 0.3 |
| Ashley | 25 | Maria's Friend | Venal | Med-High | 0.5 |
| Jessica | 29 | TV Journalist | Ambitious | Medium | 0.6 |
| Olivia | 35 | Colleague | Idealistic | Medium | 0.7 |
| Victoria | 31 | Influencer | Ambitious | High | 0.7 |
| Natalie | 33 | Lobbyist | Cynical | High | 0.8 (hard) |
| Maria | 34 | Press Secretary | Ambitious | High | 0.8 (hard) |
| Sophie | 32 | Journalist | Cynical | Highest | 0.9 (hardest) |

## Structure

- **7 Chapters** (one per day)
- **Days 1, 2, 4, 6:** Story-critical (linear, mandatory events)
- **Days 3, 5, 7:** Sandbox (open-ended, player chooses pace)
- **Duration:** 6-7 hours first playthrough, 18-25 hours completionist
- **8 Endings:** From "Ultimate Degenerate Victory" to "#MeToo Headline"

## Tone & Content Warnings

**Tone:** Dark comedy, political satire, moral complexity
**Warnings:** Sexual content, mature themes, manipulation, deception
**Rating:** PEGI 18 / ESRB M

## How to Help

When I ask for help with R. John:

1. **Reference the GDD:** Check `GDD_v3_lean.md` for design details
2. **Use the schemas:** Validate JSON against `schemas/`
3. **Follow the prompts:** Use `prompts/` for structured generation
4. **Maintain consistency:** Keep character voices, tone, and mechanics consistent
5. **Think strategically:** Every choice has consequences (Reputation, Lust, Risk)

## Example Prompts

See `prompts/` directory for ready-to-use prompts for:
- Generating C# code (systems, mechanics)
- Creating dialogue trees (JSON)
- Designing NPC profiles
- Balancing formulas
- Writing test cases

## Key Design Principles

1. **Player agency:** Multiple paths to victory, meaningful choices
2. **Consequences:** Every action affects Rep/Lust/Risk
3. **Tension:** Risk vs reward, exposure always looming
4. **Satire:** Political hypocrisy, public vs private selves
5. **Replayability:** 8 endings, different conquests each run
