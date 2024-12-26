from core.configs import settings

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from pytz import timezone
from datetime import datetime

class Evento(settings.DBBaseModel):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data_inicio = Column(DateTime, nullable=False)
    capacidade = Column(Integer, nullable=False)
    organizador_id = Column(UUID(as_uuid=True), ForeignKey('organizadores.id'), nullable=False)
    criado_em = Column(DateTime, default=datetime.now(timezone("America/Bahia")))
    atualizado_em = Column(DateTime, default=datetime.now(timezone("America/Bahia")), onupdate=datetime.now(timezone("America/Bahia")))
    organizador = relationship("Organizador", back_populates="eventos", lazy="joined")
    participantes = relationship("Participante", secondary="participantes_eventos", cascade="all, delete", back_populates="eventos", lazy="joined")

