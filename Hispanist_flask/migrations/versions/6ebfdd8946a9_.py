"""empty message

Revision ID: 6ebfdd8946a9
Revises: 6968329f0d8a
Create Date: 2023-11-01 15:31:57.907890

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "6ebfdd8946a9"
down_revision: Union[str, None] = "6968329f0d8a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question", sa.String(), nullable=False),
        sa.Column("options", sa.String(), nullable=False),
        sa.Column("answer", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("resourses")
    op.drop_table("topics")
    op.drop_index("users_topic_idx", table_name="resourses_to_topics")
    op.drop_table("resourses_to_topics")
    op.drop_table("eayh_questions")
    op.add_column("users", sa.Column("level", sa.String(length=50), nullable=True))
    op.add_column("users", sa.Column("region", sa.String(length=200), nullable=True))
    op.add_column("users", sa.Column("gender", sa.String(length=200), nullable=True))
    op.add_column("users", sa.Column("age", sa.Integer(), nullable=True))
    op.add_column("users", sa.Column("goal", sa.String(length=300), nullable=True))
    op.add_column("users", sa.Column("info", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "info")
    op.drop_column("users", "goal")
    op.drop_column("users", "age")
    op.drop_column("users", "gender")
    op.drop_column("users", "region")
    op.drop_column("users", "level")
    op.create_table(
        "eayh_questions",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("question", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column(
            "options", postgresql.ARRAY(sa.TEXT()), autoincrement=False, nullable=False
        ),
        sa.Column("answer", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="eayh_questions_pkey"),
    )
    op.create_table(
        "resourses_to_topics",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("resourse_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("topic_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["resourse_id"],
            ["resourses.id"],
            name="resourses_to_topics_resourse_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["topic_id"], ["topics.id"], name="resourses_to_topics_topic_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="resourses_to_topics_pkey"),
    )
    op.create_index(
        "users_topic_idx",
        "resourses_to_topics",
        ["resourse_id", "topic_id"],
        unique=False,
    )
    op.create_table(
        "topics",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("title", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="topics_pkey"),
    )
    op.create_table(
        "resourses",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("title", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("type", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="resourses_pkey"),
    )
    op.drop_table("questions")
    # ### end Alembic commands ###
