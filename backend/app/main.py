from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from slowapi import Limiter

from app.routes import alerts, metrics, servers
from app.auth import auth_router
from app.audit import create_audit_log

app = FastAPI(
    title="Server Monitoring Dashboard",
    description="A secure server monitoring app built with FastAPI",
    version="1.0"
)

# Rate limiter setup
limiter = Limiter(key_func=lambda request: request.client.host)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Enable CORS (frontend will run on a different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware: Audit logging
@app.middleware("http")
async def audit_log_middleware(request, call_next):
    response = await call_next(request)
    await create_audit_log(request)
    return response

# Register all routes
app.include_router(auth_router, prefix="/auth")
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["Metrics"])
app.include_router(servers.router, prefix="/api/servers", tags=["Servers"])
