# Sentiment Analyzer

A full-stack application that analyzes public sentiment about any topic using recent news data and a transformer-based NLP model.

The system collects relevant texts, classifies their sentiment using a pretrained model, aggregates the results, and displays them in an interactive dashboard.

---

## 🚀 Features

- Search sentiment for any topic
- Automatic data collection
- Transformer-based sentiment analysis (Hugging Face)
- Sentiment distribution visualization
- Sentiment timeline over time
- Weighted sentiment scoring (-1 to +1)
- Example classified sentences
- Loading state handling (backend cold start awareness)

---

## 🧱 Tech Stack

Frontend:
- React
- Vite
- Recharts

Backend:
- FastAPI
- Python

NLP:
- Hugging Face Inference API
- cardiffnlp/twitter-roberta-base-sentiment-latest

Data Source:
- NewsAPI

---

## 📁 Project Structure

project-root
│
├── frontend/
│   └── sentiment-ui/
│
├── backend/
│   ├── routes/
│   ├── services/
│   └── app.py
│
├── scraping/
├── models/
├── processing/
└── tests/

---

## 🔌 API

Main endpoint:

POST /analyze

Example request:

{
  "query": "Tesla",
  "pages": 1
}

Example response:

{
  "query": "Tesla",
  "total_texts": 40,
  "positive": 18,
  "neutral": 12,
  "negative": 10,
  "overall_score": 0.34,
  "timeline": [
    {
      "date": "2026-03-27",
      "avg_score": 0.21
    }
  ]
}

---

## ⚙️ Requirements

- Python 3.10+
- Node.js 18+
- npm

---

## 🔑 Environment Variables

Create a .env file in the project root:

NEWS_API_KEY=your_newsapi_key
HF_API_KEY=your_huggingface_token

---

## 🔗 Get API Keys

NewsAPI: https://newsapi.org  
Hugging Face: https://huggingface.co/settings/tokens  

---

## ▶️ Running the Project

1. Clone the repository

git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer

---

2. Backend setup

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app:app --reload

Backend runs at:
http://127.0.0.1:8000

---

3. Frontend setup

cd frontend/sentiment-ui
npm install
npm run dev

Frontend runs at:
http://localhost:5173

---

## 🔗 Connecting Frontend and Backend

Make sure the API URL in App.jsx matches your backend:

Local:
const API_URL = "http://127.0.0.1:8000";

Production:
const API_URL = "https://your-backend.onrender.com";

---

## 🌐 Deployment

Frontend: Vercel  
Backend: Render  

Note: Render free tier may take ~20 seconds to wake up on first request.

---

## 🧠 How It Works

1. User enters a topic  
2. Backend collects related texts  
3. Hugging Face model predicts sentiment probabilities  
4. System computes a weighted sentiment score  
5. Results are aggregated  
6. Frontend visualizes the data  

---

## 📊 Sentiment Scoring

score = positive - negative

- Range: -1 to +1  
- More accurate than simple classification  
- Enables smoother trends and better insights  

---

## 📝 License

MIT