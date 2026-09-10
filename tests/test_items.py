"""Tests CRUD du endpoint /items."""


def test_list_items_empty(client):
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_get_item(client):
    payload = {"name": "Widget Alpha", "description": "Un composant", "price": 29.99}
    response = client.post("/items/", json=payload)
    assert response.status_code == 201
    item = response.json()
    assert item["id"] == 1
    assert item["name"] == "Widget Alpha"
    assert item["price"] == 29.99

    # Récupérer l'item créé
    response = client.get(f"/items/{item['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Widget Alpha"


def test_delete_item(client):
    client.post("/items/", json={"name": "Temp", "price": 1.0})
    response = client.delete("/items/1")
    assert response.status_code == 204

    response = client.get("/items/1")
    assert response.status_code == 404


def test_get_nonexistent_item_returns_404(client):
    response = client.get("/items/999")
    assert response.status_code == 404
