from sqlalchemy.orm import Session
from .models import AuditLog
from .main import SessionLocal
from datetime import datetime

async def create_audit_log(request):
    db: Session = SessionLocal()
    try:
        log = AuditLog(
            user="Anonymous",
            action=request.method,
            endpoint=request.url.path,
            timestamp=datetime.utcnow()
        )
        db.add(log)
        db.commit()
    except Exception as e:
        print(f"[Audit Error] {e}")
    finally:
        db.close()
