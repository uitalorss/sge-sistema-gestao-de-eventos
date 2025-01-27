from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, field_validator

from models.profile_model import PerfilEnum
from utils.valida_telefone import valida_telefone

from . import EventoListUserSchema
from .inscricao_schema import InscricaoListUserSchema


class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    perfil: List[PerfilEnum]


class CreateUserSchema(UserSchema):
    senha: str

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)


class LoginUserSchema(BaseModel):
    email: EmailStr
    senha: str


class UserInListSchema(BaseModel):
    nome: str


class UserUpdateSchema(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None

    @field_validator("telefone")
    def validate_telefone(cls, v):
        return valida_telefone(v)


class ProfileResponseSchema(BaseModel):
    tipo_perfil: PerfilEnum
    is_active: bool

    class Config:
        from_attributes = True


class UserResponseSchema(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    telefone: str
    criado_em: datetime
    eventos: list[EventoListUserSchema]
    eventos_inscritos: List[InscricaoListUserSchema]
