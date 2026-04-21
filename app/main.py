"""
app/main.py — FastAPI application entry point.

Responsibilities:
  - Create and configure the FastAPI application instance.
  - Register CORS middleware.
  - Mount all routers.
  - Expose a health-check endpoint.
  - Run Uvicorn when executed directly (python -m app.main).
"""
import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings, setup_logging
from app.routers import company, contact, news, team

# ─── Bootstrap ────────────────────────────────────────────────────────────────
settings = get_settings()
setup_logging(settings.log_level)
logger = logging.getLogger(__name__)

# ─── Application factory ──────────────────────────────────────────────────────
app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    description=(
        "REST API cho dự án SGOD — Smart Generation of Digital.\n\n"
        "Cung cấp dữ liệu cho các section: News Slider, Blog, Team, Contact."
    ),
    docs_url="/docs",        # Swagger UI  → http://127.0.0.1:8000/docs
    redoc_url="/redoc",      # ReDoc UI    → http://127.0.0.1:8000/redoc
    openapi_url="/openapi.json",
)

# ─── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,   # e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

logger.info(
    "CORS configured for origins: %s",
    settings.origins_list,
)

# ─── Routers ──────────────────────────────────────────────────────────────────
app.include_router(company.router)
app.include_router(news.router)
app.include_router(team.router)
app.include_router(contact.router)


# ─── Health check ─────────────────────────────────────────────────────────────
@app.get("/health", tags=["System"], summary="Health check")
def health_check() -> dict:
    """Quick liveness probe — returns OK when the server is running."""
    return {
        "status": "ok",
        "app": settings.app_title,
        "version": settings.app_version,
        "env": settings.app_env,
    }


# ─── Dev runner ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    logger.info(
        "Starting %s v%s on %s:%d",
        settings.app_title,
        settings.app_version,
        settings.host,
        settings.port,
    )
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.app_env == "development",
        log_level=settings.log_level.lower(),
    )
