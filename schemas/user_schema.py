from uuid import UUID

from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr
from models.profile_model import PerfilEnum
from .inscricao_schema import InscricaoListUserSchema
from . import EventoListUserSchema

class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    perfil: List[PerfilEnum]

class CreateUserSchema(UserSchema):
    senha: str

class LoginUserSchema(BaseModel):
    email: EmailStr
    senha: str

class UserInListSchema(BaseModel):
    nome: str

class UserResponseSchema(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    telefone: str
    criado_em: datetime
    eventos: list[EventoListUserSchema]
    eventos_inscritos: List[InscricaoListUserSchema]