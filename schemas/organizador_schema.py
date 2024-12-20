from typing import Optional, List

from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

from .evento_schema import EventoResponseSchema

class OrganizadorBaseSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

class OrganizadorSchema(OrganizadorBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class OrganizadorUpdateSchema(OrganizadorBaseSchema):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

class OrganizadorEventoSchema(OrganizadorBaseSchema):
    eventos: List[EventoResponseSchema]