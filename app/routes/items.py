"""Endpoints CRUD pour les items (stockage in-memory)."""

from fastapi import APIRouter, HTTPException

from app.models import Item, ItemCreate

router = APIRouter()

# Stockage in-memory — suffisant pour les labs
_items: dict[int, Item] = {}
_next_id: int = 1


@router.get("/", response_model=list[Item])
async def list_items() -> list[Item]:
    """Liste tous les items."""
    return list(_items.values())


@router.post("/", response_model=Item, status_code=201)
async def create_item(payload: ItemCreate) -> Item:
    """Crée un nouvel item."""
    global _next_id
    item = Item(id=_next_id, **payload.model_dump())
    _items[_next_id] = item
    _next_id += 1
    return item


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    """Récupère un item par son identifiant."""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    return _items[item_id]


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None:
    """Supprime un item par son identifiant."""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item non trouvé")
    del _items[item_id]
