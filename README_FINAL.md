# R-John - Political Drama Visual Novel

A text-based political drama where you play Senator John through seven critical days of power, relationships, and scandal.

## Game Structure

- Day 1: The Office
- Day 2: The Charity Gala
- Day 3: The Campaign Trail
- Day 4: Capitol Hill
- Day 5: The Fundraiser
- Day 6: The Scandal
- Day 7: Resolution

## Player Stats

- **Reputation** (0-100): Public image and political standing
- **Lust** (0-100): Relationship tension
- **Risk** (0-100): Scandal exposure

## Installation

Requires Python 3.7+ with no external dependencies.

```bash
python main.py
```

## Files and Paths

### Dialogue Trees
- `data/dialogues/chapter_1/` — Maria, Laura, Emma
- `data/dialogues/chapter_2/` — Jessica, Olivia, Victoria
- `data/dialogues/chapter_3/` — Isabella
- `data/dialogues/chapter_4/` — Natalie
- `data/dialogues/chapter_5/` — Ashley
- `data/dialogues/chapter_6/` — Maria, Laura, Emma
- `data/dialogues/chapter_7/` — All NPCs

### Game Code
- `main.py` — game entry point
- `dialogue_engine.py` — dialogue tree runtime
- `narrative_engine.py` — narrative runtime
- `test_consistency.py` — basic validation tests

### Content
- `narrative/` — chapter scripts
- `art_briefs/` — character and location art direction

## Testing

```bash
python test_consistency.py
```

## Endings

- Victory: High reputation, low risk
- Damaged but Surviving: Moderate reputation and risk
- Strategic Retreat: Low reputation, low risk
- Downfall: Low reputation, high risk