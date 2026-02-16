import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { getAttendanceTrend } from "../services/api";
import "chart.js/auto";

export default function AttendanceChart() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAttendanceTrend()
      .then(res => setData(res.data))
      .catch(err => {
        console.error("Attendance API Error:", err);
        setError("Failed to load attendance data");
      });
  }, []);

  const chartData = {
    labels: data.map(d => d.attendance_date),
    datasets: [{
      label: "Daily Attendance",
      data: data.map(d => d.present),
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
