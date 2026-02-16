import SalaryChart from "./components/SalaryChart";
import AttendanceChart from "./components/AttendanceChart";
import PerformanceChart from "./components/PerformanceChart";
import HiringChart from "./components/HiringChart";
import "./App.css";

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>Employees Payroll System Analytics Dashboard</h1>
        <p>Payroll • Attendance • Performance • Hiring Insights</p>
      </header>

      <div className="grid">
        <div className="card">
          <h3>Department Salary Cost</h3>
          <SalaryChart />
        </div>

        <div className="card">
          <h3>Attendance Trend</h3>
          <AttendanceChart />
        </div>

        <div className="card">
          <h3>Top Performers</h3>
          <PerformanceChart />
        </div>

        <div className="card">
          <h3>Hiring Growth</h3>
          <HiringChart />
        </div>
      </div>
    </div>
  );
}
