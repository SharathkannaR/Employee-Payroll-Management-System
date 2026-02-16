import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { getHiringGrowth } from "../services/api";
import "chart.js/auto";

export default function HiringChart() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getHiringGrowth()
      .then(res => setData(res.data))
      .catch(err => {
        console.error("Hiring Growth API Error:", err);
        setError("Failed to load hiring data");
      });
  }, []);

  const chartData = {
    labels: data.map(d => d.month),
    datasets: [{
      label: "Hiring Growth",
      data: data.map(d => d.hires),
      borderColor: "#3b82f6",
      backgroundColor: "rgba(59, 130, 246, 0.1)"
    }]
  };

  return (
    <div style={{ height: "260px" }}>
      {error ? <p style={{color: 'red'}}>{error}</p> : <Line data={chartData} options={{ maintainAspectRatio: false }} />}
    </div>
  );
}
