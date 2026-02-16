import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api"
});

export const getDepartmentSalary = () => API.get("/department-salary");
export const getAttendanceTrend = () => API.get("/attendance-trend");
export const getTopPerformers = () => API.get("/top-performers");
export const getHiringGrowth = () => API.get("/hiring-growth");
