from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Server
from fastapi.security import OAuth2PasswordBearer
from app.security import decode_access_token
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

@router.get("/", summary="Get all servers")
def get_servers(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    servers = db.query(Server).all()
    return [
        {
            "id": s.id,
            "name": s.name,
            "ip_address": s.ip_address,
            "status": s.status
        }
        for s in servers
    ]
