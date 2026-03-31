"""Deterministic baseline risk scoring model."""

from __future__ import annotations


def predict_risk(age: int, weight: float, exercise_days: int, smoking_status: str) -> tuple[str, float]:
    """Predict a baseline health risk tier and normalized score.

    The scoring is intentionally deterministic and simple for prototype usage.

    Args:
        age: Age in years.
        weight: Weight in kilograms.
        exercise_days: Number of exercise days per week (0-7).
        smoking_status: One of "yes"/"no" (case-insensitive).

    Returns:
        A tuple of (risk_tier, score) where score is from 0.0 to 1.0.
    """
    score = 0.0

    # Age contribution
    if age >= 60:
        score += 0.35
    elif age >= 45:
        score += 0.25
    elif age >= 30:
        score += 0.15
    else:
        score += 0.05

    # Weight contribution (kg)
    if weight >= 100:
        score += 0.30
    elif weight >= 85:
        score += 0.20
    elif weight >= 70:
        score += 0.10
    else:
        score += 0.05

    # Exercise contribution (lower activity increases risk)
    if exercise_days <= 1:
        score += 0.25
    elif exercise_days <= 3:
        score += 0.15
    elif exercise_days <= 5:
        score += 0.08
    else:
        score += 0.03

    # Smoking contribution
    if smoking_status.strip().lower() in {"yes", "y", "true", "1"}:
        score += 0.30
    else:
        score += 0.05

    # Clamp final score
    score = max(0.0, min(score, 1.0))

    if score >= 0.75:
        tier = "High"
    elif score >= 0.45:
        tier = "Moderate"
    else:
        tier = "Low"

    return tier, round(score, 2)
