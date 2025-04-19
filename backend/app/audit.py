from app.models import AuditLog
from app.database import get_db
from fastapi import Request
from sqlalchemy.orm import Session
import jwt
import os
from datetime import datetime

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

async def create_audit_log(request: Request):
    db: Session = next(get_db())
    auth_header = request.headers.get("authorization")
    user = "Anonymous"

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            user = payload.get("sub", "Unknown")
        except Exception:
            pass

    audit = AuditLog(
        user=user,
        action=request.method,
        endpoint=request.url.path,
        timestamp=datetime.utcnow()
    )

    db.add(audit)
    db.commit()
