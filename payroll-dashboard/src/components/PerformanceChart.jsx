import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { getTopPerformers } from "../services/api";
import "chart.js/auto";

export default function PerformanceChart() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getTopPerformers()
      .then(res => setData(res.data))
      .catch(err => {
        console.error("Top Performers API Error:", err);
        setError("Failed to load performance data");
      });
  }, []);

  const chartData = {
    labels: data.map(d => d.emp_name),
    datasets: [{
      label: "Top Performers",
      data: data.map(d => d.rating),
      backgroundColor: "#3b82f6"
    }]
  };

  return (
    <div style={{ height: "260px" }}>
      {error ? <p style={{color: 'red'}}>{error}</p> : <Bar data={chartData} options={{ maintainAspectRatio: false }} />}
    </div>
  );
}
