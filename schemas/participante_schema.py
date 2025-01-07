from typing import Optional, List

from pydantic import EmailStr, field_validator
from uuid import UUID
from datetime import datetime
from utils.valida_telefone import valida_telefone
from . import ParticipanteBaseSchema
from schemas.evento_schema import EventoResponseSchema

class ParticipanteCreateSchema(ParticipanteBaseSchema):
    senha: str

class ParticipanteSchema(ParticipanteBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class ParticipanteUpdateSchema(ParticipanteBaseSchema):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)

class ParticipanteEventosSchema(ParticipanteSchema):
    eventos: List[EventoResponseSchema]

    class Config:
        from_attributes = True