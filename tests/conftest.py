"""Fixtures partagées pour les tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def client():
    """Client de test FastAPI."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def _reset_items():
    """Remet le stockage in-memory à zéro entre chaque test."""
    import app.routes.items as mod

    mod._items.clear()
    mod._next_id = 1
    yield
    mod._items.clear()
    mod._next_id = 1
