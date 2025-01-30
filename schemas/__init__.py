from datetime import datetime

from pydantic import BaseModel, EmailStr


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


class UserInscricaoSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
