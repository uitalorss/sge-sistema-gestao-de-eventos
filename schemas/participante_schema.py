from typing import Optional, List

from pydantic import BaseModel, EmailStr
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
    email: EmailStr
    telefone: str

class ParticipanteSchema(ParticipanteBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class ParticipanteUpdateSchema(ParticipanteBaseSchema):
    nome: Optional[str] = None
    email: Optional[str] = EmailStr
    telefone: Optional[str] = None

class ParticipanteEventosSchema(ParticipanteSchema):
    eventos: List[EventoBaseSchema]

    class Config:
        from_attributes = True

ParticipanteEventosSchema.model_rebuild()