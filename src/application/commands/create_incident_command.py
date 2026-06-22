from dataclasses import dataclass


@dataclass(frozen=True)
class CreateIncidentCommand:
    title: str
    description: str
    service_name: str
    severity: str