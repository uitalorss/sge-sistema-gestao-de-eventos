from typing import Optional, List
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class ParticipanteBaseSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

class EventoBaseSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: str
    capacidade: int
    organizador_id: str

class EventoSchema(EventoBaseSchema):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True

class EventoUpdateSchema(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    data_inicio: Optional[datetime] = None
    capacidade: Optional[int] = None
    
class EventoResponseSchemaCompleto(BaseModel):
    id: int
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int
    organizador_id: UUID
    criado_em: datetime
    atualizado_em: datetime
    participantes: List[ParticipanteBaseSchema]

    class Config:
        from_attributes = True

class EventoResponseSchema(EventoBaseSchema):
    data_inicio: datetime
    organizador_id: UUID

    class Config:
        from_attributes = True