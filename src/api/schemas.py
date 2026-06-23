from pydantic import BaseModel


class CreateIncidentRequest(BaseModel):
    title: str
    description: str
    service_name: str
    severity: str