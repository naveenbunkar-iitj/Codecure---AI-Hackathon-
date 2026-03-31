"""Utility helpers for user-facing recommendation text."""

from __future__ import annotations


def get_recommendation(risk_tier: str) -> str:
    """Map risk tiers to practical next-step recommendations."""
    normalized = risk_tier.strip().lower()

    recommendations = {
        "high": (
            "High risk detected. Please schedule a clinical check-up soon, "
            "increase physical activity gradually, and seek smoking cessation support if applicable."
        ),
        "moderate": (
            "Moderate risk detected. Improve consistency of exercise, review diet quality, "
            "and monitor your health metrics monthly."
        ),
        "low": (
            "Low risk detected. Maintain your current healthy habits and continue regular preventive care."
        ),
    }

    return recommendations.get(
        normalized,
        "Risk tier unavailable. Consult a healthcare professional for personalized guidance.",
    )
