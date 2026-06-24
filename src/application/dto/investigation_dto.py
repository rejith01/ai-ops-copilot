from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class InvestigationDTO:
    investigation_id: str

    incident_id: str

    status: str

    created_at: datetime
    updated_at: datetime