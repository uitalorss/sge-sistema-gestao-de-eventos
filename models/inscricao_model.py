from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from core.configs import settings


class Inscricao(settings.DBBaseModel):
    __tablename__ = "inscricoes"

    evento_id = Column(
        Integer, ForeignKey("eventos.id", ondelete="CASCADE"), primary_key=True
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        primary_key=True,
    )
    criado_em = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
