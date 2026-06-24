from dataclasses import dataclass


@dataclass(frozen=True)
class CreateEvidenceCommand:
    investigation_id: str

    source: str
    content: str
    confidence_score: float