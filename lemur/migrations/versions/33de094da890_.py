"""Adding the ability to specify certificate replacements

Revision ID: 33de094da890
Revises: ed422fc58ba
Create Date: 2015-11-30 15:40:19.827272

"""

# revision identifiers, used by Alembic.
revision = '33de094da890'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certificate_replacement_associations',
    sa.Column('replaced_certificate_id', sa.Integer(), nullable=True),
        sa.Column('certificate_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['certificate_id'], ['certificates.id'], ondelete='cascade'),
        sa.ForeignKeyConstraint(['replaced_certificate_id'], ['certificates.id'], ondelete='cascade')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificate_replacement_associations')
    ### end Alembic commands ###
