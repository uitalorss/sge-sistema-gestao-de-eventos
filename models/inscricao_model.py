from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from pytz import timezone
from datetime import datetime

from core.configs import settings

class Inscricao(settings.DBBaseModel):
    __tablename__ = "inscricoes"

    evento_id = Column(Integer, ForeignKey('eventos.id', ondelete="CASCADE"), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('usuarios.id', ondelete="CASCADE"), primary_key=True)
    criado_em = Column(DateTime, default=datetime.now(timezone("America/Bahia")))