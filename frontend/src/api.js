import axios from "axios";

const api = axios.create({
  baseURL: "https://monitoring-backend-siuy.onrender.com", // replace with backend URL after hosting
});

// Attach token to headers
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
