# R-John: Godot Vertical Slice Demo

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
4. Start the demo from main menu

---

## 📖 Demo Content

**Chapter 1: The Press Secretary**
- Meet Maria (Press Secretary)
- Make choices that affect Reputation, Lust, and Risk
- Experience the visual novel gameplay
- See consequences of your decisions

**Duration:** 5-10 minutes
**Endings:** Multiple based on your choices

---

## 🎯 Features

- ✅ Full dialogue system with choices
- ✅ Stats tracking (Reputation, Lust, Risk)
- ✅ NPC relationship system
- ✅ Save/Load system (coming soon)
- ✅ Visual novel UI with portraits
- ✅ Multiple choice paths
- ✅ Consequence system

---

## 📁 Project Structure

```
r-john/
├── project.godot          # Godot project file
├── scenes/
│   ├── main_menu.tscn     # Main menu scene
│   └── dialogue_scene.tscn # Main dialogue scene
├── scripts/
│   ├── main_menu.gd       # Main menu logic
│   └── dialogue_manager.gd # Dialogue system
├── data/
│   └── dialogues/
│       └── chapter_1/
│           └── dialogue_maria_ch1.json # Maria's dialogue
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

1. **Add more dialogues** (Laura, Emma in Chapter 1)
2. **Add save/load system**
3. **Add character portraits** (placeholder art)
4. **Add backgrounds** (Senator's Office)
5. **Add music and SFX**
6. **Expand to Chapters 2-7**

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

**Goal:** Prove the core gameplay is engaging before full production.

---

## 📞 Development

**Branch:** `feat/godot-vertical-slice`
**Godot Version:** 4.2+
**Status:** Playable demo

---

**Ready for playtesting and feedback!**
