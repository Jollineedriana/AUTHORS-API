"""migrate

Revision ID: c88dbf5f70f0
Revises: fd93de7338db
Create Date: 2024-03-21 11:15:21.932541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c88dbf5f70f0'
down_revision = 'fd93de7338db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('contact', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('user_type', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', 'contact'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('contact')
        batch_op.drop_index('email')
        batch_op.drop_index('password')

    op.drop_table('users')
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint('books_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'])

    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_constraint('companies_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('companies_ibfk_2', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('books_ibfk_1', 'users', ['user_id'], ['id'])

    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('contact', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('update_at', mysql.DATETIME(), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', 'contact'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('password', ['password'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)
        batch_op.create_index('contact', ['contact'], unique=True)

    op.drop_table('Users')
    # ### end Alembic commands ###
