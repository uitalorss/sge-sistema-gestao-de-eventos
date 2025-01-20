from enum import Enum
from core.configs import settings
import uuid

from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class PerfilEnum(str, Enum):
    ORGANIZADOR = "Organizador"
    PARTICIPANTE = "Participante"

class Profile(settings.DBBaseModel):
    __tablename__ = "perfis"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id", ondelete="cascade"))
    tipo_perfil = Column(SQLAlchemyEnum(PerfilEnum), nullable=False)

    usuario = relationship("User", back_populates="perfil")