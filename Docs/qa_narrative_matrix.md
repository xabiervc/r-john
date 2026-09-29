# Narrative QA Matrix

## Core regression cases
| ID | Setup | Action | Expected result |
|---|---|---|---|
| NAR-01 | Chapter 5, no evidence | Complete congress session | Chapter can progress without any social route |
| NAR-02 | Any NPC scene | Select decline/boundary option | Scene ends respectfully; no hidden penalty |
| NAR-03 | Victoria route | Attempt political leverage | Route closes; witness flag is recorded |
| NAR-04 | Sophie lead | Choose truthful statement | Evidence ledger updates; accountability ending remains reachable |
| NAR-05 | Chapter 6 | Attempt retaliation | Immediate accountability branch; staff safety state preserved |
| NAR-06 | Chapter 7 | Debate pass, Reputation 75, no retaliation | `reform_victory` resolves |
| NAR-07 | Chapter 7 | Pressure critical | `exposed_scandal` resolves |
| NAR-08 | Chapter 7 | Reputation 10, debate failure | `isolated_defeat` resolves |
| NAR-09 | Any branch | Reload after state change | State variables and ending eligibility persist |
| NAR-10 | Accessibility | Captions enabled | Critical audio cue is captioned and state change is text-readable |

## Validation rules
1. Every dialogue node must have a unique ID.
2. Every `next` target must exist within its tree.
3. Every non-terminal node must offer at least one player choice.
4. Terminal nodes must declare a supported ending or a documented return state.
5. NPC and location IDs must resolve against canonical data files.
6. No path may reward coercion, retaliation, employment leverage, or concealment of wrongdoing.
7. Each chapter must have a reachable non-romantic path.

## Manual review gates
- Narrative consistency review against GDD and chapter configuration.
- Consent/boundaries editorial pass.
- Accessibility review for UI contrast, captions and input clarity.
- Full ending matrix playthrough after implementation.
