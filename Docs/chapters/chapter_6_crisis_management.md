# Chapter 6 — Crisis Management

## Purpose
Story-critical crisis chapter after the congress. The player responds to an investigation without using coercion, intimidation or evidence tampering.

## Mandatory beats
- Morning: `return_to_capital` travel sequence.
- Afternoon: `crisis_meeting` in the office with Maria, Sophie's published leads and Carlos's public challenge.

## Decision routes
1. **Accountability:** issue a truthful statement, release relevant records, cooperate with independent review. Short-term reputation cost; long-term pressure reduction.
2. **Legal process:** retain counsel, provide a narrow factual response and preserve evidence. Neutral immediate effect; outcome depends on consistency.
3. **Deflection:** attempt a policy-focused response. Only succeeds when facts already support it; contradictions increase pressure.

## Failure gates
- `scandal_threshold_check` triggers if pressure >= 81 or documented contradictions >= 3.
- Any attempt to coerce, bribe, threaten, delete or destroy evidence routes directly to an accountability-loss branch.

## End state
Set `crisis_strategy`, `evidence_preserved`, `statement_truthfulness`, `maria_trust`, `sophie_evidence_level`, and `pressure_band`.
