import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login.jsx";
import Dashboard from "./components/Dashboard.jsx";
import { isAuthenticated } from "./auth";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={isAuthenticated() ? <Dashboard /> : <Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
};

export default App;
