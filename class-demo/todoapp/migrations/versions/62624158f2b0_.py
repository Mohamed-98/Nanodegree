"""empty message

Revision ID: 62624158f2b0
Revises: b6a1b2a56227
Create Date: 2020-12-01 14:44:14.103862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62624158f2b0'
down_revision = 'b6a1b2a56227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolist', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###
