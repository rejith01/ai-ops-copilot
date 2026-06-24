from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class EvidenceDTO:
    evidence_id: str

    investigation_id: str

    source: str
    content: str
    confidence_score: float

    status: str

    created_at: datetime
    updated_at: datetime