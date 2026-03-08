# Sentiment Analyzer

A full-stack application that analyzes public sentiment about any topic using recent news articles and a transformer-based NLP model.

The system collects news articles related to a query, classifies their sentiment, aggregates the results, and displays them in an interactive dashboard.

## Features

- Search sentiment for **any topic**
- Automatic **news collection**
- **Transformer-based sentiment classification**
- Sentiment **distribution visualization**
- **Sentiment timeline** over time
- Example classified sentences

## Tech Stack

Frontend:
- React
- Vite
- Recharts

Backend:
- FastAPI
- Python

NLP:
- HuggingFace Transformers
- `cardiffnlp/twitter-roberta-base-sentiment-latest`

Data Source:
- NewsAPI

## Project Structure

```
project-root
│
├── frontend
│   └── sentiment-ui
│
├── backend
│   ├── routes
│   ├── services
│   └── app.py
│
├── scraping
│
├── models
│
├── processing
│
└── tests
```

## API

Main endpoint:

```
POST /analyze
```

Example request:

```json
{
  "query": "Tesla",
  "pages": 1
}
```

Example response:

```json
{
  "query": "Tesla",
  "total_texts": 40,
  "positive": 18,
  "neutral": 12,
  "negative": 10
}
```

## Requirements

- Python 3.10+
- Node.js 20+
- npm
- NewsAPI key

Get a free API key:

```
https://newsapi.org
```

Create a `.env` file in the project root:

```
NEWS_API_KEY=your_key_here
```

## Running the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer
```

### 2. Backend setup

Create a virtual environment:

```
python -m venv .venv
```

Activate it (Linux / WSL):

```
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Start the backend:

```
uvicorn backend.app:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

### 3. Frontend setup

Go to the frontend directory:

```
cd frontend/sentiment-ui
```

Install dependencies:

```
npm install
```

Start the development server:

```
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

## Usage

1. Open the frontend in your browser  
2. Enter a topic (e.g. **Tesla**, **Bitcoin**, **OpenAI**)  
3. Click **Analyze**

The system will collect news articles, classify sentiment, and display the results in the dashboard.

## License

MIT