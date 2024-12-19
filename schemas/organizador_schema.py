from typing import Optional

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

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