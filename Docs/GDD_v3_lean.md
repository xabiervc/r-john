# Game Design Document (GDD)
## R. John: Public Servant

**Version:** 3.0 (Lean)  
**Date:** September 28, 2026  
**Authors:** Xabier + Partner  
**Genre:** Narrative Stealth Adventure / Dark Comedy / Political Satire  
**Platform:** PC, Mobile (iOS/Android)  
**Engine:** Unity or Godot (to decide in Phase 1)  
**Target Audience:** Adults (18+), fans of narrative adventures, dark comedy, political satire

---

## 1. High Concept

### 1.1 Core Premise
**R. John** is a 52-year-old charismatic politician with a flawless public image: intellectual, progressive, feminist ally, and grieving widower. Behind closed doors, he is a degenerate obsessed with one goal: sleeping with as many women as possible without getting caught.

The player controls R. John through **one critical week** (7 days) leading to a major political vote. Every interaction is a balancing act: pursue private desires while maintaining perfect public facade.

**Win/Lose Conditions:**
- **LOSE A (Exposed):** Getting caught = career destroyed, labeled misogynist, #MeToo headline
- **LOSE B (Settled):** Entering stable relationship = personal failure (he's a degenerate, not a romantic)
- **WIN:** Maximize conquests while maintaining perfect public image = ultimate degenerate victory

### 1.2 Unique Hook
> "A stealth adventure where your greatest enemy is your own reputation. Seduce, manipulate, and bribe your way through a week of political pressure—without becoming a #MeToo headline."

### 1.3 Key Innovations
1. **Triple Win-Lose Condition:** Creates constant tension (not present in traditional dating sims or adventures)
2. **Mask System:** Switch between public persona and private degenerate in real-time
3. **Mood System:** NPCs have dynamic moods that affect seduction success (read the room)
4. **Sandbox Days:** Days 3, 5, 7 are open-ended (player chooses pace), days 1, 2, 4, 6 are story-critical
5. **Multiple Endings (8):** High replayability (3-4 playthroughs to see everything)

### 1.4 Duration & Pacing
- **First playthrough:** 6-7 hours (more fluid than Leisure Suit Larry's 6-8 hours)
- **Completionist (all endings):** 18-25 hours (3-4 playthroughs)
- **Structure:** 7 chapters (one per day), with days 3, 5, 7 as sandbox (more freedom)
- **Flow:** Less backtracking than classic adventures, more focus on observation and timing

---

## 2. Story & Narrative

### 2.1 Synopsis
R. John is a senior politician (52 years old) from the progressive party "Forward Together" (fictional). He's publicly a widower (wife Margaret died 3 years ago in a car accident), has no recognized children, and positions himself as a champion of women's rights. In reality, he's a predator who uses his power, charm, and resources to pursue women relentlessly.

**The Week:**
- **Day 1-2:** Preparation for televised debate on gender equality (story-critical, linear)
- **Day 3:** Party congress travel (sandbox, new opportunities)
- **Day 4:** Congress day 1 (story-critical, high visibility)
- **Day 5:** Congress day 2 + free evening (sandbox, maximum risk/reward)
- **Day 6:** Return to capital, investigation intensifies (story-critical, crisis mode)
- **Day 7:** The debate + vote + final reckoning (climax, all paths converge)

### 2.2 Main Characters

#### R. John (Protagonist)
- **Age:** 52 years old
- **Public Image:** Grieving widower, intellectual, feminist ally, progressive champion, lonely but dedicated
- **Private Reality:** Degenerate predator, obsessed with conquest, manipulative, selfish
- **Mechanic:** "Mask System" (switch between public persona and private self)
- **Inner Voice:** Two competing thoughts (public calculations vs private urges)
- **Backstory:** Wife (Margaret) died 3 years ago, no children, uses widowhood as sympathy card

#### Margaret (Deceased Wife - Mentioned Only)
- **Role:** Public sympathy tool
- **Death:** Car accident 3 years ago (official story)
- **Function:** R. John mentions her strategically ("my late wife would have supported this")
- **Plot Twist (optional):** She may have known about his behavior before death (lore only)

#### Maria (Press Secretary)
- **Age:** 34
- **Role:** Manages R. John's public image 24/7
- **Personality:** Ambitious, efficient, loyal, increasingly suspicious
- **Function:** Limits player actions, warns of risks, can be bribed or manipulated
- **Risk Level:** High (knows schedule intimately)
- **Seduction Profile:** Responds to career promises, flattery, power displays
- **Mood Patterns:** Stressed in mornings, relaxed in evenings, angry when things go wrong

#### Laura (Personal Assistant)
- **Age:** 26
- **Role:** Manages schedule, travel, logistics
- **Personality:** Naive, eager to please, ambitious, posts on social media
- **Function:** Multiple routes (conquest target, ally if bribed, enemy if betrayed)
- **Risk:** Medium-High (young, may talk to friends, social media presence)
- **Seduction Profile:** Responds to attention, flattery, career promises
- **Mood Patterns:** Flirty when praised, stressed before deadlines, neutral otherwise

#### Carlos (Political Rival)
- **Age:** 55
- **Role:** Opposition politician, seeks to destroy R. John
- **Personality:** Ruthless, cunning, wealthy, always watching
- **Function:** Primary antagonist, hires investigators, creates scandals
- **Threat Level:** Constant (actively investigates, has resources)
- **Weakness:** Has his own secrets (player can investigate for leverage)
- **Not Seduceable:** Pure antagonist

#### Sophie (Investigative Journalist)
- **Age:** 32
- **Role:** Writing exposé on R. John for major publication
- **Personality:** Tenacious, intelligent, morally ambiguous, ambitious
- **Function:** Can be bribed, seduced, outsmarted, or turned into ally
- **Risk:** Highest (has resources, contacts, persistence, editorial support)
- **Seduction Profile:** Responds to intellectual conversation, exclusives, insider access
- **Mood Patterns:** Neutral when investigating, flirty when given exclusives, angry when blocked

#### Conquest Targets (8 NPCs)

| Name | Age | Role | Risk | Personality | Mood Patterns | Best Approach |
|------|-----|------|------|-------------|---------------|---------------|
| **Emma** | 24 | Young Intern | Low | Naive, idealistic | Flirty when praised, nervous around authority | Flattery, mentorship, career promises |
| **Jessica** | 29 | TV Journalist | Medium | Ambitious, cynical | Stressed before broadcasts, flirty when given scoops | Exclusive interviews, insider info |
| **Olivia** | 35 | Party Colleague | Medium | Professional, guarded | Neutral in office, relaxed at events | Intellectual conversation, policy talk |
| **Isabella** | 27 | Hotel Staff (Congress) | Low | Friendly, flirty | Flirty on evening shifts, tired in mornings | Direct, gifts, cash tips |
| **Victoria** | 31 | Influencer/Activist | High | Image-conscious, savvy | Flirty at parties, stressed before events | Social media collabs, photo ops |
| **Rachel** | 26 | Campaign Volunteer | Low | Eager, starstruck | Flirty when alone, nervous in groups | Attention, promises of access |
| **Natalie** | 33 | Lobbyist | High | Calculating, experienced | Neutral in meetings, flirty in private | Mutual benefit, quid pro quo |
| **Ashley** | 25 | Maria's Friend | Medium-High | Social, gossipy | Flirty at parties, stressed at work | Group settings, parties, drinks |

### 2.3 Narrative Structure

**7 Chapters (One Per Day):**

| Day | Type | Duration | Key Events | Conquest Opportunities |
|-----|------|----------|------------|------------------------|
| **Day 1** | Story-Critical | 45 min | Debate prep, press conference, office | Emma (intern), Laura (assistant) |
| **Day 2** | Story-Critical | 45 min | TV interview, charity gala | Jessica (journalist), Olivia (colleague) |
| **Day 3** | **Sandbox** | 90 min | Travel to congress, hotel check-in | Isabella (hotel staff), free choice |
| **Day 4** | Story-Critical | 45 min | Congress day 1, keynote speech | Victoria (influencer), Natalie (lobbyist) |
| **Day 5** | **Sandbox** | 90 min | Congress day 2, evening party | Ashley (Maria's friend), multiple options |
| **Day 6** | Story-Critical | 45 min | Return to capital, crisis management | Risk: Sophie investigation intensifies |
| **Day 7** | **Sandbox/Climax** | 90 min | Final debate, vote, endings | Final conquests or cover-up |

**Multiple Endings (8 total):**

1. **Ultimate Degenerate Victory:** 5+ conquests, zero exposure, wins vote, continues career [WIN]
2. **Moderate Victory:** 3-4 conquests, low exposure, career intact [WIN]
3. **Exposed Scandal:** Caught by journalist/rival, career destroyed, labeled misogynist [LOSE]
4. **#MeToo Headline:** Multiple accusers, public trial, social death [LOSE - WORST]
5. **Settled Down:** Enters stable relationship, loses "freedom" [LOSE - PERSONAL]
6. **Blackmailed Forever:** Survives but pays bribes indefinitely, trapped [PARTIAL WIN]
7. **Forced Resignation:** Pressure too high, quietly steps down [LOSE]
8. **Secret President:** Perfect play, becomes head of government while continuing double life [SECRET WIN]

---

## 3. Gameplay Mechanics

### 3.1 Core System: The Triple Bar

#### Reputation Bar (0-100) - VISIBLE
- **High (70-100):** Media support, allies trust you, easier to dismiss accusations
- **Medium (40-69):** Neutral, normal political pressure
- **Low (0-39):** Suspicious media, allies distance themselves
- **Critical (<20):** One scandal triggers career destruction
- **Increases:** Public speeches, charitable acts, widowhood mentions, successful debates
- **Decreases:** Failed seductions, witnessed inappropriate behavior, bribes discovered

#### Lust Bar (0-100) - VISIBLE
- **High (70-100):** Satisfied, better decisions, but more confident/risky
- **Medium (40-69):** Normal state, balanced risk-taking
- **Low (0-39):** Frustrated, impulsive decisions, unnecessary risks
- **Critical (<20):** Reckless, may attempt dangerous seductions
- **Increases:** Time passing, seeing attractive NPCs, resisting urges
- **Decreases:** Successful conquests, viewing private content

#### Exposure Risk Bar (0-100) - HIDDEN
- **Hidden from player** (shown as vague "Pressure" indicators: Low/Medium/High/Critical)
- **Low (0-30):** Safe, minimal evidence
- **Medium (31-60):** Some evidence, witnesses may talk
- **High (61-80):** Strong evidence, journalist investigating
- **Critical (81-100):** Exposure imminent, one mistake = scandal
- **Increases:** Each conquest, bribing people, being seen in private moments
- **Decreases:** Destroying evidence, silencing witnesses, successful cover-ups

### 3.2 The Mask System

R. John can toggle between two modes (when not in front of witnesses):

#### Public Mask (Active)
- **Behavior:** Perfect politician, grieving widower
- **Actions:** Speeches, donations, policy work, sympathy plays
- **Effects:** +Reputation, -Lust, -Exposure Risk (slowly)
- **Restrictions:** Cannot pursue conquests, cannot visit private locations
- **NPC Perception:** Respectable, sympathetic leader

#### Private Mask (Active)
- **Behavior:** True degenerate self
- **Actions:** Pursue conquests, visit private locations, dating apps, inappropriate messages
- **Effects:** -Reputation (if seen), +Lust, +Exposure Risk
- **Restrictions:** Cannot attend public events
- **NPC Perception:** Some see opportunity, others see danger

**Mechanic:** Switching masks takes time (animation, location change). Cannot switch in front of witnesses.

### 3.3 Mood System (NEW)

Each NPC has a **Current Mood** that dynamically affects seduction success.

#### 5 Mood States

| Mood | Interest Modifier | Suspicion Modifier | Best For | Visual Cues |
|------|-------------------|-------------------|----------|-------------|
| **Relaxed** | +10 | -10 | Safe approach, steady progress | Smiling, open body language, slow movements |
| **Stressed** | -20 | +15 | Avoid or use stress-relief approach | Frowning, tense posture, checking watch/phone |
| **Flirty** | +30 | -20 | Golden opportunity, escalate fast | Eye contact, touching hair, leaning in, lingering looks |
| **Angry** | -40 | +30 | Do NOT approach, wait or defuse | Crossed arms, sharp movements, cold expression |
| **Neutral** | 0 | 0 | Baseline, standard approach | Normal expression, neutral body language |

#### Mood Triggers (What Changes Mood)

| Trigger | Affected NPCs | Mood Change | Duration |
|---------|---------------|-------------|----------|
| **Time of Day** | All | Morning: Stressed, Afternoon: Neutral, Evening: Relaxed/Flirty | Persistent |
| **Recent Event (Good)** | Specific NPC | Relaxed or Flirty (+10-30 Interest) | 1-2 scenes |
| **Recent Event (Bad)** | Specific NPC | Stressed or Angry (-20-40 Interest) | 1-2 scenes |
| **Player Helped Earlier** | Specific NPC | Relaxed (+10 Interest, -10 Suspicion) | Rest of day |
| **Player Insulted/Rejected** | Specific NPC | Angry (-40 Interest, +30 Suspicion) | Rest of day |
| **Location** | All | Office: Stressed/Neutral, Bar/Party: Relaxed/Flirty | While in location |
| **Alcohol Consumed** | NPC (if drinking) | Flirty (+20 Interest, -15 Suspicion) | 1 scene |
| **Compliment Received** | Specific NPC | Flirty (+15 Interest) | 1 scene |

#### How Player Reads Mood

**Visual (Primary):**
- Character art changes (expression, body language)
- Color grading (warm = flirty/relaxed, cool = stressed/angry)
- Animation (relaxed = slow, stressed = fidgety)

**Dialogue (Secondary):**
- NPC dialogue options change slightly based on mood
- Example: Stressed Laura says "I'm so busy right now" vs Flirty Laura says "Hey, I was hoping you'd stop by"

**UI (Optional, Subtle):**
- Small mood icon next to NPC name in dialogue (not a number, just emoji-style indicator)
- Example: 😊 (Relaxed), 😤 (Stressed), 😏 (Flirty), 😠 (Angry), 😐 (Neutral)

#### Mood Impact on Seduction

**Success Chance Formula:**
```
Base Success = (Interest / 100) * 50 + (100 - Suspicion) / 100 * 30 + Approach Match * 20

Mood Modifier:
- Relaxed: +10%
- Stressed: -20%
- Flirty: +30%
- Angry: -40%
- Neutral: 0%

Final Success = Base Success + Mood Modifier
```

**Example:**
- Emma has Interest 60, Suspicion 30, player uses correct approach
- Base Success = (60/100)*50 + (70/100)*30 + 20 = 30 + 21 + 20 = 71%
- Emma is **Flirty** (mood): +30%
- **Final Success = 101% → capped at 95%** (never 100%)

**Example 2:**
- Same Emma, but she's **Angry** (mood): -40%
- **Final Success = 71% - 40% = 31%** (much riskier)

### 3.4 Seduction System (5 Phases)

Each conquest follows a **5-phase mini-game**:

#### Phase 1 - Approach
- **Choose:** Location and timing (private vs public)
- **Check:** NPC's current mood (visual/dialogue cues)
- **Risk:** Being seen approaching = +Exposure Risk (+10-20)
- **Success:** Move to Phase 2

#### Phase 2 - Conversation
- **Dialogue Tree:** Personality-based choices (see section 2.2 for each NPC's type)
- **Build:** Rapport, find common ground
- **Read:** Mood changes during conversation (if you say wrong thing, mood worsens)
- **Risk:** Wrong choice = -Interest (-10-20), +Suspicion (+10-20), mood worsens
- **Success:** Interest +20-30, move to Phase 3

#### Phase 3 - Escalation
- **Actions:** Gradual advances (compliments, light touch, invitations)
- **Watch:** For resistance (mood change to Stressed/Angry) or encouragement (mood change to Flirty)
- **Risk:** Too fast = mood becomes Angry, rejection; too slow = loses interest
- **Success:** Interest +20-40, Suspicion +10-20 (she's catching on), move to Phase 4

#### Phase 4 - Climax
- **Final Push:** Direct proposition, invitation to private location
- **Success Chance:** Calculated based on Interest, Suspicion, Mood, Approach Match
- **Risk:** Rejection = she may tell others (+Exposure +10-30)
- **Success:** Conquest completed, Lust -40-60, Exposure Risk +20-40 (evidence created)

#### Phase 5 - Aftermath
- **Manage:** Evidence (delete messages, ensure silence)
- **Exit:** Cleanly without being seen leaving
- **Risk:** Being seen leaving together = witness created (+Exposure +20-30)
- **Success:** Conquest logged, NPC relationship updated (may be ally, neutral, or enemy)

### 3.5 Bribery & Silence System

When at risk of exposure, R. John can **bribe or silence** people:

#### Bribery Options

| Method | Cost | Effectiveness | Risk | Best For |
|--------|------|---------------|------|----------|
| **Direct Cash** | €5k-50k | High (immediate) | Medium (financial trail) | One-time witnesses, low-level NPCs |
| **Career Favors** | Future cost | Medium | Low (hard to trace) | Ambitious NPCs (Laura, Maria) |
| **Blackmail Counter** | Investigation cost | Very High | High (if caught) | Hostile NPCs (Sophie, Carlos) |
| **Gifts & Luxury** | €2k-20k | Medium | Low (appears legitimate) | Venal NPCs (Isabella, Ashley) |
| **Exclusive Access** | Low | Low-Medium | Low | Journalists (Jessica, Sophie) |

#### Silence Mechanics

**One-Time Payment:**
- Cheaper upfront (€5k-20k)
- NPC may come back for more later (random events)
- Risk: They talk to others about being paid (+Exposure +10)

**Permanent Silence:**
- Expensive (€30k-100k)
- Removes them as threat permanently
- Risk: Large payment may be discovered by investigators (+Exposure +30 if found)

**Leverage Creation:**
- Gather dirt on them (investigation mini-game)
- Cost: 2-3 time slots, risk of being caught
- Effect: They can't talk without self-incriminating
- Best for: Sophie, Carlos, hostile witnesses

### 3.6 Evidence & Cover-Up System

Every conquest leaves **evidence** that can be discovered:

#### Types of Evidence

| Type | Examples | Remove Difficulty | Risk if Found |
|------|----------|-------------------|---------------||
| **Digital Messages** | WhatsApp, SMS, emails, DMs | Easy (delete) | Medium (backups exist) |
| **Photos** | Selfies, paparazzi, security cameras | Hard (can't control others) | High |
| **Physical Items** | Clothing, gifts, hotel receipts | Medium (retrieve/destroy) | Medium |
| **Witnesses** | People who saw you together | Hard (must bribe/intimidate) | High |
| **Digital Footprint** | Location data, credit cards, ride-share | Medium (pay tech people) | Medium |

#### Cover-Up Actions

| Action | Time Cost | Success Rate | Risk if Failed |
|--------|-----------|--------------|----------------|
| **Delete Messages** | 1 slot | 80% | +Exposure +30 (backups exist) |
| **Retrieve Physical Evidence** | 2-4 slots + travel | Skill-based | +Exposure +50 (caught in act) |
| **Pay Off Witness** | 1 slot | 90% | +Exposure +20 (they talk anyway) |
| **Create Alibi** | 2-3 slots | 70% | +Exposure +40 (alibi debunked) |
| **Destroy Digital Footprint** | 1 slot + €10k-50k | 85% | +Exposure +30 (hackers caught) |

### 3.7 Time & Schedule System

#### Daily Structure (6 Time Slots Per Day)

| Slot | Time | Available Actions |
|------|------|-------------------||
| **Morning** | 6:00-12:00 | Public events, press conferences, meetings |
| **Afternoon** | 12:00-19:00 | Political work, travel, public appearances |
| **Evening** | 19:00-24:00 | Dinners, events, private opportunities |
| **Night** | 24:00-6:00 | Private time, high-risk activities, rest |

#### Story-Critical Days (1, 2, 4, 6)
- **Mandatory Events:** 3-4 slots (debates, meetings, press conferences)
- **Free Slots:** 2-3 slots (can use for conquests, cover-ups, bribes)
- **Pacing:** More linear, less flexibility

#### Sandbox Days (3, 5, 7)
- **Mandatory Events:** 1-2 slots (minimal obligations)
- **Free Slots:** 4-5 slots (player chooses how to spend)
- **Pacing:** Open-ended, player sets pace
- **Opportunities:** More conquest options, more risks

#### Action Costs

| Action | Time Cost |
|--------|-----------||
| Public Speech | 1-2 slots |
| Meeting | 1 slot |
| Travel | 1 slot |
| Seduction (full 5 phases) | 2-3 slots |
| Cover-Up | 1-4 slots |
| Bribery | 1 slot |
| Investigation | 2-3 slots |
| Rest | 1 slot (Lust +20) |

### 3.8 Dialogue System

#### Branching Dialogue Trees

**Public Dialogue:**
- What R. John says out loud
- Affects Reputation primarily
- Options: "safe" (politically correct, sympathetic)

**Private Thoughts (Inner Monologue):**
- What he thinks internally (shown to player only)
- Affects Lust and decision-making
- Options: "true" (degenerate, selfish, calculating)

**Example:**
```
[Sophie, Journalist]: "Mr. John, your voting record on women's issues is impressive. 
What drives your commitment to feminism?"

PUBLIC OPTIONS:
- "Women deserve full equality in all spheres of society." 
  → +Reputation (+5), -Lust (-3)
  
- "My late wife Margaret would have wanted me to fight for this." 
  → +Reputation (+8), -Lust (-5), +Sympathy
  
- "It's simply the right thing to do." 
  → +Reputation (+4), Neutral Lust

PRIVATE THOUGHTS (Player Only):
- "What drives me? The 25-year-old intern in my office, for one." 
  → +Lust (+5), may trigger reckless action
  
- "This journalist is hot. If I say the right thing, maybe she'll invite 
  me to her podcast... alone." 
  → +Lust (+8), +Interest (Sophie), +Risk
  
- "She's digging. I need to deflect. Maybe compliment her work?" 
  → Strategic, +Reputation (+2), -Risk (-5)
```

#### Personality-Based Responses

| NPC Personality | Responds To | Avoid |
|-----------------|-------------|-------||
| **Naive** (Emma, Rachel) | Flattery, mentorship, encouragement | Cynicism, directness |
| **Ambitious** (Jessica, Laura, Maria) | Career offers, connections, exclusives | Condescension, vagueness |
| **Cynical** (Natalie, Carlos, Sophie) | Honesty (ironic), directness, quid pro quo | Idealism, flattery |
| **Idealistic** (Emma, Olivia) | Policy talk, shared values, moral arguments | Cynicism, selfishness |
| **Venal** (Isabella, Ashley) | Cash, gifts, luxury, direct benefits | Moral arguments, vagueness |

### 3.9 Inventory System

#### Public Items
- Suits (3 types): Required for public events, +Reputation if matched
- Ties/Cufflinks: Cosmetic, minor +Reputation
- Official Documents: Required for meetings/debates
- Phone (Public): Email, calendar, news apps
- Family Photos: Use in sympathy plays ("Margaret would...")

#### Private Items
- Condoms (various): Required for conquests
- Dating Apps: Find conquest targets, arrange meetings
- Gifts: Jewelry, flowers, luxury items for conquests
- Cash (untraceable): For bribes, tips, private payments
- Hotel Key Cards: Access to private locations
- Incriminating Photos: Leverage on others (blackmail)
- Private Phone: Separate device for private communications

**Risk:** If searched while carrying private items = massive scandal

### 3.10 Mini-Games

#### 1. Debate Mini-Game
- **Format:** Quick-time dialogue choices
- **Mechanic:** Choose correct policy positions under time pressure
- **Success:** +Reputation (+10-15), media praise
- **Failure:** -Reputation (-10-20), gaffes go viral
- **Occurrences:** Day 2, Day 7

#### 2. Blackmail Investigation
- **Format:** Stealth/investigation mini-game
- **Mechanic:** Gather dirt on targets without being caught
- **Success:** Gain leverage for silence
- **Failure:** +Exposure Risk, target becomes enemy
- **Targets:** Sophie, Carlos, hostile witnesses

#### 3. Evidence Destruction
- **Format:** Stealth/puzzle mini-game
- **Mechanic:** Retrieve or destroy evidence from locations
- **Success:** -Exposure Risk (-20-40)
- **Failure:** Caught in act, massive scandal (+Exposure +50)
- **Locations:** Hotel rooms, NPC apartments, news offices

#### 4. Social Media Management
- **Format:** Resource management / quick-time events
- **Mechanic:** Post correct content, respond to crises, manage hashtags
- **Success:** +Reputation (+5-10), control narrative
- **Failure:** -Reputation (-10-20), scandal spreads

#### 5. Bribe Negotiation
- **Format:** Dialogue/negotiation mini-game
- **Mechanic:** Determine how much to pay, detect if they're bluffing
- **Success:** Pay minimum, secure silence
- **Failure:** Overpay, or they talk anyway

---

## 4. Art & Visual Style

### 4.1 Visual Direction
- **Style:** 2.5D (3D characters on hand-painted 2D backgrounds)
- **Aesthetic:** Modern political thriller meets dark comedy
- **Color Palette:**
  - **Public Scenes:** Cold, clean, professional (blues, grays, whites)
  - **Private Scenes:** Warm, saturated, intimate (reds, ambers, deep shadows)
  - **Transition:** Subtle "glitch" or filter shift when switching masks

### 4.2 Character Design

#### R. John
- **Age:** 52, distinguished but still attractive
- **Public:** Perfect suit, silver hair, warm sad smile (grieving widower)
- **Private:** Slightly disheveled, intense eyes, predatory smile
- **Unique:** Eyes change subtly between modes (warm/public vs cold/private)

#### NPCs
- **Design:** Realistic proportions with slight caricature for satire
- **Variety:** Diverse ages, ethnicities, body types
- **Mood Expressions:** Each NPC has 5 distinct expressions (Relaxed, Stressed, Flirty, Angry, Neutral)

### 4.3 Environment Design

#### Public Locations (8-10 total)
- Government Buildings: Sterile, imposing, marble, flags
- TV Studios: Bright lights, cameras, polished surfaces
- Press Conference Rooms: Podiums, microphones, journalist crowd
- Party Headquarters: Busy, campaign posters, volunteers
- Charity Galas: Elegant, wealthy donors, auction items

#### Private Locations (8-10 total)
- Hotel Rooms: Luxurious but generic, mini-bar, dim lighting
- Private Offices: After hours, desk cleared, door locked
- Upscale Bars: Dim, intimate booths, expensive drinks
- R. John's Apartment: Modern, minimalist, photos of Margaret (strategic)

### 4.4 UI/UX Design

#### HUD
- **Top Bar:** Reputation (visible), Lust (visible), Pressure (vague: Low/Med/High/Crit)
- **Bottom Bar:** Time slot, location, mask indicator (Public/Private icon)
- **Corner:** Phone icon (inventory, messages, apps, calendar)

#### Dialogue UI
- **Public Speech:** Clean white text bubbles
- **Private Thoughts:** Darker bubbles, different font (player only)
- **Mood Indicator:** Small emoji icon next to NPC name (😊😤😏😠😐)

---

## 5. Audio & Sound Design

### 5.1 Musical Score

#### Public Mode
- **Style:** Orchestral, inspiring, documentary-style
- **Instruments:** Strings, piano, light brass
- **Mood:** Hopeful, serious, sympathetic (widower theme)

#### Private Mode
- **Style:** Jazz-noir, synthwave, sensual but tense
- **Instruments:** Saxophone, upright bass, synth pads
- **Mood:** Intimate, dangerous, predatory

#### Transitions
- **Mask Switch:** Sharp audio cue, filter change
- **Risk Spike:** Dissonant strings, heartbeat sounds
- **Scandal Trigger:** Dramatic orchestral hit, camera shutters

### 5.2 Sound Effects
- **Public:** Camera shutters, crowd murmurs, microphone feedback, applause
- **Private:** Door locks, phone notifications, ice in glasses, distant traffic
- **UI:** Positive chime (Reputation up), negative buzz (Reputation down), tension strings (Risk up)

---

## 6. Technical Specifications

### 6.1 Engine & Tools
- **Engine:** Unity 2024 LTS or Godot 4.x (decision in Phase 1)
- **Language:** C# (Unity) or GDScript (Godot)
- **Version Control:** Git + GitHub (private repo)
- **Dialogue System:** Ink or custom JSON-based
- **Project Management:** Notion or Linear

### 6.2 Platforms
- **Primary:** PC (Steam, Epic, GOG) - Windows, macOS, Linux
- **Secondary:** Mobile (iOS, Android) with touch controls
- **Future:** Consoles (Switch, PS5, Xbox) if successful

### 6.3 Project Architecture

```
/RJohn_PublicServant
├── /Assets
│   ├── /Scenes
│   │   ├── MainMenu
│   │   ├── Chapter1_Day1
│   │   ├── Chapter2_Day2
│   │   ├── Chapter3_Day3
│   │   ├── Chapter4_Day4
│   │   ├── Chapter5_Day5
│   │   ├── Chapter6_Day6
│   │   ├── Chapter7_Day7
│   │   └── /Endings (8 ending scenes)
│   │
│   ├── /Scripts
│   │   ├── /Core (GameManager, SaveSystem, TimeSystem, EventBus)
│   │   ├── /Mechanics (Reputation, Lust, ExposureRisk, Mask, Seduction, Bribery, Evidence, Mood)
│   │   ├── /Dialogue (DialogueManager, DialogueTree, PersonalitySystem)
│   │   ├── /UI (HUD, Menus, Inventory, DialogueUI)
│   │   ├── /AI (NPCSchedule, InvestigationAI, WitnessAI, MoodAI)
│   │   └── /MiniGames (Debate, BribeNegotiation, EvidenceDestruction)
│   │
│   ├── /Art
│   │   ├── /Characters (R. John Public/Private, NPCs with 5 moods each)
│   │   ├── /Backgrounds (Public locations, Private locations)
│   │   ├── /UI (HUD elements, menus, dialogue boxes)
│   │   └── /Effects (Mask transition, mood indicators)
│   │
│   ├── /Audio
│   │   ├── /Music (Public theme, Private theme, Transitions, Endings)
│   │   ├── /SFX (UI, Environment, Character)
│   │   └── /VO (R. John internal, NPCs - optional)
│   │
│   └── /Data
│       ├── /Dialogue (JSON per chapter, per NPC)
│       ├── /NPCs (Profiles, Seduction profiles, Mood profiles)
│       ├── /Items (Item database)
│       └── /Endings (Ending conditions, triggers)
│
├── /Docs
│   ├── GDD.md (this document)
│   ├── TechnicalArchitecture.md
│   └── ArtStyleGuide.md
│
└── README.md
```

### 6.4 Data Structures (Key JSON Schemas)

#### NPC Profile
```json
{
  "id": "npc_maria",
  "name": "Maria",
  "role": "Press Secretary",
  "age": 34,
  "personality": "Ambitious",
  "riskProfile": "High",
  "seductionProfile": {
    "baseInterest": 30,
    "baseSuspicion": 40,
    "preferredApproaches": ["Career", "Flattery", "Power"],
    "conquestDifficulty": "Hard"
  },
  "moodProfile": {
    "defaultMood": "Neutral",
    "morningMood": "Stressed",
    "eveningMood": "Relaxed",
    "triggers": {
      "playerHelped": "Relaxed",
      "playerRejected": "Angry",
      "beforeDeadline": "Stressed",
      "afterCompliment": "Flirty"
    }
  },
  "schedule": {
    "Day1": ["Morning: Office", "Afternoon: Press Conference", "Evening: Free"],
    "Day2": ["Morning: Free", "Afternoon: Gala", "Evening: Free"]
  },
  "dialogueTree": "dialogue_maria.json"
}
```

#### Seduction Success Formula (for reference)
```
Base Success = (Interest / 100) * 50 + ((100 - Suspicion) / 100) * 30 + (ApproachMatch ? 20 : 0)

Mood Modifier:
- Relaxed: +10%
- Stressed: -20%
- Flirty: +30%
- Angry: -40%
- Neutral: 0%

Final Success = min(95, max(5, Base Success + Mood Modifier))
```

---

## 7. Development Roadmap (Lean)

### Phase 1: Pre-Production (Month 1-2)
**Goals:** Finalize design, prototype core systems, art tests

- [ ] Week 1-2: Finalize GDD, choose engine, set up repo
- [ ] Week 3-4: Prototype Reputation, Lust, Mask, basic dialogue
- [ ] Week 5-6: Mood system prototype, art style test (R. John + 1 NPC)
- [ ] Week 7-8: Playable prototype (1 location, 1 NPC, basic seduction)

**Deliverables:**
- Approved GDD (this doc)
- Technical architecture doc
- Art style guide
- Playable prototype (10-min demo)

### Phase 2: Core Systems (Month 3-5)
**Goals:** All mechanics functional, Chapter 1 complete

- [ ] Month 3: All core systems (Reputation, Lust, Risk, Mask, Seduction, Mood, Bribery, Evidence)
- [ ] Month 4: Chapter 1 (Day 1-2) fully implemented (art, dialogue, all systems)
- [ ] Month 5: Chapter 2-3 (Day 3-4), internal alpha (Chapters 1-3 playable)

**Deliverables:**
- All mechanics implemented
- Chapters 1-3 complete (50% content)
- Internal alpha build

### Phase 3: Content (Month 6-9)
**Goals:** All chapters complete, art finalized

- [ ] Month 6: Chapter 4-5 (Day 5-6), investigation mechanics
- [ ] Month 7: Chapter 6-7 (Day 7 + all 8 endings)
- [ ] Month 8: Polish, bug fixes, balance tuning
- [ ] Month 9: Final art pass, audio implementation, content complete

**Deliverables:**
- All 7 chapters complete
- All 8 endings implemented
- Full art and audio
- Beta build (content complete)

### Phase 4: Polish & Launch (Month 10-12)
**Goals:** Bug-free, optimized, released

- [ ] Month 10: QA testing (all paths, all endings), bug fixing
- [ ] Month 11: Optimization (performance, mobile), localization (ES, FR, DE)
- [ ] Month 12: Marketing, launch (PC + Mobile), post-launch support

**Deliverables:**
- Gold master build
- Game launched on Steam, Epic, iOS, Android
- Post-launch support plan

---

## 8. Appendix

### 8.1 Competitive Analysis (Brief)

| Game | Similarities | What We Do Better |
|------|--------------|-------------------||
| **Disco Elysium** | Deep narrative, internal voices, political themes | More focused win/lose tension, seduction as stealth mechanic |
| **Life is Strange** | Branching narrative, consequences, modern setting | Adult themes, strategic gameplay (reputation management), satire |
| **Leisure Suit Larry** | Sexual theme, adventure, comedy | Modern satire, real consequences, multiple endings, mood system |
| **The Wolf Among Us** | 2.5D art, noir tone, moral choices | More player agency, 8 distinct endings, political satire |

### 8.2 Key Art References
- **Disco Elysium:** Character portraits, dialogue UI, color grading
- **The Wolf Among Us:** 2.5D composition, lighting
- **Firewatch:** Environmental storytelling, color palettes
- **Night in the Woods:** Character expressions, body language

### 8.3 Claude Opus 5.5 Integration

**For Code Generation:**
```
Prompt: "Based on GDD section 6.4 (Architecture) and 6.5 (Data Structures), 
generate C# script for MoodSystem.cs with:
- Track NPC mood (5 states)
- Methods: SetMood(npcId, mood), GetMood(npcId), GetMoodModifier(mood)
- Integrate with SeductionSystem.cs
- Use EventBus pattern from GDD"
```

**For Dialogue Generation:**
```
Prompt: "Using GDD section 2.2 (Characters) and 3.8 (Dialogue System), 
generate dialogue JSON for Maria Chapter 1. Include:
- 5 public options with reputation effects
- 5 private thoughts with lust effects
- Mood-based variations (Stressed morning vs Relaxed evening)
- Personality-based responses (Ambitious type)"
```

**For Balance Tuning:**
```
Prompt: "Using GDD section 3.1 (Triple Bar) and 3.4 (Seduction), 
create spreadsheet formula for seduction success based on:
- Interest (0-100), Suspicion (0-100), Mood (5 states), Approach Match (bool)
Output: 5-95% success chance"
```

---

**END OF DOCUMENT**

*Last updated: September 28, 2026. Version 3.0 (Lean, 2-person team).*