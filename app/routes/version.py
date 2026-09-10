"""Endpoint de version."""

from fastapi import APIRouter

from app.config import settings
from app.models import VersionResponse

router = APIRouter(tags=["version"])


@router.get("/version", response_model=VersionResponse)
async def get_version() -> VersionResponse:
    """Retourne la version de l'application."""
    return VersionResponse(version=settings.app_version)
