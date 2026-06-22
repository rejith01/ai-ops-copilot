from src.infrastructure.database.base import Base

# Import models so they register with metadata
from src.infrastructure.database.models.incident_model import IncidentModel
from src.infrastructure.database.models.investigation_model import InvestigationModel
from src.infrastructure.database.models.evidence_model import EvidenceModel
from src.infrastructure.database.models.root_cause_hypothesis_model import (
    RootCauseHypothesisModel,
)
from src.infrastructure.database.models.knowledge_document_model import (
    KnowledgeDocumentModel,
)
from src.infrastructure.database.models.runbook_model import (
    RunbookModel,
)
from src.infrastructure.database.models.execution_plan_model import (
    ExecutionPlanModel,
)
from src.infrastructure.database.models.rollback_plan_model import (
    RollbackPlanModel,
)


def test_all_tables_registered():
    tables = Base.metadata.tables

    assert "incidents" in tables
    assert "investigations" in tables
    assert "evidence" in tables
    assert "root_cause_hypotheses" in tables
    assert "knowledge_documents" in tables
    assert "runbooks" in tables
    assert "execution_plans" in tables
    assert "rollback_plans" in tables