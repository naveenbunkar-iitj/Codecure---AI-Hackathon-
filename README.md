# Codecure AI Hackathon Prototype

This repository contains a simple, deterministic command-line prototype for baseline health risk triage.

## Project Structure

- `app/main.py` — CLI entrypoint and input handling.
- `app/model.py` — deterministic baseline scoring logic.
- `app/utils.py` — recommendation mapping by risk tier.
- `data/sample_data.csv` — tiny sample dataset for quick testing.
- `docs/workflow.md` — end-to-end execution flow.
- `requirements.txt` — dependency file (none required).

## Quick Start

1. Ensure Python 3.10+ is available.
2. Run the CLI from repository root:

```bash
python -m app.main
```

3. Enter prompted values:
   - age
   - weight
   - exercise days per week
   - smoking status (`yes`/`no`)

You will receive a risk tier (`Low`, `Moderate`, or `High`) and a recommendation.

## Notes

- This is a baseline deterministic heuristic for prototyping only.
- It is not a medical device and should not be used for clinical decision-making.
