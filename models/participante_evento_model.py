from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from pytz import timezone
from datetime import datetime

from core.configs import settings

class ParticipanteEvento(settings.DBBaseModel):
    __tablename__ = "participantes_eventos"

    evento_id = Column(Integer, ForeignKey('eventos.id', ondelete="CASCADE"), primary_key=True)
    participante_id = Column(UUID(as_uuid=True), ForeignKey('participantes.id', ondelete="CASCADE"), primary_key=True)
    criado_em = Column(DateTime, default=datetime.now(timezone("America/Bahia")))