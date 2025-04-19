from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# USER TABLE (for login & role-based access)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="viewer")  # "admin" or "viewer"

# SERVER TABLE
class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    status = Column(String)  # online/offline

    metrics = relationship("Metric", back_populates="server")
    alerts = relationship("Alert", back_populates="server")
    traffic = relationship("NetworkTraffic", back_populates="server")

# METRICS TABLE
class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    cpu_usage = Column(Float)
    ram_usage = Column(Float)
    disk_usage = Column(Float)
    app_usage = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    server = relationship("Server", back_populates="metrics")

# ALERTS TABLE
class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    level = Column(String)  # critical, medium, low
    message = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    server = relationship("Server", back_populates="alerts")

# NETWORK TRAFFIC TABLE
class NetworkTraffic(Base):
    __tablename__ = "network_traffic"
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    incoming_traffic = Column(Float)  # Mbps
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    server = relationship("Server", back_populates="traffic")

# models.py

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    action = Column(String)
    endpoint = Column(String)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

