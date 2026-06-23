import pytest
from httpx import AsyncClient

from src.api.main import app


@pytest.mark.asyncio
async def test_create_incident_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/incidents",
            json={
                "title": "API Test Incident",
                "description": "Testing API",
                "service_name": "test-service",
                "severity": "P1",
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "API Test Incident"
    assert data["status"] == "OPEN"


@pytest.mark.asyncio
async def test_get_incident_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        create_response = await client.post(
            "/incidents",
            json={
                "title": "Lookup Incident",
                "description": "Testing lookup",
                "service_name": "test-service",
                "severity": "P1",
            },
        )

        incident_id = create_response.json()[
            "incident_id"
        ]

        get_response = await client.get(
            f"/incidents/{incident_id}"
        )

    assert get_response.status_code == 200

    data = get_response.json()

    assert data["incident_id"] == incident_id
    assert data["title"] == "Lookup Incident"