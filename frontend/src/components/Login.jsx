/*commented for temporary login once the login part will be fixed by me i will uncomment it again
import React, { useState } from "react";
import api from "../api";
import { login } from "../auth";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [form, setForm] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/auth/login", new URLSearchParams(form));
      login(res.data.access_token);
      navigate("/");
    } catch (err) {
      setError("Invalid credentials");
    }
  };

  return (
    <div style={{ padding: "50px", maxWidth: "400px", margin: "auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input name="username" placeholder="Username" onChange={handleChange} required />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
        <button type="submit">Login</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
};

export default Login;*/
import React, { useState, useEffect } from "react";
import { login } from "../auth"; // Assuming the login function is in auth.js
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Login = () => {
  const [form, setForm] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    // Check if in development mode to bypass login
    if (process.env.REACT_APP_ENV_MODE === "development") {
      const fakeToken = "sample-hardcoded-token";  // Fake token for dev mode
      login(fakeToken);  // Automatically log in
      navigate("/");  // Redirect to the home page or the page you want
    }
  }, [navigate]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (process.env.REACT_APP_ENV_MODE !== "development") {
      try {
        const apiUrl = import.meta.env.VITE_API_BASE_URL;
        const res = await axios.post(`${apiUrl}/auth/login`, new URLSearchParams(form));
        login(res.data.access_token);
        navigate("/");  // Redirect to the home page or the page you want
      } catch (err) {
        setError("Invalid credentials");
      }
    }
  };

  return (
    <div style={{ padding: "50px", maxWidth: "400px", margin: "auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Username"
          onChange={handleChange}
          required
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Login</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
};

export default Login;
