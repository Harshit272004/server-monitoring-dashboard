import axios from "axios";

const api = axios.create({
  baseURL: "postgresql://postgres:qWyvHgCCMZmkPhCesYYrQuoxNaMaGkhe@mainline.proxy.rlwy.net:31562/railway", // replace with backend URL after hosting
});

// Attach token to headers
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
