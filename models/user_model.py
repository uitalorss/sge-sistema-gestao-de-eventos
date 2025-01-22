import uuid
from datetime import datetime

from pytz import timezone
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings


class User(settings.DBBaseModel):
    __tablename__ = "usuarios"

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
    perfil = relationship(
        "Profile", back_populates="usuario", cascade="all, delete-orphan"
    )
    eventos = relationship(
        "Evento",
        back_populates="usuario",
        lazy="joined",
        uselist=True,
        cascade="all, delete-orphan",
    )
    eventos_inscritos = relationship(
        "Evento",
        secondary="inscricoes",
        cascade="all, delete",
        back_populates="participantes",
        lazy="joined",
        uselist=True,
    )
