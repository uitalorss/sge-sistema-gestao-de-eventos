from datetime import datetime

from pytz import timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings


class Evento(settings.DBBaseModel):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data_inicio = Column(DateTime, nullable=False)
    capacidade = Column(Integer, nullable=False)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False
    )
    criado_em = Column(
        DateTime, default=datetime.now(timezone("America/Bahia"))
    )
    atualizado_em = Column(
        DateTime,
        default=datetime.now(timezone("America/Bahia")),
        onupdate=datetime.now(timezone("America/Bahia")),
    )
    usuario = relationship("User", back_populates="eventos", lazy="joined")
    participantes = relationship(
        "User",
        secondary="inscricoes",
        cascade="all, delete",
        uselist=True,
        back_populates="eventos_inscritos",
        lazy="joined",
    )
