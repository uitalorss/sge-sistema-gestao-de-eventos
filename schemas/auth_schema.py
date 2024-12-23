from enum import Enum
from pydantic import BaseModel, EmailStr

class LoginTypeEnum(str, Enum):
    ORGANIZADOR = "Organizador"
    PARTICIPANTE = "Participante"


class LoginSchema(BaseModel):
    auth_type: LoginTypeEnum
    email: EmailStr
    senha: str