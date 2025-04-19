from app.models import User, Server, Metric, Alert, NetworkTraffic
from app.security import hash_password
from app.database import SessionLocal
from datetime import datetime, timedelta
import random

db = SessionLocal()

def create_mock_data():
    # USERS
    if not db.query(User).first():
        admin = User(username="admin", hashed_password=hash_password("admin123"), role="admin")
        viewer = User(username="viewer", hashed_password=hash_password("viewer123"), role="viewer")
        db.add_all([admin, viewer])
        db.commit()
        print("✅ Created default users: admin / viewer")

    # SERVERS
    for i in range(1, 6):
        server = Server(
            name=f"Server-{i}",
            ip_address=f"192.168.0.{i}",
            status=random.choice(["online", "offline"])
        )
        db.add(server)
    db.commit()
    print("✅ Inserted mock servers")

    # METRICS
    servers = db.query(Server).all()
    for server in servers:
        for _ in range(24):  # 24 timestamps
            metric = Metric(
                server_id=server.id,
                cpu_usage=random.uniform(10, 90),
                ram_usage=random.uniform(20, 95),
                disk_usage=random.uniform(30, 85),
                app_usage=random.uniform(15, 75),
                timestamp=datetime.utcnow() - timedelta(minutes=random.randint(0, 1440))
            )
            db.add(metric)
    db.commit()
    print("✅ Inserted mock CPU/RAM/Disk metrics")

    # ALERTS
    for server in servers:
        for _ in range(5):
            alert = Alert(
                server_id=server.id,
                level=random.choice(["critical", "medium", "low"]),
                message="Sample alert message",
                timestamp=datetime.utcnow() - timedelta(minutes=random.randint(0, 500))
            )
            db.add(alert)
    db.commit()
    print("✅ Inserted mock alerts")

    # NETWORK TRAFFIC
    for server in servers:
        for _ in range(24):
            traffic = NetworkTraffic(
                server_id=server.id,
                incoming_traffic=random.uniform(10, 1000),  # Mbps
                timestamp=datetime.utcnow() - timedelta(minutes=random.randint(0, 1440))
            )
            db.add(traffic)
    db.commit()
    print("✅ Inserted mock network traffic")

if __name__ == "__main__":
    create_mock_data()
