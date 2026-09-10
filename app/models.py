"""Modèles Pydantic pour l'API."""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """Schéma de création d'un item."""

    name: str = Field(..., min_length=1, max_length=100, examples=["Widget Alpha"])
    description: str = Field(
        default="", max_length=500, examples=["Un composant essentiel"]
    )
    price: float = Field(..., gt=0, examples=[29.99])


class Item(ItemCreate):
    """Schéma complet d'un item avec son identifiant."""

    id: int


class HealthResponse(BaseModel):
    """Réponse du endpoint /health."""

    status: str = "ok"


class VersionResponse(BaseModel):
    """Réponse du endpoint /version."""

    version: str
    name: str = "pipeline-craft"
