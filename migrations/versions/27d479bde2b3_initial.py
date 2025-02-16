"""initial

Revision ID: 27d479bde2b3
Revises:
Create Date: 2025-01-30 15:42:24.467667
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "27d479bde2b3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "usuarios",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("cpf", sa.String(length=14), nullable=False),
        sa.Column("senha", sa.String(), nullable=False),
        sa.Column("telefone", sa.String(length=11), nullable=True),
        sa.Column(
            "criado_em",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("cpf"),
    )
    op.create_index(
        op.f("ix_usuarios_email"), "usuarios", ["email"], unique=True
    )
    op.create_index(op.f("ix_usuarios_id"), "usuarios", ["id"], unique=False)
    op.create_table(
        "eventos",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("descricao", sa.String(), nullable=True),
        sa.Column("data_inicio", sa.DateTime(), nullable=False),
        sa.Column("capacidade", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column(
            "criado_em",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "atualizado_em",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["usuarios.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_eventos_id"), "eventos", ["id"], unique=False)
    op.create_table(
        "perfis",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("usuario_id", sa.UUID(), nullable=True),
        sa.Column(
            "tipo_perfil",
            sa.Enum("ORGANIZADOR", "PARTICIPANTE", "ADMIN", name="perfilenum"),
            nullable=False,
        ),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["usuario_id"], ["usuarios.id"], ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "inscricoes",
        sa.Column("evento_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("criado_em", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["evento_id"], ["eventos.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["usuarios.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("evento_id", "user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("inscricoes")
    op.drop_table("perfis")
    op.drop_index(op.f("ix_eventos_id"), table_name="eventos")
    op.drop_table("eventos")
    op.drop_index(op.f("ix_usuarios_id"), table_name="usuarios")
    op.drop_index(op.f("ix_usuarios_email"), table_name="usuarios")
    op.drop_table("usuarios")
    # ### end Alembic commands ###
