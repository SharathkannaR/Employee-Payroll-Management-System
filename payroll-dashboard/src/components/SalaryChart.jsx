import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { getDepartmentSalary } from "../services/api";
import "chart.js/auto";

export default function SalaryChart() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    getDepartmentSalary()
      .then(res => setData(res.data))
      .catch(err => {
        console.error("Department Salary API Error:", err);
        setError("Failed to load salary data");
      });
  }, []);

  const chartData = {
    labels: data.map(d => d.dept_name),
    datasets: [{
      label: "Department Salary Cost",
      data: data.map(d => d.total_salary),
      backgroundColor: "#3b82f6"
    }]
  };

  return (
    <div style={{ height: "260px" }}>
      {error ? <p style={{color: 'red'}}>{error}</p> : <Bar data={chartData} options={{ maintainAspectRatio: false }} />}
    </div>
  );
}
