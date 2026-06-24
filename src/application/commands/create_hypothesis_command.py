from dataclasses import dataclass


@dataclass(frozen=True)
class CreateHypothesisCommand:
    investigation_id: str

    description: str
    confidence_score: float