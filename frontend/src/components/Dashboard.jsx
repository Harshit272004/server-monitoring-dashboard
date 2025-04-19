import React, { useEffect, useState } from "react";
import AlertsSummary from "./AlertsSummary";
import MetricsChart from "./MetricsChart";
import ServerList from "./ServerList";
import api from "../api";

const Dashboard = () => {
  const [servers, setServers] = useState([]);
  const [selectedServer, setSelectedServer] = useState(null);

  useEffect(() => {
    api.get("/api/servers").then((res) => {
      setServers(res.data);
      setSelectedServer(res.data[0]?.id);
    });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Server Monitoring Dashboard</h1>
      <AlertsSummary />
      <ServerList servers={servers} setSelected={setSelectedServer} />
      {selectedServer && <MetricsChart serverId={selectedServer} />}
    </div>
  );
};

export default Dashboard;
