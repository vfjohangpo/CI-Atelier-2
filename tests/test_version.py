"""Tests du endpoint /version."""


def test_version_returns_name_and_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "pipeline-craft"
    assert "version" in data
