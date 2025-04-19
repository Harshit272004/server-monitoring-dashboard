import React, { useEffect, useState } from "react";
import api from "../api";

const AlertsSummary = () => {
  const [counts, setCounts] = useState({ critical: 0, medium: 0, low: 0 });

  useEffect(() => {
    api.get("/api/alerts/summary").then((res) => setCounts(res.data));
  }, []);

  return (
    <div style={{ display: "flex", gap: "20px", margin: "20px 0" }}>
      <div style={{ background: "#f44336", color: "white", padding: "10px", borderRadius: "8px" }}>
        Critical: {counts.critical}
      </div>
      <div style={{ background: "#ff9800", color: "white", padding: "10px", borderRadius: "8px" }}>
        Medium: {counts.medium}
      </div>
      <div style={{ background: "#4caf50", color: "white", padding: "10px", borderRadius: "8px" }}>
        Low: {counts.low}
      </div>
    </div>
  );
};

export default AlertsSummary;
