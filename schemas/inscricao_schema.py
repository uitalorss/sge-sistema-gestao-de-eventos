from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class InscricaoBaseSchema(BaseModel):
    evento_id: int


class InscricaoSchema(InscricaoBaseSchema):
    user_id: UUID
    criado_em: datetime


class InscricaoListUserSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int
