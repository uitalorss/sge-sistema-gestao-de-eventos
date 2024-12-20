from typing import Optional, List

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from .evento_schema import EventoResponseSchema

class ParticipanteBaseSchema(BaseModel):
    nome: str
    email: str
    telefone: str

class ParticipanteSchema(ParticipanteBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class ParticipanteUpdateSchema(ParticipanteBaseSchema):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class ParticipanteEventosSchema(ParticipanteSchema):
    eventos: List[EventoResponseSchema]