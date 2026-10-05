# Day 1 Playtest Checklist

Run this checklist after pulling `feat/godot-vertical-slice`.

## Office scene

1. Start `day1_office_3d.tscn`.
2. Walk to Emma and start conversation.
   - [ ] Options include a professional line and a subtext line.
   - [ ] Choosing subtext leads to a boundary node.
   - [ ] Choosing "You are right. Senator John, then." sets `emma_boundary_respected`.
   - [ ] Choosing "It helps communication. Relax." sets `emma_boundary_pressed`.
3. Repeat with Laura.
   - [ ] Subtext option appears only in private context.
   - [ ] Boundary can be respected or pressed.
4. Repeat with Maria.
   - [ ] Subtext and explicit options appear.
   - [ ] Boundary response is firm: "Focus on the briefing, Senator."
   - [ ] Repair option reduces risk and sets `maria_boundary_respected`.
   - [ ] Press option sets `maria_boundary_pressed`.

## Collectibles and exit

- [ ] Picking up briefing sets `briefing` item.
- [ ] Picking up archive sets `opponent_record`.
- [ ] Picking up donor card increases risk slightly.
- [ ] Door is locked until briefing and Maria talk are complete.
- [ ] After completing requirements, door transitions to debate.

## Debate scene

1. Enter `day1_debate_3d.tscn`.
2. Confirm dialogue options:
   - [ ] All options are policy, evidence, principle, or deflect.
   - [ ] No flirt or subtext options appear.
   - [ ] If `opponent_record` is collected, an evidence option appears.
   - [ ] If `maria_trust_established` flag exists, a Maria-backed evidence option appears.
3. Complete debate and reach summary.

## Summary scene

1. Open `day1_summary.tscn`.
2. Check text:
   - [ ] If any `*_boundary_pressed` flags exist, summary mentions staff discomfort.
   - [ ] If all boundaries were respected, summary mentions professionalism.
   - [ ] Risk changes match choices made.

## Regression checks

- [ ] No console errors about forbidden intents in public debate.
- [ ] No crash when finishing conversations.
- [ ] State persists correctly between scenes.
