"""Endpoint de health check."""

from fastapi import APIRouter

from app.models import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Vérifie que l'API est opérationnelle."""
    return HealthResponse()
