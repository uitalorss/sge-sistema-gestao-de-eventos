from typing import Optional, List, TYPE_CHECKING

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EventoBaseSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int
    organizador_id: UUID

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
    eventos: List[EventoBaseSchema]

    class Config:
        from_attributes = True

ParticipanteEventosSchema.model_rebuild()