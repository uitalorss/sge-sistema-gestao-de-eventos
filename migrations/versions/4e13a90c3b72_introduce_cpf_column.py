"""introduce-cpf-column

Revision ID: 4e13a90c3b72
Revises: 721c2d951a08
Create Date: 2025-01-29 09:53:30.238600

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4e13a90c3b72"
down_revision: Union[str, None] = "721c2d951a08"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "usuarios",
        sa.Column("cpf", sa.String(length=14), nullable=False, unique=False),
    )


def downgrade() -> None:
    op.drop_column("usuarios", "cpf")
