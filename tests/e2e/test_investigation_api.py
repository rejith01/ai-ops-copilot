import pytest
from httpx import AsyncClient

from src.api.main import app


@pytest.mark.asyncio
async def test_create_investigation_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        incident_response = await client.post(
            "/incidents",
            json={
                "title": "Investigation Test",
                "description": "Create investigation",
                "service_name": "test-service",
                "severity": "P1",
            },
        )

        incident_id = incident_response.json()[
            "incident_id"
        ]

        response = await client.post(
            "/investigations",
            json={
                "incident_id": incident_id,
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["incident_id"] == incident_id
    assert data["status"] == "CREATED"