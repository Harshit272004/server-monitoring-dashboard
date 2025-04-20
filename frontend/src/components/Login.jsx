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


import React, { useEffect } from "react";
import api from "../api";
import { login } from "../auth";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const loginUser = async () => {
      try {
        // Call the /login endpoint
        const res = await api.post("/auth/login");
        login(res.data.access_token); // Store the token in local storage or context
        navigate("/"); // Redirect to the main page
      } catch (err) {
        console.error("Login failed", err);
      }
    };

    loginUser(); // Automatically log in the user when the page is loaded
  }, [navigate]);

  return (
    <div style={{ padding: "50px", maxWidth: "400px", margin: "auto" }}>
      <h2>Logging in...</h2> {/* Display a loading message */}
    </div>
  );
};

export default Login;


