from pydantic import BaseModel, EmailStr, field_validator
from uuid import UUID
from datetime import datetime

from utils.valida_telefone import valida_telefone

class ParticipanteBaseSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)

class EventoBaseSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: str
    capacidade: int

class EventoListUserSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int