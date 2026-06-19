from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infrastructure.database.base import Base


class InvestigationModel(Base):
    __tablename__ = "investigations"

    investigation_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    incident_id: Mapped[str] = mapped_column(
        ForeignKey("incidents.incident_id"),
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