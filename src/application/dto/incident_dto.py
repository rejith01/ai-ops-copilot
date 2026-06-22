from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class IncidentDTO:
    incident_id: str

    title: str
    description: str
    service_name: str

    severity: str
    status: str

    created_at: datetime
    updated_at: datetime