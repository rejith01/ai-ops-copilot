from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.knowledge_document_id import KnowledgeDocumentId


@dataclass
class KnowledgeDocument:
    knowledge_document_id: KnowledgeDocumentId

    title: str
    content: str
    source: str

    status: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

        if not self.content.strip():
            raise ValueError("Content cannot be empty")

        if not self.source.strip():
            raise ValueError("Source cannot be empty")

    def transition_to(self, new_status: str):
        allowed_transitions = {
            "INGESTED": {"CHUNKED"},
            "CHUNKED": {"EMBEDDED"},
            "EMBEDDED": {"INDEXED"},
            "INDEXED": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()