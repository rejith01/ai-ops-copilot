from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class HypothesisDTO:
    hypothesis_id: str

    investigation_id: str

    description: str
    confidence_score: float

    status: str

    created_at: datetime
    updated_at: datetime