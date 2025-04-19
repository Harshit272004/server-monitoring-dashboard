from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Alert
from fastapi.security import OAuth2PasswordBearer
from app.security import decode_access_token
from fastapi import HTTPException, status, Request

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Verify token for all alert routes
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

@router.get("/summary")
def get_alert_summary(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    critical = db.query(Alert).filter(Alert.level == "critical").count()
    medium = db.query(Alert).filter(Alert.level == "medium").count()
    low = db.query(Alert).filter(Alert.level == "low").count()

    return {
        "critical": critical,
        "medium": medium,
        "low": low
    }
