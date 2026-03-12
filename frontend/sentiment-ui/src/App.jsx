import { useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid
} from "recharts";

import "./index.css";

const API_URL = "https://analise-de-sentimento-automatica-asa.onrender.com";

const COLORS = ["#22c55e", "#9ca3af", "#ef4444"];

function App() {

  const [query, setQuery] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {

    if (!query) return;

    setLoading(true);

    const res = await fetch(`${API_URL}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: query,
        pages: 1
      })
    });

    const result = await res.json();

    setData(result);
    setLoading(false);
  };

  const getVerdict = () => {

    if (!data) return "";

    if (data.positive > data.negative) return "Overall Positive Sentiment";
    if (data.negative > data.positive) return "Overall Negative Sentiment";

    return "Mostly Neutral Sentiment";
  };

  const chartData = data
    ? [
        { name: "Positive", value: data.positive },
        { name: "Neutral", value: data.neutral },
        { name: "Negative", value: data.negative }
      ]
    : [];

  return (

    <div className="app-container">

      {/* HERO HEADER */}

      <div className="hero">

        <h1 className="hero-title">
          Sentiment Analyzer
        </h1>

        <p className="hero-subtitle">
          Monitor public sentiment for any topic
        </p>

        <div className="search-bar">

          <input
            className="search-input"
            placeholder="Search a company, brand, person..."
            value={query}
            onChange={(e)=>setQuery(e.target.value)}
            onKeyDown={(e)=>{
              if(e.key === "Enter"){
                analyze();
              }
            }}
          />

          <button
            className="search-button"
            onClick={analyze}
          >
            Analyze
          </button>

        </div>

        {/* Suggestions */}

        <div className="suggestions">
          Try:
          <span onClick={()=>setQuery("Tesla")}> Tesla</span>
          <span onClick={()=>setQuery("Apple")}> Apple</span>
          <span onClick={()=>setQuery("Bitcoin")}> Bitcoin</span>
          <span onClick={()=>setQuery("OpenAI")}> OpenAI</span>
        </div>

      </div>

      {loading && (
        <p style={{textAlign:"center"}}>
          Analyzing sentiment...
        </p>
      )}

      {/* DASHBOARD */}

      {data && (

        <div className="grid">

          {/* PIE CHART */}

          <div className="card">

            <div className="card-title">
              Sentiment Distribution
            </div>

            <div className="card-content chart-center">

              <PieChart width={350} height={300}>
                <Pie
                  data={chartData}
                  dataKey="value"
                  outerRadius={110}
                >
                  {chartData.map((entry, index) => (
                    <Cell key={index} fill={COLORS[index]} />
                  ))}
                </Pie>

                <Tooltip />

              </PieChart>

            </div>

          </div>

          {/* SUMMARY */}

          <div className="card">

            <div className="card-title">
              Summary
            </div>

            <div className="card-content">

              <p>Total texts analyzed: <b>{data.total_texts}</b></p>

              <p>Positive: {data.positive}</p>

              <p>Neutral: {data.neutral}</p>

              <p>Negative: {data.negative}</p>

              <h3>Verdict</h3>

              <p className="verdict">
                {getVerdict()}
              </p>

            </div>

          </div>

        </div>

      )}

      {/* TIMELINE */}

      {data && data.timeline && (

        <div className="card timeline-card">

          <div className="card-title">
            Sentiment Over Time
          </div>

          <div className="card-content chart-center">

            <LineChart
              width={900}
              height={350}
              data={data.timeline}
            >

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="date" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="positive"
                stroke="#22c55e"
                strokeWidth={2}
              />

              <Line
                type="monotone"
                dataKey="neutral"
                stroke="#9ca3af"
                strokeWidth={2}
              />

              <Line
                type="monotone"
                dataKey="negative"
                stroke="#ef4444"
                strokeWidth={2}
              />

            </LineChart>

          </div>

        </div>

      )}

      {/* EXAMPLES */}

      {data && (

        <div className="card examples-card">

          <div className="card-title">
            Example Sentences
          </div>

          <div className="card-content">

            <ul>
              {data.results.slice(0,10).map((r,i)=>(
                <li key={i}>
                  {r.text} → <b>{r.sentiment}</b>
                </li>
              ))}
            </ul>

          </div>

        </div>

      )}

    </div>

  );
}

export default App;