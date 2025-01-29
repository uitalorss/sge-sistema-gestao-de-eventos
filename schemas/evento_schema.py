from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from . import EventoBaseSchema
from .user_schema import UserInListSchema


class EventoSchema(EventoBaseSchema):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True


class EventoUpdateSchema(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    data_inicio: Optional[str] = None
    capacidade: Optional[int] = None


class EventoResponseSchemaCompleto(BaseModel):
    id: int
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int
    organizador: str
    criado_em: datetime
    atualizado_em: datetime
    participantes: List[UserInListSchema]

    class Config:
        from_attributes = True


class EventoResponseSchema(EventoBaseSchema):
    data_inicio: datetime
    organizador: str = ""

    class Config:
        from_attributes = True
