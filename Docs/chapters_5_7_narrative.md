# Chapters 5–7 Narrative Package

## Content standard
All characters are adults. Dialogue and outcomes must preserve informed, freely given consent; coercion, employment leverage, intimidation, bribery, and cover-up are not romantic-success routes. They instead increase scrutiny, end collaboration, or trigger accountability paths.

## Chapter 5 — Congress Day 2
**Type:** Sandbox, 90 minutes. **Mandatory:** Congress session, morning, congress hall.

### Dramatic purpose
The investigation becomes visible. Sophie has corroborating leads, Carlos exploits every mistake, and John must decide whether to answer evidence, cooperate with counsel, or double down publicly.

### Beats
1. Morning vote: John must attend the congress session in Public Mask; a poor debate result reduces Reputation.
2. Ashley's party invitation: Ashley can offer a friendly social route only after a clear invitation and an equal-footing check-in. Declining is always valid and has no penalty.
3. Victoria follow-up: Victoria requests a transparent, consensual on-record collaboration or walks away. Any attempt to use political access as leverage ends the route and creates a witness flag.
4. Natalie policy meeting: Natalie offers lawful policy advocacy; secret quid-pro-quo arrangements create an investigation flag rather than a reward.
5. Sophie lead: player can provide documents, issue a truthful statement, consult counsel, or evade questions. Evidence cannot be erased by a payment.
6. Closing trigger: `investigation_intensifies` if two or more evidence flags, a witness flag, or Reputation below 40.

### State effects
- `public_statement_truthful`: Reputation +5, Pressure -1.
- `cooperate_with_sophie`: evidence ledger disclosed; unlocks accountability ending.
- `attempt_leverage`: Pressure +2, `witness_flag = true`, relationship route closes.
- `consensual_social_connection`: optional adult relationship flag; never required for victory.

## Chapter 6 — Crisis Management
**Type:** Story-critical, 45 minutes. **Mandatory:** return to capital (morning), crisis meeting (afternoon).

### Dramatic purpose
Maria presents the evidence ledger, Sophie requests a response, and Carlos prepares a public attack. The player has to choose integrity, legal containment, or self-serving denial.

### Beats
1. Travel: messages reveal which evidence and witnesses remain active.
2. Crisis meeting: Maria establishes boundaries: no retaliation, no pressure on staff, no back-channel payments.
3. Sophie interview request: player chooses a recorded response, written statement, or counsel-mediated review.
4. Carlos leak: an edited clip tests the player's reputation and debate readiness.
5. Threshold check: `scandal_threshold_check` evaluates Pressure, evidence, witness flags, and the response chosen.

### State effects
- `accept_independent_review`: Reputation +8 over time; unlocks reform ending.
- `public_denial_contradicted_by_evidence`: Reputation -20; Pressure +2.
- `retaliation_attempt`: immediate accountability branch, no romantic/social routes.
- `staff_safety_commitment`: Maria trust +15; unlocks truthful debate support.

## Chapter 7 — Final Debate & Vote
**Type:** Sandbox/climax, 90 minutes. **Mandatory:** final debate (afternoon, TV studio), final vote (evening, parliament).

### Dramatic purpose
Every major state converges. The debate is a competence and accountability test; the vote and public response determine one of eight endings.

### Beats
1. Morning preparation: player selects debate brief, evidence response, and whether to speak to Sophie on record.
2. Optional adult social scenes: Emma, Jessica, and Olivia may appear only as independent adults with explicit, enthusiastic consent and no professional leverage; routes can remain platonic or end cleanly.
3. Final debate: choices test policy knowledge, consistency, and ownership of harm.
4. Final vote: vote outcome combines debate score, Reputation, ally support, and investigation state.
5. Ending calculation: resolve `final_ending_calculation`.

## Ending matrix
| ID | Conditions | Result |
|---|---|---|
| `reform_victory` | Reputation >= 70, debate pass, no retaliation, accepts review | Bill passes; John remains in office under oversight. |
| `qualified_victory` | Reputation 50–69, debate pass, low pressure | Bill passes narrowly; ongoing scrutiny remains. |
| `accountability_resignation` | Pressure high, evidence corroborated, truthful cooperation | John resigns and faces investigation; staff are protected. |
| `exposed_scandal` | Pressure critical or witness/evidence threshold exceeded | Public exposé ends career. |
| `institutional_reform` | Cooperation + review + staff-safety commitment | Investigation prompts wider safeguards and a reform legacy. |
| `legal_containment` | Counsel path, medium pressure, no retaliation | Career survives temporarily but investigation continues. |
| `isolated_defeat` | Reputation < 20 or debate fails decisively | Allies abandon John; vote and career are lost. |
| `private_reckoning` | Optional relationship flag plus withdrawal from public life | He leaves politics and confronts consequences privately; not a reward path. |

## Acceptance criteria
- Every chapter has a non-romantic completion route.
- Every choice with pressure or consent implications has a visibly documented state effect.
- No branch requires an adult social/romantic outcome to achieve a positive ending.
- All terminal endings are reachable and mutually exclusive.
