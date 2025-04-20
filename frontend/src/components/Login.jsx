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

    // Check if in development mode
    const devMode = process.env.REACT_APP_ENV_MODE === "development";

    if (devMode) {
      // Skip login and simulate successful login in dev mode
      const response = {
        data: {
          access_token: "fake_token_for_dev_mode", // Fake token
          token_type: "bearer",
          role: "user"
        }
      };
      login(response.data.access_token); // Store fake token
      navigate("/"); // Redirect to home
    } else {
      try {
        const res = await api.post("/auth/login", new URLSearchParams(form)); // Normal login in prod mode
        login(res.data.access_token);
        navigate("/");
      } catch (err) {
        setError("Invalid credentials");
      }
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

export default Login;

