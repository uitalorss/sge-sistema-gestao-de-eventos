import uuid
from datetime import datetime

from pytz import timezone
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings


class Organizador(settings.DBBaseModel):
    __tablename__ = "organizadores"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=False,
        index=True,
    )
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    telefone = Column(String(11), nullable=True)
    criado_em = Column(
        DateTime, default=datetime.now(timezone("America/Bahia"))
    )
