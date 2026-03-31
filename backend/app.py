from flask import Flask, request, jsonify

from model import predict_risk
from utils import get_recommendation

app = Flask(__name__)


@app.route('/')
def home():
    return "HealthCure AI Backend Running"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}

    age = data.get('age')
    weight = data.get('weight')
    exercise = data.get('exercise')
    smoking = data.get('smoking')

    risk = predict_risk(age, weight, exercise, smoking)
    advice = get_recommendation(risk)

    return jsonify({
        "risk": risk,
        "advice": advice
    })


if __name__ == '__main__':
    app.run(debug=True)
