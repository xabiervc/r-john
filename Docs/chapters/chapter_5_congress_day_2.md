# Chapter 5 — Congress Day 2

## Purpose
Sandbox chapter: the congress vote, the evening reception and the first public signs that Sophie's investigation is gaining traction.

## Mandatory beat
- Morning: `congress_session` at `congress_hall`. R. John must cast a visible procedural vote; media, Carlos and Sophie observe the result.

## Optional routes
- Ashley: a voluntary, clearly adult social route at the reception. The scene checks for private setting, mutual interest and an explicit affirmative choice; a refusal closes the route with no penalty.
- Victoria: influencer collaboration route. Player may approve a transparent, consensual interview, decline it, or accept a risky but lawful live-stream appearance.
- Natalie: policy negotiation route. All proposals are documented and must remain lawful; any attempted quid-pro-quo is flagged as a failure-risk event rather than a reward.
- Sophie: investigation route. Player can offer on-record answers, provide verifiable documents, or refuse comment. No intimidation, bribery or sexual leverage is a valid resolution.

## State changes
- `investigation_intensifies` is set if Sophie receives corroborating evidence or R. John contradicts a public statement.
- Public vote success: reputation +8; visible evasiveness: reputation -8.
- Transparent cooperation: pressure -5; obstructive conduct: pressure +15.

## End state
Persist `congress_vote_result`, `sophie_evidence_level`, `public_statement_consistency`, and voluntary relationship flags only after an explicit consent checkpoint.
