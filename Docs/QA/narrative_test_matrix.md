# Narrative QA Matrix

| ID | Scenario | Expected result |
|---|---|---|
| NAR-01 | NPC declines invitation | Route ends respectfully; no NPC penalty or retaliation |
| NAR-02 | NPC withdraws consent | Scene ends immediately; relationship flag remains false |
| NAR-03 | Player makes public statement contradicted by evidence | Pressure increases and Sophie evidence path unlocks |
| NAR-04 | Player cooperates with review | Evidence preserved; pressure decreases after verification |
| NAR-05 | Player attempts bribery/threat/evidence deletion | Accountability-loss gate; no success reward |
| NAR-06 | Final debate with high preparation and consistency | Debate score increases |
| NAR-07 | Final vote with low coalition trust | Vote support decreases |
| NAR-08 | All ending inputs set | Exactly one ending family resolves |
| NAR-09 | All dialogue JSON files parse | Validator returns success |
| NAR-10 | Every dialogue node is reachable or deliberately marked | No accidental orphan nodes |
