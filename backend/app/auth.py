from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import models
from app.database import get_db
from app.security import create_access_token
import os

auth_router = APIRouter()

@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Check if we are in development mode
    if os.getenv("ENV_MODE", "development") == "development":
        # Skip authentication and directly return a token for development
        token = create_access_token({"sub": "guest", "role": "user"})
        return {"access_token": token, "token_type": "bearer", "role": "user"}

    # Normal authentication process (will happen in production mode)
    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer", "role": user.role}
