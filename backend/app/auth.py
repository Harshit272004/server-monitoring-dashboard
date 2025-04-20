from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.security import create_access_token
import os

auth_router = APIRouter()

@auth_router.post("/login")
def login(db: Session = Depends(get_db)):
    # Skip the login verification for development mode
    if os.getenv("ENV_MODE", "development") == "development":
        # Directly return a token without checking credentials
        token = create_access_token({"sub": "guest", "role": "user"})
        return {"access_token": token, "token_type": "bearer", "role": "user"}

    # Comment out or remove the authentication logic for now
    # Example code below is commented out
    # user = db.query(models.User).filter(models.User.username == form_data.username).first()
    # if not user or not verify_password(form_data.password, user.hashed_password):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invalid username or password",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )

    # Temporarily allow direct access by skipping the token generation
    token = create_access_token({"sub": "guest", "role": "user"})
    return {"access_token": token, "token_type": "bearer", "role": "user"}

