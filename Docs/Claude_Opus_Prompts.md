# Claude Opus 5.5 Prompts - R. John: Public Servant

**Project:** R. John: Public Servant  
**GDD Reference:** `Docs/GDD_v3_lean.md`  
**Version:** 1.0  
**Date:** September 28, 2026

---

## How to Use These Prompts

1. **Always reference the GDD:** Start each prompt by mentioning the relevant GDD section
2. **Be specific:** Include exact method names, data structures, and requirements
3. **Iterate:** Generate → Review → Refine prompt → Regenerate
4. **Validate:** Always test Claude's output against GDD requirements

---

## Table of Contents

1. [Core Systems Code](#1-core-systems-code)
2. [Dialogue System](#2-dialogue-system)
3. [NPC & Seduction](#3-npc--seduction)
4. [Mood System](#4-mood-system)
5. [UI & HUD](#5-ui--hud)
6. [Save/Load System](#6-saveload-system)
7. [Mini-Games](#7-mini-games)
8. [Art & Visual Briefs](#8-art--visual-briefs)
9. [Balance & Tuning](#9-balance--tuning)
10. [Testing & QA](#10-testing--qa)

---

## 1. Core Systems Code

### 1.1 GameManager (Central Controller)

```
Based on GDD section 6.3 (Project Architecture) and 6.4 (Data Structures), 
generate a C# script for GameManager.cs with the following requirements:

CONTEXT:
- R. John: Public Servant is a narrative stealth adventure
- GameManager is the central controller that coordinates all systems
- Must support 7 chapters (one per day), 8 endings
- Must track Reputation (0-100), Lust (0-100), Exposure Risk (0-100, hidden)

REQUIREMENTS:
1. Singleton pattern (persistent across scenes)
2. Public properties:
   - int CurrentChapter (1-7)
   - float Reputation (0-100)
   - float Lust (0-100)
   - float ExposureRisk (0-100, internal only)
   - bool IsPublicMask (true if wearing public persona)
   - string CurrentLocation
   - float CurrentTimeSlot (0-5 for 6 time slots per day)

3. Methods:
   - void StartChapter(int chapterNumber)
   - void EndChapter(bool success)
   - void SwitchMask(bool toPublic)
   - void ChangeLocation(string locationName)
   - void AdvanceTimeSlot(int slots = 1)
   - void TriggerEnding(string endingId)
   - GameStatus GetGameStatus()

4. Events (using C# events or UnityEvent):
   - OnReputationChanged(float oldValue, float newValue)
   - OnLustChanged(float oldValue, float newValue)
   - OnExposureRiskChanged(float oldValue, float newValue)
   - OnMaskSwitched(bool isPublic)
   - OnLocationChanged(string oldLocation, string newLocation)
   - OnTimeSlotAdvanced(int oldSlot, int newSlot)
   - OnChapterStarted(int chapterNumber)
   - OnChapterEnded(bool success)
   - OnEndingTriggered(string endingId)

5. Integrate with:
   - SaveSystem (save/load game state)
   - EventBus (for decoupled communication with other systems)

6. Include XML documentation comments for all public methods

OUTPUT:
- Complete C# script with proper namespaces, class structure, and comments
- Follow Unity best practices (SerializeField for private fields exposed in inspector)
- Include example usage in comments
```

---

### 1.2 Reputation System

```
Based on GDD section 3.1 (Core System: The Triple Bar), generate C# script 
for ReputationSystem.cs with:

CONTEXT:
- Reputation bar (0-100) represents R. John's public image
- High reputation (70-100): media support, allies trust, easier to dismiss accusations
- Medium reputation (40-69): neutral, normal pressure
- Low reputation (0-39): suspicious media, allies distance
- Critical (<20): one scandal triggers career destruction

REQUIREMENTS:
1. Class: ReputationSystem (MonoBehaviour or ScriptableObject)

2. Public properties:
   - float CurrentReputation { get; } (0-100)
   - ReputationTier CurrentTier { get; } (enum: Critical, Low, Medium, High)

3. Methods:
   - void AddReputation(float amount, string reason = null)
   - void RemoveReputation(float amount, string reason = null)
   - void SetReputation(float value)
   - ReputationTier GetTier()
   - float GetTierThreshold(ReputationTier tier)
   - bool IsInTier(ReputationTier tier)

4. Reputation modifiers (apply multipliers):
   - Successful debate: +10-15
   - Charitable act: +5-10
   - Widowhood mention ("my late wife Margaret..."): +8
   - Failed seduction (witnessed): -10-20
   - Inappropriate behavior (witnessed): -15-30
   - Bribe discovered: -20-40

5. Events:
   - OnReputationChanged(float oldValue, float newValue, string reason)
   - OnTierChanged(ReputationTier oldTier, ReputationTier newTier)
   - OnCriticalReputation() (when <20, trigger warning)

6. Integrate with:
   - EventBus for broadcasting changes
   - SaveSystem for persistence
   - UIManager for updating HUD

OUTPUT:
- Complete C# script with enum definition for ReputationTier
- Include modifier table as ScriptableObject or config
- XML documentation for all public methods
```

---

### 1.3 Lust System

```
Based on GDD section 3.1 (Core System: The Triple Bar), generate C# script 
for LustSystem.cs with:

CONTEXT:
- Lust bar (0-100) represents R. John's sexual frustration/satisfaction
- High lust (70-100): satisfied, better decisions, but more confident/risky
- Medium lust (40-69): normal state, balanced
- Low lust (0-39): frustrated, impulsive, takes unnecessary risks
- Critical (<20): reckless, may attempt dangerous seductions

REQUIREMENTS:
1. Class: LustSystem (MonoBehaviour or ScriptableObject)

2. Public properties:
   - float CurrentLust { get; } (0-100)
   - LustTier CurrentTier { get; } (enum: Critical, Low, Medium, High)

3. Methods:
   - void AddLust(float amount, string reason = null)
   - void RemoveLust(float amount, string reason = null)
   - void SetLust(float value)
   - LustTier GetTier()
   - float GetDecisionsMakingModifier() (returns -0.3 to +0.3 based on lust level)
   - float GetRiskTakingModifier() (returns -0.2 to +0.4 based on lust level)

4. Lust modifiers:
   - Time passing (per hour): +2-5
   - Seeing attractive NPC: +5-10
   - Resisting urge: +10-15
   - Successful conquest: -40-60
   - Viewing private content (dating apps, photos): -10-20
   - Widowhood loneliness thought: +5-10

5. Events:
   - OnLustChanged(float oldValue, float newValue, string reason)
   - OnTierChanged(LustTier oldTier, LustTier newTier)
   - OnCriticalLust() (when <20, trigger reckless behavior warning)

6. Integrate with:
   - SeductionSystem (successful conquest reduces lust)
   - EventBus
   - SaveSystem

OUTPUT:
- Complete C# script with LustTier enum
- Include decision-making and risk-taking modifier formulas
- XML documentation
```

---

### 1.4 Exposure Risk System (Hidden)

```
Based on GDD section 3.1 (Core System: The Triple Bar), generate C# script 
for ExposureRiskSystem.cs with:

CONTEXT:
- Exposure Risk bar (0-100) is HIDDEN from player
- Shown only as vague "Pressure" indicators: Low/Medium/High/Critical
- Low (0-30): safe, minimal evidence
- Medium (31-60): some evidence, witnesses may talk
- High (61-80): strong evidence, journalist investigating
- Critical (81-100): exposure imminent, one mistake = scandal

REQUIREMENTS:
1. Class: ExposureRiskSystem (MonoBehaviour or ScriptableObject)

2. Public properties:
   - float CurrentRisk { get; internal set; } (0-100, internal to prevent UI access)
   - RiskLevel CurrentLevel { get; } (enum: Low, Medium, High, Critical)
   - string PressureIndicator { get; } (returns "Low", "Medium", "High", "Critical" for UI)

3. Methods:
   - void AddRisk(float amount, string reason = null)
   - void RemoveRisk(float amount, string reason = null)
   - void SetRisk(float value)
   - RiskLevel GetLevel()
   - string GetPressureIndicator() (for UI display only)
   - bool IsCritical() (returns true if >=81)
   - float GetScandalTriggerThreshold() (returns value at which scandal triggers)

4. Risk modifiers:
   - Each conquest completed: +20-40
   - Bribing someone: +10-30
   - Being seen in private moment: +30-50
   - Destroying evidence: -20-40
   - Silencing witness: -15-30
   - Successful cover-up: -20-40

5. Events:
   - OnRiskChanged(float oldValue, float newValue, string reason)
   - OnLevelChanged(RiskLevel oldLevel, RiskLevel newLevel)
   - OnCriticalRisk() (when >=81, trigger imminent scandal warning)
   - OnScandalTriggered() (when scandal actually happens)

6. Special:
   - DO NOT expose actual risk value to UI (only PressureIndicator)
   - Internal scandal trigger logic (auto-trigger if risk >=100 or specific event)

7. Integrate with:
   - EvidenceSystem (evidence adds/removes risk)
   - BriberySystem (bribes add risk)
   - SeductionSystem (conquests add risk)
   - EventBus
   - SaveSystem

OUTPUT:
- Complete C# script with RiskLevel enum
- Include scandal trigger logic
- XML documentation with WARNING comments about not exposing actual value
```

---

### 1.5 Mask System

```
Based on GDD section 3.2 (The Mask System), generate C# script 
for MaskSystem.cs with:

CONTEXT:
- R. John can toggle between Public Mask and Private Mask
- Public Mask: perfect politician, grieving widower (+Reputation, -Lust, -Risk)
- Private Mask: true degenerate self (-Reputation if seen, +Lust, +Risk)
- Cannot switch masks in front of witnesses
- Switching takes time (animation, location change)

REQUIREMENTS:
1. Class: MaskSystem (MonoBehaviour)

2. Public properties:
   - bool IsPublicMask { get; private set; }
   - MaskState CurrentState { get; } (enum: Public, Private, Transitioning)
   - float SwitchDuration { get; } (time in seconds to switch masks, default 2.0f)
   - bool CanSwitch { get; } (false if witnesses present or transitioning)

3. Methods:
   - void SwitchToPublic()
   - void SwitchToPrivate()
   - void ToggleMask()
   - bool TrySwitchMask() (returns false if can't switch, with reason)
   - void SetWitnessesPresent(bool present)
   - IEnumerator SwitchMaskCoroutine() (for animation/timing)

4. Mask effects (apply while active):
   Public Mask:
   - Reputation gain: +0.5 per minute
   - Lust loss: -1.0 per minute
   - Risk reduction: -0.3 per minute
   - Cannot access private locations
   - Cannot initiate seductions
   
   Private Mask:
   - Reputation loss if seen: -20-40
   - Lust gain: +1.0 per minute
   - Risk increase: +0.5 per minute
   - Can access private locations
   - Can initiate seductions

5. Events:
   - OnMaskSwitchStarted(MaskState from, MaskState to)
   - OnMaskSwitchCompleted(MaskState newState)
   - OnMaskSwitchBlocked(string reason)

6. Witness detection:
   - Track if NPCs are present (list of witness IDs)
   - Block switch if witnesses.Count > 0
   - Method: AddWitness(string npcId), RemoveWitness(string npcId)

7. Integrate with:
   - ReputationSystem, LustSystem, ExposureRiskSystem (apply modifiers)
   - LocationSystem (check if in public/private location)
   - EventBus
   - UIManager (update mask indicator)

OUTPUT:
- Complete C# script with MaskState enum
- Include coroutine for switch animation/timing
- Witness tracking system
- XML documentation
```

---

## 2. Dialogue System

### 2.1 Dialogue Manager

```
Based on GDD section 3.8 (Dialogue System) and 6.4 (Data Structures), 
generate C# script for DialogueManager.cs with:

CONTEXT:
- Branching dialogue trees with public dialogue and private thoughts
- Public dialogue affects Reputation
- Private thoughts (inner monologue) affect Lust, shown to player only
- Personality-based responses (Naive, Ambitious, Cynical, Idealistic, Venal)
- Mood-based variations (Relaxed, Stressed, Flirty, Angry, Neutral)

REQUIREMENTS:
1. Class: DialogueManager (MonoBehaviour)

2. Public properties:
   - bool IsInDialogue { get; }
   - string CurrentNPC { get; }
   - DialogueNode CurrentNode { get; }
   - bool ShowingPrivateThoughts { get; }

3. Methods:
   - void StartDialogue(string npcId, string dialogueTreeId)
   - void EndDialogue()
   - void SelectOption(int optionIndex)
   - void ShowPrivateThoughts(bool show)
   - DialogueOption[] GetAvailableOptions()
   - void ApplyChoiceEffects(DialogueChoice choice)

4. Dialogue data structure (JSON schema from GDD):
   {
     "id": "dialogue_maria_ch1",
     "npcId": "npc_maria",
     "chapter": 1,
     "nodes": [
       {
         "id": "start",
         "text": "Mr. John, we need to discuss your schedule...",
         "publicOptions": [
           {
             "text": "Yes, Maria. What's on the agenda?",
             "reputationEffect": 5,
             "lustEffect": 0,
             "nextNode": "schedule_discussion"
           }
         ],
         "privateThoughts": [
           {
             "text": "She's hot when she's serious. How do I pivot to asking her out?",
             "lustEffect": 8,
             "riskEffect": 5
           }
         ]
       }
     ]
   }

5. Events:
   - OnDialogueStarted(string npcId, string dialogueTreeId)
   - OnNodeDisplayed(DialogueNode node)
   - OnOptionSelected(int optionIndex, DialogueOption option)
   - OnPrivateThoughtsShown(PrivateThought[] thoughts)
   - OnDialogueEnded(string npcId)

6. Integrate with:
   - ReputationSystem, LustSystem, ExposureRiskSystem (apply effects)
   - MoodSystem (show mood-based variations)
   - PersonalitySystem (filter options based on NPC personality)
   - UIManager (display dialogue UI)
   - SaveSystem (save dialogue state)

OUTPUT:
- Complete C# script with DialogueNode, DialogueOption, PrivateThought classes
- JSON parsing logic (using Unity's JsonUtility or Newtonsoft)
- XML documentation
```

---

### 2.2 Dialogue Tree Generator (Claude-assisted)

```
Using GDD section 2.2 (Characters - Maria) and section 3.8 (Dialogue System), 
generate a complete dialogue JSON tree for Maria (Press Secretary) in Chapter 1.

REQUIREMENTS:
1. Dialogue context: Maria is discussing R. John's schedule for the upcoming debate
2. Include 5 public dialogue options with different reputation effects:
   - Professional/polite: +5 reputation
   - Widowhood mention ("Margaret would approve..."): +8 reputation
   - Dismissive: -3 reputation
   - Charming: +4 reputation
   - Strategic (ask about press): +6 reputation

3. Include 5 private thoughts (inner monologue) with different lust effects:
   - Degenerate thought ("She's hot when serious"): +8 lust, +5 risk
   - Strategic thought ("She knows too much, need to keep her close"): +3 lust, -5 risk
   - Lonely widower thought ("I need companionship"): +5 lust, +3 risk
   - Calculating thought ("If I flatter her, she'll work harder"): +4 lust, +2 risk
   - Impatient thought ("Just get on with it"): -2 lust, +0 risk

4. Include mood-based variations:
   - If Maria is Stressed (morning): She's more direct, less patient
   - If Maria is Relaxed (evening): She's more open, slightly flirty
   - If Maria is Neutral: Standard dialogue

5. Include personality-based responses (Maria is Ambitious type):
   - She responds better to career promises, flattery about her work, power displays
   - She responds worse to condescension, vagueness, dismissiveness

6. Branching paths:
   - If player is charming + mentions widowhood: Maria becomes more sympathetic (unlock "personal" path)
   - If player is dismissive: Maria becomes suspicious (unlock "investigative" path)
   - If player is professional: Standard path continues

7. Output format: Valid JSON matching GDD section 6.4 Dialogue schema

OUTPUT:
- Complete JSON file (dialogue_maria_ch1.json)
- Include all nodes, options, private thoughts, mood variations
- Include comments explaining branching logic
```

---

## 3. NPC & Seduction

### 3.1 NPC Profile System

```
Based on GDD section 2.2 (Main Characters) and 6.4 (Data Structures - NPC Profile), 
generate C# script for NPCProfile.cs with:

CONTEXT:
- Each NPC has a profile with personality, risk level, seduction profile, mood profile, schedule
- 10 main NPCs: R. John, Margaret (deceased), Maria, Laura, Carlos, Sophie, Emma, Jessica, Olivia, Isabella, Victoria, Rachel, Natalie, Ashley
- Profiles are loaded from JSON at runtime

REQUIREMENTS:
1. Class: NPCProfile (ScriptableObject or data class)

2. Properties:
   - string Id (e.g., "npc_maria")
   - string Name (e.g., "Maria")
   - string Role (e.g., "Press Secretary")
   - int Age
   - NPCPersonality Personality (enum: Naive, Ambitious, Cynical, Idealistic, Venal)
   - RiskProfile RiskProfile (enum: Low, Medium, High)
   - SeductionProfile SeductionProfile (nested class)
   - MoodProfile MoodProfile (nested class)
   - ScheduleEntry[] Schedule (array of daily schedules)
   - string DialogueTreeId (reference to dialogue JSON)

3. SeductionProfile class:
   - float BaseInterest (0-100)
   - float BaseSuspicion (0-100)
   - string[] PreferredApproaches (e.g., ["Career", "Flattery", "Power"])
   - float ConquestDifficulty (0-1, 1 = hardest)

4. MoodProfile class:
   - Mood DefaultMood
   - Mood MorningMood
   - Mood EveningMood
   - Dictionary<string, Mood> Triggers (key: trigger name, value: resulting mood)

5. ScheduleEntry class:
   - int Day (1-7)
   - string TimeSlot (Morning, Afternoon, Evening, Night)
   - string Location
   - string Activity

6. Methods:
   - Mood GetCurrentMood() (based on time of day and recent events)
   - bool IsAvailable(int day, string timeSlot)
   - string GetCurrentLocation(int day, string timeSlot)
   - float GetApproachMatchScore(string approach) (returns 0-1 based on preferred approaches)

7. Integrate with:
   - MoodSystem (get current mood)
   - SeductionSystem (provide profile data)
   - TimeSystem (check schedule)
   - JSON loader (load from GDD schema)

OUTPUT:
- Complete C# script with all nested classes and enums
- Example JSON loading code
- XML documentation
```

---

### 3.2 Seduction System (5 Phases)

```
Based on GDD section 3.4 (Seduction System - 5 Phases), generate C# script 
for SeductionSystem.cs with:

CONTEXT:
- Each conquest follows 5 phases: Approach, Conversation, Escalation, Climax, Aftermath
- Success chance based on Interest, Suspicion, Mood, Approach Match
- Each phase has risks and rewards
- Failed seduction can increase exposure risk

REQUIREMENTS:
1. Class: SeductionSystem (MonoBehaviour)

2. Public properties:
   - bool IsInSeduction { get; }
   - string CurrentTarget { get; }
   - SeductionPhase CurrentPhase { get; } (enum: Approach, Conversation, Escalation, Climax, Aftermath, None)
   - float CurrentSuccessChance { get; } (calculated 5-95%)

3. Methods:
   - bool TryStartSeduction(string npcId) (returns false if not available or already in seduction)
   - void AdvancePhase()
   - void SelectOption(int optionIndex) (for Conversation/Escalation phases)
   - float CalculateSuccessChance() (using formula from GDD)
   - void ResolveClimax() (roll dice, determine success/failure)
   - void CompleteSeduction(bool success)
   - void AbortSeduction()

4. Success chance formula (from GDD section 3.3):
   Base Success = (Interest / 100) * 50 + ((100 - Suspicion) / 100) * 30 + (ApproachMatch ? 20 : 0)
   
   Mood Modifier:
   - Relaxed: +10%
   - Stressed: -20%
   - Flirty: +30%
   - Angry: -40%
   - Neutral: 0%
   
   Final Success = min(95, max(5, Base Success + Mood Modifier))

5. Phase-specific logic:
   Approach:
   - Check location (private vs public)
   - Check NPC mood
   - Risk: +10-20 exposure if seen
   
   Conversation:
   - Dialogue tree with personality-based options
   - Build rapport (Interest +20-30)
   - Risk: Wrong choice = -Interest, +Suspicion, mood worsens
   
   Escalation:
   - Gradual advances (compliments, touch, invitations)
   - Watch for resistance (mood change) or encouragement
   - Interest +20-40, Suspicion +10-20
   
   Climax:
   - Final push (direct proposition)
   - Roll success chance
   - Success: Conquest completed, Lust -40-60, Exposure +20-40
   - Failure: Rejection, Exposure +10-30 (she may tell others)
   
   Aftermath:
   - Manage evidence (delete messages, ensure silence)
   - Exit cleanly
   - Risk: +20-30 exposure if seen leaving together

6. Events:
   - OnSeductionStarted(string npcId)
   - OnPhaseAdvanced(SeductionPhase oldPhase, SeductionPhase newPhase)
   - OnSuccessChanceCalculated(float chance)
   - OnClimaxResolved(bool success)
   - OnSeductionCompleted(string npcId, bool success)
   - OnSeductionAborted(string reason)

7. Integrate with:
   - NPCProfile (get target's profile)
   - MoodSystem (get current mood, apply modifier)
   - LustSystem (reduce lust on success)
   - ExposureRiskSystem (increase risk on success/failure)
   - EvidenceSystem (create evidence on success)
   - EventBus
   - UIManager (update seduction UI)

OUTPUT:
- Complete C# script with SeductionPhase enum
- Include all 5 phases with specific logic
- Success chance formula implementation
- XML documentation
```

---

## 4. Mood System

### 4.1 Mood System Core

```
Based on GDD section 3.3 (Mood System), generate C# script for MoodSystem.cs with:

CONTEXT:
- Each NPC has a current mood that dynamically affects seduction success
- 5 mood states: Relaxed, Stressed, Flirty, Angry, Neutral
- Moods change based on time of day, recent events, location, player actions
- Mood affects Interest and Suspicion modifiers

REQUIREMENTS:
1. Class: MoodSystem (MonoBehaviour)

2. Mood enum:
   public enum Mood { Relaxed, Stressed, Flirty, Angry, Neutral }

3. Mood modifiers (from GDD table):
   - Relaxed: Interest +10, Suspicion -10
   - Stressed: Interest -20, Suspicion +15
   - Flirty: Interest +30, Suspicion -20
   - Angry: Interest -40, Suspicion +30
   - Neutral: Interest 0, Suspicion 0

4. Public properties:
   - Dictionary<string, Mood> NPCMoods { get; } (npcId -> current mood)
   - Mood GetMood(string npcId)
   - float GetInterestModifier(Mood mood)
   - float GetSuspicionModifier(Mood mood)
   - float GetSeductionSuccessModifier(Mood mood)

5. Methods:
   - void SetMood(string npcId, Mood mood, string reason = null)
   - Mood GetMood(string npcId)
   - void UpdateMood(string npcId) (based on time, location, recent events)
   - void TriggerMoodChange(string npcId, string triggerName) (e.g., "playerHelped", "playerRejected")
   - Mood CalculateMoodFromTime(string timeOfDay)
   - Mood CalculateMoodFromLocation(string location)
   - void ApplyMoodModifierToSeduction(string npcId, ref float baseSuccessChance)

6. Mood triggers (from GDD table):
   - Time of Day: Morning -> Stressed, Afternoon -> Neutral, Evening -> Relaxed/Flirty
   - Recent Event (Good): -> Relaxed or Flirty
   - Recent Event (Bad): -> Stressed or Angry
   - Player Helped Earlier: -> Relaxed
   - Player Insulted/Rejected: -> Angry
   - Location: Office -> Stressed/Neutral, Bar/Party -> Relaxed/Flirty
   - Alcohol Consumed: -> Flirty
   - Compliment Received: -> Flirty

7. Events:
   - OnMoodChanged(string npcId, Mood oldMood, Mood newMood, string reason)
   - OnMoodUpdated(string npcId, Mood newMood)
   - OnMoodTriggered(string npcId, string triggerName, Mood resultingMood)

8. Integrate with:
   - NPCProfile (get mood profile, triggers)
   - TimeSystem (time of day affects mood)
   - LocationSystem (location affects mood)
   - SeductionSystem (apply mood modifier to success chance)
   - UIManager (show mood indicator emoji: 😊😤😏😠😐)
   - EventBus

OUTPUT:
- Complete C# script with Mood enum and all methods
- Include mood trigger dictionary and application logic
- Success modifier formula implementation
- XML documentation
```

---

## 5. UI & HUD

### 5.1 HUD Controller

```
Based on GDD section 3.1 (Triple Bar) and 4.4 (UI/UX Design), 
generate C# script for HUDController.cs with:

CONTEXT:
- HUD shows Reputation (visible), Lust (visible), Pressure (vague: Low/Med/High/Crit)
- Bottom bar shows time slot, location, mask indicator
- Corner phone icon for inventory/messages/apps/calendar

REQUIREMENTS:
1. Class: HUDController (MonoBehaviour)

2. HUD elements (Unity UI references):
   - Slider reputationSlider (0-100, color-coded: green=high, yellow=medium, red=low)
   - Slider lustSlider (0-100, color-coded: blue=high, yellow=medium, red=low)
   - Text pressureText (shows "Low", "Medium", "High", "Critical")
   - Text timeSlotText (shows "Morning", "Afternoon", "Evening", "Night")
   - Text locationText (shows current location name)
   - Image maskIndicator (shows Public/Private icon)
   - Button phoneButton (opens phone menu)

3. Methods:
   - void UpdateReputation(float value, float oldValue)
   - void UpdateLust(float value, float oldValue)
   - void UpdatePressure(string pressureLevel)
   - void UpdateTimeSlot(string timeSlot)
   - void UpdateLocation(string location)
   - void UpdateMask(bool isPublic)
   - void OpenPhoneMenu()
   - void ClosePhoneMenu()

4. Color coding (from GDD):
   Reputation:
   - High (70-100): Green
   - Medium (40-69): Yellow
   - Low (0-39): Red
   - Critical (<20): Flashing red
   
   Lust:
   - High (70-100): Blue
   - Medium (40-69): Yellow
   - Low (0-39): Red
   - Critical (<20): Flashing red

5. Pressure indicators (from GDD):
   - Low (0-30): "Low" (green text)
   - Medium (31-60): "Medium" (yellow text)
   - High (61-80): "High" (orange text)
   - Critical (81-100): "CRITICAL" (flashing red text)

6. Events (subscribe to):
   - ReputationSystem.OnReputationChanged
   - LustSystem.OnLustChanged
   - ExposureRiskSystem.OnLevelChanged
   - TimeSystem.OnTimeSlotAdvanced
   - LocationSystem.OnLocationChanged
   - MaskSystem.OnMaskSwitchCompleted

7. Integrate with:
   - All system scripts (listen to events)
   - PhoneMenuController (open/close phone)
   - UIManager (overall UI coordination)

OUTPUT:
- Complete C# script with all UI references and update methods
- Include color-coding logic
- Include event subscriptions
- XML documentation
```

---

## 6. Save/Load System

### 6.1 Save System Core

```
Based on GDD section 6.3 (Project Architecture) and general save game patterns, 
generate C# script for SaveSystem.cs with:

CONTEXT:
- Save game state including: Reputation, Lust, Exposure Risk, inventory, completed conquests, active investigations, NPC relationships, evidence locations, bribes paid, time slot, current chapter, mask state
- Auto-save at end of each day, before major decisions, after conquests
- Manual save: 10 save slots
- Cloud save: Steam Cloud, iCloud, Google Play Games

REQUIREMENTS:
1. Class: SaveSystem (MonoBehaviour, singleton)

2. Save data structure (serializable class):
   [System.Serializable]
   public class SaveData {
     public string SaveName;
     public DateTime SaveTime;
     public int CurrentChapter;
     public float Reputation;
     public float Lust;
     public float ExposureRisk;
     public bool IsPublicMask;
     public string CurrentLocation;
     public int CurrentTimeSlot;
     
     public List<ConquestSaveData> CompletedConquests;
     public List<EvidenceSaveData> ActiveEvidence;
     public List<NPCRelationshipSaveData> NPCRelationships;
     public List<BribeSaveData> PaidBribes;
     public List<string> Inventory;
     
     public Dictionary<string, float> NPCInterest;
     public Dictionary<string, float> NPCSuspicion;
     public Dictionary<string, Mood> NPCMoods;
   }

3. Methods:
   - void SaveGame(int slotIndex, string saveName = null)
   - void LoadGame(int slotIndex)
   - void DeleteSave(int slotIndex)
   - bool HasSave(int slotIndex)
   - SaveData GetSaveInfo(int slotIndex) (without loading full game)
   - void AutoSave(string reason)
   - string GetSavePath(int slotIndex)
   - IEnumerator SaveGameAsync(int slotIndex, SaveData data) (for async file I/O)

4. Auto-save triggers:
   - End of each chapter (day)
   - Before major decisions (debate, climax of seduction)
   - After conquest completion
   - Every 10 minutes (optional, configurable)

5. Manual save:
   - 10 save slots (indexed 0-9)
   - Player can name saves
   - Show save time, chapter, play time

6. Cloud save integration:
   - Steam Cloud (PC)
   - iCloud (iOS)
   - Google Play Games (Android)
   - Fallback: local file save

7. Versioning:
   - Include save format version in SaveData
   - Migration logic for old saves if format changes

8. Security:
   - Basic encryption or obfuscation (prevent easy cheating)
   - Checksum validation (detect corrupted saves)

9. Integrate with:
   - All system scripts (gather state for saving, restore state on load)
   - Platform-specific cloud save APIs
   - UIManager (save/load UI)

OUTPUT:
- Complete C# script with SaveData class and all save/load methods
- Include auto-save triggers and cloud save stubs
- Include basic encryption/checksum logic
- XML documentation
```

---

## 7. Mini-Games

### 7.1 Debate Mini-Game

```
Based on GDD section 3.10 (Mini-Games - Debate), generate C# script 
for DebateMiniGame.cs with:

CONTEXT:
- Quick-time dialogue choices during debates
- Choose correct policy positions under time pressure
- Success: +Reputation (+10-15), media praise
- Failure: -Reputation (-10-20), gaffes go viral
- Occurrences: Day 2 (TV interview), Day 7 (final debate)

REQUIREMENTS:
1. Class: DebateMiniGame (MonoBehaviour)

2. Debate structure:
   - 5-7 rounds per debate
   - Each round: Question appears, 3-4 answer options, 10-15 second timer
   - Correct answer: +Reputation, positive media reaction
   - Incorrect answer: -Reputation, negative media reaction
   - Time runs out: -Reputation (smaller penalty than wrong answer)

3. Public properties:
   - bool IsInDebate { get; }
   - int CurrentRound { get; }
   - int TotalRounds { get; }
   - float TimeRemaining { get; }
   - int CorrectAnswers { get; }
   - int DebateScore { get; }

4. Methods:
   - void StartDebate(string debateId)
   - void PresentQuestion(DebateQuestion question)
   - void SelectAnswer(int answerIndex)
   - void OnTimeRanOut()
   - void EndDebate()
   - DebateResult CalculateResult()

5. DebateQuestion class:
   - string QuestionText
   - string[] Answers
   - int CorrectAnswerIndex
   - string Topic (e.g., "Gender Equality", "Economy", "Healthcare")
   - float ReputationGain (for correct answer)
   - float ReputationLoss (for wrong answer)

6. Scoring:
   - Each correct answer: +2-3 reputation
   - Each wrong answer: -2-3 reputation
   - Time bonus: +0.5 reputation per second remaining (max +5)
   - Final result:
     * 5-7 correct: "Landslide Victory" (+15 reputation)
     * 3-4 correct: "Solid Performance" (+10 reputation)
     * 1-2 correct: "Poor Showing" (-10 reputation)
     * 0 correct: "Disaster" (-20 reputation)

7. Events:
   - OnDebateStarted(string debateId)
   - OnRoundStarted(int roundNumber, DebateQuestion question)
   - OnAnswerSelected(int answerIndex, bool isCorrect)
   - OnTimeRanOut(int roundNumber)
   - OnDebateEnded(DebateResult result)

8. Integrate with:
   - ReputationSystem (apply reputation changes)
   - UIManager (debate UI, timer, answer buttons)
   - AudioManager (play tense music, timer beep, correct/wrong sounds)

OUTPUT:
- Complete C# script with DebateQuestion and DebateResult classes
- Include timer logic and scoring system
- Include example debate questions (gender equality, economy, etc.)
- XML documentation
```

---

## 8. Art & Visual Briefs

### 8.1 Character Design Brief (R. John)

```
Using GDD section 4.2 (Character Design - R. John), create a detailed art brief 
for R. John's character model suitable for sending to a 3D artist.

CONTEXT:
- R. John is 52 years old, distinguished but still attractive
- Has two modes: Public (perfect politician, grieving widower) and Private (degenerate self)
- Eyes change subtly between modes (warm/public vs cold/private)
- Style: 2.5D (3D character on 2D backgrounds), similar to Disco Elysium / Wolf Among Us

REQUIREMENTS:
1. Character overview:
   - Name: R. John
   - Age: 52
   - Role: Senior politician
   - Personality (public): Charismatic, intellectual, sympathetic, grieving widower
   - Personality (private): Predatory, manipulative, selfish, degenerate

2. Physical appearance:
   - Height: 6'0" (183 cm)
   - Build: Fit but not muscular (politician who works out but not obsessed)
   - Hair: Silver/gray, distinguished, perfectly styled in public, slightly disheveled in private
   - Eyes: Blue or gray, warm and sad in public mode, cold and predatory in private mode
   - Skin: Light tan, well-maintained
   - Distinguishing features: None (intentionally generic, could be any politician)

3. Public mode outfit:
   - Suit: Dark navy or charcoal gray, perfectly tailored, expensive
   - Shirt: Crisp white, French cuffs
   - Tie: Conservative pattern (stripes or small dots), silk
   - Shoes: Black Oxford, polished
   - Accessories: Lapel pin (party logo), wedding band (widower), expensive watch
   - Posture: Confident, open, approachable
   - Expression: Warm sad smile (grieving but strong)

4. Private mode outfit:
   - Suit: Same suit but jacket off, top button undone
   - Shirt: White, slightly wrinkled, sleeves rolled up
   - Tie: Loosened or removed
   - Shoes: Same but scuffed
   - Accessories: Watch only (no lapel pin, wedding band removed)
   - Posture: Relaxed, predatory, prowling
   - Expression: Intense eyes, slight smirk, calculating

5. Facial expressions (need 5 for each mode):
   Public mode:
   - Neutral: Warm, approachable, slight sad smile
   - Happy: Genuine-seeming smile, eyes crinkle
   - Sad: Grieving widower look, downturned mouth, sympathetic eyes
   - Angry: Controlled anger, tight smile, cold eyes
   - Surprised: Raised eyebrows, open expression
   
   Private mode:
   - Neutral: Calculating, intense stare, slight smirk
   - Happy (lustful): Predatory smile, intense eyes
   - Angry: Cold fury, tight jaw, narrowed eyes
   - Surprised: Quick flash of panic, then calculation
   - Flirty: Suggestive smirk, lingering eye contact

6. Animations needed:
   - Idle (public): Confident stance, hands clasped or in pockets
   - Idle (private): Relaxed, prowling, hands gesturing
   - Walk (public): Confident stride, purposeful
   - Walk (private): Slower, more deliberate, predatory
   - Talk (public): Open gestures, warm expressions
   - Talk (private): Minimal gestures, intense stare
   - Mask switch transition: Subtle shift in posture and expression (2 seconds)

7. Technical requirements:
   - Polygon count: 10,000-15,000 tris (mobile-friendly)
   - Texture resolution: 2048x2048 (diffuse, normal, specular maps)
   - Rigging: Humanoid rig (Unity Mecanim compatible)
   - LODs: 3 levels (high, medium, low for mobile)
   - File format: FBX with separate material slots

8. Reference images:
   - Political photography: Study real politician body language (handshakes, press conferences)
   - Film noir: Study predatory character lighting and expressions
   - Disco Elysium: Character portrait style, color grading
   - The Wolf Among Us: 2.5D composition, lighting

9. Deliverables:
   - 3D model (FBX)
   - Textures (PNG/TGA)
   - Rigged and ready for animation
   - 5 facial expressions per mode (as blend shapes or separate meshes)
   - Material setup for Unity

OUTPUT:
- Complete art brief document (Markdown or PDF)
- Include reference image links
- Include technical specification sheet
- Include expression sheet (descriptions of all 10 expressions)
```

---

## 9. Balance & Tuning

### 9.1 Seduction Success Formula (Spreadsheet)

```
Using GDD section 3.1 (Triple Bar) and 3.4 (Seduction System), 
create a spreadsheet formula for calculating seduction success chance.

INPUTS:
- Interest (0-100): NPC's attraction to R. John
- Suspicion (0-100): NPC's suspicion of his true nature
- Mood (5 states): Relaxed, Stressed, Flirty, Angry, Neutral
- ApproachMatch (TRUE/FALSE): Does player's approach match NPC's personality?

FORMULA (from GDD):
Base Success = (Interest / 100) * 50 + ((100 - Suspicion) / 100) * 30 + (ApproachMatch ? 20 : 0)

Mood Modifier:
- Relaxed: +10%
- Stressed: -20%
- Flirty: +30%
- Angry: -40%
- Neutral: 0%

Final Success = MIN(95, MAX(5, Base Success + Mood Modifier))

SPREADSHEET IMPLEMENTATION:
Assume:
- Cell A2: Interest (0-100)
- Cell B2: Suspicion (0-100)
- Cell C2: Mood (text: "Relaxed", "Stressed", "Flirty", "Angry", "Neutral")
- Cell D2: ApproachMatch (TRUE/FALSE)

Formula in E2 (Base Success):
=(A2/100)*50 + ((100-B2)/100)*30 + IF(D2=TRUE, 20, 0)

Formula in F2 (Mood Modifier):
=IF(C2="Relaxed", 10, IF(C2="Stressed", -20, IF(C2="Flirty", 30, IF(C2="Angry", -40, 0))))

Formula in G2 (Final Success):
=MIN(95, MAX(5, E2 + F2))

EXAMPLE CALCULATIONS:
1. Emma (Interest 60, Suspicion 30, Flirty, ApproachMatch TRUE):
   Base = (60/100)*50 + (70/100)*30 + 20 = 30 + 21 + 20 = 71%
   Mood = +30% (Flirty)
   Final = 71 + 30 = 101% → capped at 95%

2. Maria (Interest 40, Suspicion 50, Stressed, ApproachMatch FALSE):
   Base = (40/100)*50 + (50/100)*30 + 0 = 20 + 15 + 0 = 35%
   Mood = -20% (Stressed)
   Final = 35 - 20 = 15%

3. Sophie (Interest 70, Suspicion 20, Neutral, ApproachMatch TRUE):
   Base = (70/100)*50 + (80/100)*30 + 20 = 35 + 24 + 20 = 79%
   Mood = 0% (Neutral)
   Final = 79 + 0 = 79%

OUTPUT:
- Spreadsheet formula as shown above
- Example calculations table
- Sensitivity analysis (how much does each input affect final chance?)
```

---

## 10. Testing & QA

### 10.1 Test Cases for Seduction System

```
Based on GDD section 3.4 (Seduction System), create a comprehensive test case 
document for QA testing of the seduction system.

TEST CASES:

TC-SED-001: Basic Seduction Flow
- Steps: Start seduction with Emma (Day 1), complete all 5 phases
- Expected: Seduction completes, Lust -40-60, Exposure +20-40, evidence created
- Pass criteria: All phases advance correctly, stats update, evidence in system

TC-SED-002: Seduction Success Chance Calculation
- Steps: Start seduction with known Interest/Suspicion/Mood, calculate success chance
- Expected: Formula matches GDD (Base + Mood Modifier, capped 5-95%)
- Pass criteria: Calculated chance matches manual calculation within 1%

TC-SED-003: Mood Impact on Seduction
- Steps: Seduce same NPC (Emma) in different moods (Flirty vs Angry)
- Expected: Flirty = +30% success, Angry = -40% success
- Pass criteria: Success rate differs by ~70% between best and worst mood

TC-SED-004: Personality Match Impact
- Steps: Seduce Maria (Ambitious) with Career approach vs Naive approach
- Expected: Career approach = +20% base success, Naive approach = 0%
- Pass criteria: Success rate differs by 20%

TC-SED-005: Seduction Failure Consequences
- Steps: Fail seduction (rejection), check exposure risk
- Expected: Exposure +10-30 (she may tell others)
- Pass criteria: Risk increases, NPC relationship worsens

TC-SED-006: Witness Detection
- Steps: Start seduction in public location with witnesses present
- Expected: +10-20 exposure risk, or seduction blocked
- Pass criteria: Risk increases or seduction prevented

TC-SED-007: Evidence Creation on Success
- Steps: Complete successful seduction, check evidence system
- Expected: 1-3 evidence items created (messages, photos, witnesses)
- Pass criteria: Evidence in system, correct type and location

TC-SED-008: Seduction Save/Load
- Steps: Start seduction, save game, load save, continue seduction
- Expected: Seduction state preserved (phase, interest, suspicion, mood)
- Pass criteria: Can continue from exact state before save

OUTPUT:
- Complete test case document (Markdown or spreadsheet)
- Include all test cases with steps, expected results, pass criteria
- Include edge cases and error conditions
```

---

## Appendix: Quick Reference

### GDD Section Quick Reference

| Section | Topic | Key Content |
|---------|-------|-------------|
| 1.1 | Core Premise | Win/lose conditions, hook |
| 2.2 | Characters | 10 NPCs with profiles |
| 3.1 | Triple Bar | Reputation, Lust, Exposure Risk |
| 3.2 | Mask System | Public/Private toggle |
| 3.3 | Mood System | 5 moods, modifiers, triggers |
| 3.4 | Seduction | 5 phases, success formula |
| 3.5 | Bribery | Methods, costs, risks |
| 3.6 | Evidence | Types, cover-ups, discovery |
| 3.7 | Time System | 6 slots/day, sandbox days |
| 3.8 | Dialogue | Public/private, personality-based |
| 3.10 | Mini-Games | 5 mini-games |
| 4.2 | Character Design | R. John, NPCs, expressions |
| 6.3 | Architecture | Project structure |
| 6.4 | Data Structures | JSON schemas |

### Prompt Template

```
Based on GDD section [X.X] ([Section Name]), generate [C# script / JSON / Art Brief / Spreadsheet] for [Specific Feature] with:

CONTEXT:
[Brief context from GDD]

REQUIREMENTS:
[List specific requirements, methods, properties, events]

INTEGRATE WITH:
[List other systems to integrate with]

OUTPUT:
[Describe expected output]
```

---

**END OF DOCUMENT**

*Last updated: September 28, 2026. For use with Claude Opus 5.5.*
