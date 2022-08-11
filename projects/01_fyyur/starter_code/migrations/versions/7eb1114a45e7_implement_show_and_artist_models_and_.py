"""Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

Revision ID: 7eb1114a45e7
Revises: 66f9e30d1560
Create Date: 2022-08-11 17:05:49.219062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eb1114a45e7'
down_revision = '66f9e30d1560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.Column('show_title', sa.String(), nullable=False),
    sa.Column('show_time', sa.DateTime(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('show_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###
