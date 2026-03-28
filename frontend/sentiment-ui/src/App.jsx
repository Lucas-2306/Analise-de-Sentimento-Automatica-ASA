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

const API_URL = "http://127.0.0.1:8000"; // change to Render when deploying

const COLORS = ["#22c55e", "#9ca3af", "#ef4444"];

function App() {

  const [query, setQuery] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {

    if (!query) return;

    setLoading(true);

    try {
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

    } catch (err) {
      console.error("Error:", err);
    }

    setLoading(false);
  };

  // 🔥 UPDATED VERDICT
  const getVerdict = () => {

    if (!data) return "";

    if (data.overall_score > 0.2) return "Highly Positive Sentiment";
    if (data.overall_score < -0.2) return "Highly Negative Sentiment";
    if (data.overall_score > 0.1) return "Overall Positive Sentiment";
    if (data.overall_score < -0.1) return "Overall Negative Sentiment";

    return "Mostly Neutral Sentiment";
  };

  const getVerdictColor = () => {
    if (!data) return "#000";
    if (data.overall_score > 0.1) return "#22c55e";
    if (data.overall_score < -0.1) return "#ef4444";
    return "#9ca3af";
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

      {/* HERO */}

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

        <div className="suggestions">
          Try:
          <span onClick={()=>setQuery("Tesla")}> Tesla</span>
          <span onClick={()=>setQuery("Apple")}> Apple</span>
          <span onClick={()=>setQuery("Bitcoin")}> Bitcoin</span>
          <span onClick={()=>setQuery("OpenAI")}> OpenAI</span>
        </div>

      </div>

      {/* 🔥 LOADING UI (NEW) */}

      {loading && (
        <div style={{
          textAlign: "center",
          marginTop: "40px"
        }}>

          <div style={{
            width: "50px",
            height: "50px",
            border: "5px solid #e5e7eb",
            borderTop: "5px solid #2563eb",
            borderRadius: "50%",
            margin: "0 auto",
            animation: "spin 1s linear infinite"
          }} />

          <p style={{ marginTop: "15px", fontWeight: "600" }}>
            Analyzing sentiment...
          </p>

          <p style={{ fontSize: "14px", color: "#6b7280" }}>
            First request may take a minute (server waking up)
          </p>

        </div>
      )}

      {/* DASHBOARD */}

      {data && !loading && (

        <div className="grid">

          {/* PIE */}

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

              <p>
                Sentiment Score: <b>{data.overall_score.toFixed(2)}</b>
              </p>

              {/* SCORE BAR */}

              <div style={{
                height: "10px",
                background: "#e5e7eb",
                borderRadius: "10px",
                overflow: "hidden",
                marginTop: "10px"
              }}>
                <div style={{
                  width: `${(data.overall_score + 1) * 50}%`,
                  background: "#2563eb",
                  height: "100%"
                }} />
              </div>

              <h3>Verdict</h3>

              <p className="verdict" style={{color: getVerdictColor()}}>
                {getVerdict()}
              </p>

            </div>

          </div>

        </div>

      )}

      {/* TIMELINE */}

      {data && data.timeline && !loading && (

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

              <Line type="monotone" dataKey="positive" stroke="#22c55e" strokeWidth={2} />
              <Line type="monotone" dataKey="neutral" stroke="#9ca3af" strokeWidth={2} />
              <Line type="monotone" dataKey="negative" stroke="#ef4444" strokeWidth={2} />

              {/* 🔥 avg score */}
              <Line
                type="monotone"
                dataKey="avg_score"
                stroke="#2563eb"
                strokeWidth={3}
              />

            </LineChart>

          </div>

        </div>

      )}

      {/* EXAMPLES */}

      {data && !loading && (

        <div className="card examples-card">

          <div className="card-title">
            Example Sentences
          </div>

          <div className="card-content">

            <ul>
              {data.results.slice(0,10).map((r,i)=>(
                <li key={i}>
                  {r.text} → <b>{r.sentiment}</b> ({r.score.toFixed(2)})
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