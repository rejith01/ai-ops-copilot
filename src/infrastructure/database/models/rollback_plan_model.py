from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infrastructure.database.base import Base


class RollbackPlanModel(Base):
    __tablename__ = "rollback_plans"

    rollback_plan_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    execution_plan_id: Mapped[str] = mapped_column(
    ForeignKey("execution_plans.execution_plan_id"),
    nullable=False,
    )

    steps: Mapped[list[str]] = mapped_column(
    JSON,
    nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )