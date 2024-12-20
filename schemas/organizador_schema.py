from typing import Optional, List

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from .evento_schema import EventoBaseSchema, EventoResponseSchema

class OrganizadorBaseSchema(BaseModel):
    nome: str
    email: str
    telefone: str

class OrganizadorSchema(OrganizadorBaseSchema):
    id: UUID
    criado_em: datetime

    class Config:
        from_attributes = True

class OrganizadorUpdateSchema(OrganizadorBaseSchema):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class OrganizadorEventoSchema(OrganizadorBaseSchema):
    eventos: List[EventoResponseSchema]