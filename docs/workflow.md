# Prototype Workflow

1. User runs the CLI (`python -m app.main`).
2. CLI collects four inputs:
   - age
   - weight
   - exercise days per week
   - smoking status
3. `app.model.predict_risk(...)` computes a deterministic baseline score and risk tier.
4. `app.utils.get_recommendation(...)` maps the tier to actionable guidance.
5. CLI prints the tier, score, and recommendation.
