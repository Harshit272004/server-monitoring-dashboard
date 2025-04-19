from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Metric, Server
from fastapi.security import OAuth2PasswordBearer
from app.security import decode_access_token
from typing import List
from datetime import datetime, timedelta

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

@router.get("/usage/{server_id}")
def get_server_metrics(
    server_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")

    metrics = (
        db.query(Metric)
        .filter(Metric.server_id == server_id)
        .order_by(Metric.timestamp.asc())
        .limit(24)
        .all()
    )

    data = [
        {
            "timestamp": m.timestamp,
            "cpu": m.cpu_usage,
            "ram": m.ram_usage,
            "disk": m.disk_usage,
            "app": m.app_usage
        }
        for m in metrics
    ]

    return {"server": server.name, "metrics": data}
