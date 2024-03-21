"""another migration

Revision ID: 61de058ba5c7
Revises: 5185cdee6a9d
Create Date: 2024-03-21 13:47:14.972415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61de058ba5c7'
down_revision = '5185cdee6a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('contact', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('number_of_pages', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('companies')
    op.drop_table('books')
    op.drop_table('Users')
    # ### end Alembic commands ###