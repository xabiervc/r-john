# R-John: Public Servant - Godot Day 1 Vertical Slice

**Political Drama Visual Novel - Playable Demo**

---

## 🎮 Quick Start

### Requirements
- Godot 4.2+ (https://godotengine.org/download)
- No additional dependencies needed

### Run the Demo

1. Open Godot Engine
2. Import the project (`project.godot`)
3. Press F5 or click Play
4. Start Day 1 from main menu

---

## 📖 Demo Content

**Day 1: The Office**
- Meet Emma (Intern), Laura (Personal Assistant), Maria (Press Secretary)
- Make choices that affect Reputation, Lust, and Risk
- Experience the visual novel gameplay
- See consequences of your decisions
- Save your progress at the end of Day 1

**Duration:** 10-15 minutes
**Endings:** Day 1 summary with stats and flags

---

## 🎯 Features

- ✅ Full dialogue system with choices (Emma, Laura, Maria)
- ✅ Stats tracking (Reputation, Lust, Risk)
- ✅ NPC relationship flags
- ✅ Save/Load system (Day 1)
- ✅ Visual novel UI with portraits and background
- ✅ Multiple choice paths with consequences
- ✅ Day 1 summary screen

---

## 📁 Project Structure

```
r-john/
├── project.godot          # Godot project file
├── scenes/
│   ├── main_menu.tscn     # Main menu scene
│   ├── dialogue_scene.tscn # Main dialogue scene (Day 1)
│   └── day1_summary.tscn  # Day 1 summary scene
├── scripts/
│   ├── main_menu.gd       # Main menu logic
│   ├── dialogue_manager.gd # Dialogue system
│   └── day1_summary.gd    # Summary screen logic
├── data/
│   └── dialogues/
│       └── chapter_1/
│           ├── dialogue_day1.json         # Day 1 flow (Emma → Laura → Maria)
│           ├── dialogue_emma_ch1_premium.json
│           ├── dialogue_laura_ch1_premium.json
│           └── dialogue_maria_ch1_premium.json
├── art/
│   └── placeholders/
│       ├── README.md
│       └── (placeholder images)
└── icon.svg               # Game icon
```

---

## 🎨 Art Placeholders

Currently using placeholder sprites. For production:
- Character portraits (60 total needed)
- Backgrounds (7 locations)
- UI elements (buttons, bars, icons)

See `ART_BRIEF_COMPLETE.md` in main branch for full specifications.

---

## 🚀 Next Steps

1. ✅ Day 1 complete (Emma, Laura, Maria)
2. ⏳ Add character portraits (placeholder art)
3. ⏳ Add background (Senator's Office)
4. ⏳ Add music and SFX
5. ⏳ Expand to Days 2-7 (Chapters 2-7)
6. ⏳ Full save/load system
7. ⏳ Accessibility features (text scaling, high contrast)

---

## 📝 Controls

- **Mouse:** Click choices, navigate UI
- **Keyboard:** Enter/Space to continue, Arrow keys to navigate
- **Gamepad:** A button to select, D-pad/Stick to navigate

---

## 🏆 Target Quality

This vertical slice demonstrates:
- Core dialogue gameplay loop
- Choice and consequence system
- Stats tracking and visualization
- Visual novel presentation
- Save/Load functionality

**Goal:** Prove the core gameplay is engaging before full production.

---

## 📞 Development

**Branch:** `feat/godot-vertical-slice`
**Godot Version:** 4.2+
**Status:** Playable Day 1 demo

---

**Ready for playtesting and feedback!**
