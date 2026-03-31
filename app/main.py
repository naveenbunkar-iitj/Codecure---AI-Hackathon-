"""CLI entrypoint for the health-risk prototype."""

from __future__ import annotations

from app.model import predict_risk
from app.utils import get_recommendation


def _ask_int(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue
        return value


def _ask_float(prompt: str, min_value: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        return value


def _ask_smoking_status(prompt: str) -> str:
    accepted = {"yes", "no", "y", "n"}
    while True:
        value = input(prompt).strip().lower()
        if value in accepted:
            return "yes" if value in {"yes", "y"} else "no"
        print("Please enter yes or no.")


def main() -> None:
    print("=== Health Risk Prototype CLI ===")
    age = _ask_int("Enter age (years): ", min_value=1, max_value=120)
    weight = _ask_float("Enter weight (kg): ", min_value=1)
    exercise_days = _ask_int("Exercise days per week (0-7): ", min_value=0, max_value=7)
    smoking_status = _ask_smoking_status("Do you currently smoke? (yes/no): ")

    risk_tier, score = predict_risk(age, weight, exercise_days, smoking_status)
    recommendation = get_recommendation(risk_tier)

    print("\n=== Prediction Result ===")
    print(f"Risk Tier: {risk_tier}")
    print(f"Risk Score: {score}")
    print(f"Recommendation: {recommendation}")


if __name__ == "__main__":
    main()
