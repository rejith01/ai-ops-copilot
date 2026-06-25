import pytest
from httpx import AsyncClient

from src.api.main import app


@pytest.mark.asyncio
async def test_create_rollback_plan_api():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        # Step 1: Create an Execution Plan
        execution_plan_response = await client.post(
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

        execution_plan_id = execution_plan_response.json()[
            "execution_plan_id"
        ]

        # Step 2: Create Rollback Plan
        response = await client.post(
            "/rollback-plans",
            json={
                "execution_plan_id": execution_plan_id,
                "steps": [
                    "Restore backup",
                    "Restart PostgreSQL",
                    "Verify health",
                ],
            },
        )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["execution_plan_id"]
        == execution_plan_id
    )

    assert data["status"] == "DRAFT"

    assert data["steps"] == [
        "Restore backup",
        "Restart PostgreSQL",
        "Verify health",
    ]