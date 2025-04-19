import React from "react";

const ServerList = ({ servers, setSelected }) => {
  return (
    <div>
      <h3>Servers:</h3>
      <ul>
        {servers.map((s) => (
          <li
            key={s.id}
            style={{ cursor: "pointer", margin: "5px 0" }}
            onClick={() => setSelected(s.id)}
          >
            {s.name} - {s.status} ({s.ip_address})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ServerList;
