import React, { useEffect, useState } from "react";
import api from "../api";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

const MetricsChart = ({ serverId }) => {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    api.get(`/api/metrics/usage/${serverId}`).then((res) => {
      setMetrics(res.data.metrics.map((m) => ({
        ...m,
        timestamp: new Date(m.timestamp).toLocaleTimeString()
      })));
    });
  }, [serverId]);

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Usage Graphs</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={metrics}>
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="cpu" stroke="#8884d8" />
          <Line type="monotone" dataKey="ram" stroke="#82ca9d" />
          <Line type="monotone" dataKey="disk" stroke="#ff7300" />
          <Line type="monotone" dataKey="app" stroke="#f44336" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default MetricsChart;
