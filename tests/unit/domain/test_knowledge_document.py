from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.knowledge_document import KnowledgeDocument
from src.domain.value_objects.knowledge_document_id import KnowledgeDocumentId


def test_empty_title_raises_error():
    with pytest.raises(
        ValueError,
        match="Title cannot be empty"
    ):
        KnowledgeDocument(
            knowledge_document_id=KnowledgeDocumentId(uuid4()),
            title="",
            content="Runbook content",
            source="Confluence",
            status="INGESTED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_content_raises_error():
    with pytest.raises(
        ValueError,
        match="Content cannot be empty"
    ):
        KnowledgeDocument(
            knowledge_document_id=KnowledgeDocumentId(uuid4()),
            title="Database Runbook",
            content="",
            source="Confluence",
            status="INGESTED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_source_raises_error():
    with pytest.raises(
        ValueError,
        match="Source cannot be empty"
    ):
        KnowledgeDocument(
            knowledge_document_id=KnowledgeDocumentId(uuid4()),
            title="Database Runbook",
            content="Runbook content",
            source="",
            status="INGESTED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    document = KnowledgeDocument(
        knowledge_document_id=KnowledgeDocumentId(uuid4()),
        title="Database Runbook",
        content="Runbook content",
        source="Confluence",
        status="INGESTED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    document.transition_to("CHUNKED")

    assert document.status == "CHUNKED"


def test_invalid_status_transition_raises_error():
    document = KnowledgeDocument(
        knowledge_document_id=KnowledgeDocumentId(uuid4()),
        title="Database Runbook",
        content="Runbook content",
        source="Confluence",
        status="INGESTED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        document.transition_to("INDEXED")