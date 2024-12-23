from typing import Optional, List

from pydantic import BaseModel, EmailStr, field_validator
from uuid import UUID
from datetime import datetime

from .evento_schema import EventoResponseSchema
from utils.valida_telefone import valida_telefone

class OrganizadorBaseSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)
    
class OrganizadorCreateSchema(OrganizadorBaseSchema):
    senha: str


class OrganizadorSchema(OrganizadorBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class OrganizadorUpdateSchema(OrganizadorBaseSchema):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)

class OrganizadorEventoSchema(OrganizadorBaseSchema):
    eventos: List[EventoResponseSchema]