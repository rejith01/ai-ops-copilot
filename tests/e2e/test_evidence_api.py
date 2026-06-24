import pytest
from httpx import AsyncClient

from src.api.main import app


@pytest.mark.asyncio
async def test_create_evidence_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        incident_response = await client.post(
            "/incidents",
            json={
                "title": "Evidence Test",
                "description": "Testing evidence",
                "service_name": "test-service",
                "severity": "P1",
            },
        )

        incident_id = incident_response.json()[
            "incident_id"
        ]

        investigation_response = await client.post(
            "/investigations",
            json={
                "incident_id": incident_id,
            },
        )

        investigation_id = (
            investigation_response.json()[
                "investigation_id"
            ]
        )

        response = await client.post(
            "/evidence",
            json={
                "investigation_id": investigation_id,
                "source": "datadog",
                "content": "CPU spike detected",
                "confidence_score": 0.95,
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["investigation_id"]
        == investigation_id
    )

    assert data["status"] == "COLLECTED"