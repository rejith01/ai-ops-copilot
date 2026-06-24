from dataclasses import dataclass


@dataclass(frozen=True)
class CreateInvestigationCommand:
    incident_id: str