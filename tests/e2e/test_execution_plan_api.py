import pytest
from httpx import AsyncClient

from src.api.main import app


@pytest.mark.asyncio
async def test_create_execution_plan_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/execution-plans",
            json={
                "title": "Restart Database",
                "description": "Safely restart PostgreSQL",
                "actions": [
                    "Drain connections",
                    "Restart PostgreSQL",
                    "Verify health",
                ],
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Restart Database"
    assert data["status"] == "DRAFT"