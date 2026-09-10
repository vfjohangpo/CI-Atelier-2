"""Pipeline Craft — API FastAPI fil rouge pour les labs CI/CD."""

from fastapi import FastAPI

from app.config import settings
from app.routes import health, items, version

app = FastAPI(
    title="Pipeline Craft API",
    description="API fil rouge pour la formation GitLab CI/CD",
    version=settings.app_version,
)

app.include_router(health.router)
app.include_router(version.router)
app.include_router(items.router, prefix="/items", tags=["items"])
