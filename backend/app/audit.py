from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from .models import Base, AuditLog

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Automatically create tables (like audit_logs) on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Server Monitoring Dashboard",
    description="A secure server monitoring app built with FastAPI",
    version="1.0"
)

# CORS setup (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware to create audit log
@app.middleware("http")
async def audit_log_middleware(request: Request, call_next):
    from .audit import create_audit_log
    response = await call_next(request)
    await create_audit_log(request)
    return response

@app.get("/")
def read_root():
    return {"message": "Server Monitoring App is Running!"}
