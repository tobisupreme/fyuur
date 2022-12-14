"""Implement missing fields as database migration using Flask-Migrate

Revision ID: 8ef00e0d3272
Revises: 37f324e0fcdd
Create Date: 2022-08-11 16:53:20.299582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ef00e0d3272'
down_revision = '37f324e0fcdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=75), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('website', sa.String(length=90), nullable=False),
    sa.Column('facebook_link', sa.String(length=90), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=False),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=75), nullable=False),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('website', sa.String(length=90), nullable=False),
    sa.Column('facebook_link', sa.String(length=90), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=140), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###
