from typing import List
from pydantic import BaseModel, EmailStr
from models.profile_model import PerfilEnum

class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    perfil: List[PerfilEnum]

class CreateUserSchema(UserSchema):
    senha: str
