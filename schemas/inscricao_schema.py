from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from schemas import UserInscricaoSchema


class InscricaoBaseSchema(BaseModel):
    evento_id: int


class InscricaoSchema(InscricaoBaseSchema):
    user_id: UUID
    criado_em: datetime


class ParticipantesInscritosSchema(BaseModel):
    participantes: List[UserInscricaoSchema]


class InscricaoListUserSchema(BaseModel):
    nome: str
    descricao: str
    data_inicio: datetime
    capacidade: int
