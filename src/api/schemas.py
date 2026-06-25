from pydantic import BaseModel


class CreateIncidentRequest(BaseModel):
    title: str
    description: str
    service_name: str
    severity: str

class CreateInvestigationRequest(BaseModel):
    incident_id: str

class CreateEvidenceRequest(BaseModel):
    investigation_id: str

    source: str
    content: str
    confidence_score: float

class CreateHypothesisRequest(BaseModel):
    investigation_id: str

    description: str
    confidence_score: float

class CreateExecutionPlanRequest(BaseModel):
    title: str
    description: str

    actions: list[str]

class CreateRollbackPlanRequest(BaseModel):
    execution_plan_id: str

    steps: list[str]