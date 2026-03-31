# HealthCure AI 🏥

## Overview
HealthCure AI is a HealthTech prototype that predicts user health risks based on lifestyle inputs and provides preventive recommendations.

## Features
- Health risk prediction (Low/Medium/High)
- Personalized suggestions
- Simple web interface
- Scalable backend API

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)

## Updated Folder Structure
```text
healthcure-ai/
├── backend/
│   ├── app.py
│   ├── model.py
│   └── utils.py
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── requirements.txt
└── README.md
```

## Installation & Run

### 1) Start backend
```bash
cd backend
pip install -r ../requirements.txt
python app.py
```

### 2) Open frontend
Open `frontend/index.html` in your browser.

## Workflow
User Input → Flask API → Risk Model → Recommendation → UI Output

## Future Scope
- AI/ML model integration
- Wearable device data
- Doctor consultation system
- React dashboard UI
- Cloud deployment on Render / Vercel

## Author
Naveen
