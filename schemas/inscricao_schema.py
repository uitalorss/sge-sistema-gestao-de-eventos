from typing import Optional

from pydantic import BaseModel
from uuid import UUID

from datetime import datetime

class InscricaoBaseSchema(BaseModel):
    evento_id: int

class InscricaoSchema(InscricaoBaseSchema):
    participante_id: UUID
    criado_em: datetime