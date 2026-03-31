def predict_risk(age, weight, exercise, smoking):
    score = 0

    if age > 50:
        score += 2
    if weight > 80:
        score += 2
    if exercise < 2:
        score += 2
    if smoking == 1:
        score += 3

    if score <= 2:
        return "Low"
    elif score <= 5:
        return "Medium"
    else:
        return "High"
