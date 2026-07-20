from __future__ import annotations

import enum

from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from agentops.db.base import Base
from agentops.db.mixins import TimestampMixin, UUIDMixin


class OpportunityStatus(enum.StrEnum):
    NEW = "new"
    RESEARCHING = "researching"
    PROPOSAL_DRAFTED = "proposal_drafted"
    QUOTATION_READY = "quotation_ready"
    AWAITING_APPROVAL = "awaiting_approval"
    SENT = "sent"
    NEGOTIATION = "negotiation"
    WON = "won"
    LOST = "lost"


class OpportunityPriority(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class OpportunitySource(enum.StrEnum):
    EMAIL = "email"
    WEBSITE = "website"
    LINKEDIN = "linkedin"
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    MANUAL = "manual"
    API = "api"


class Opportunity(Base, UUIDMixin, TimestampMixin):
    """
    Sales opportunity captured by the AI Workforce Platform.
    """

    __tablename__ = "opportunities"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    organization_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
        default="demo-org",
        server_default="demo-org",
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    company_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    contact_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    status: Mapped[OpportunityStatus] = mapped_column(
        Enum(
            OpportunityStatus,
            name="opportunitystatus",
            values_callable=lambda enum_cls: [e.value for e in enum_cls],
        ),
        default=OpportunityStatus.NEW,
        server_default="new",
        nullable=False,
    )

    priority: Mapped[OpportunityPriority] = mapped_column(
        Enum(
            OpportunityPriority,
            name="opportunitypriority",
            values_callable=lambda enum_cls: [e.value for e in enum_cls],
        ),
        default=OpportunityPriority.MEDIUM,
        server_default="medium",
        nullable=False,
    )

    source: Mapped[OpportunitySource] = mapped_column(
        Enum(
            OpportunitySource,
            name="opportunitysource",
            values_callable=lambda enum_cls: [e.value for e in enum_cls],
        ),
        default=OpportunitySource.MANUAL,
        server_default="manual",
        nullable=False,
    )
