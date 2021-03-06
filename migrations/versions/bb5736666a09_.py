"""empty message

Revision ID: bb5736666a09
Revises: 
Create Date: 2020-12-13 21:24:23.306194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb5736666a09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('uId', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=60), nullable=False),
    sa.Column('lastName', sa.String(length=60), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('profileImg', sa.String(length=500), nullable=True),
    sa.Column('createDate', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('isVerifyAccount', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('uId'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    # ### end Alembic commands ###
