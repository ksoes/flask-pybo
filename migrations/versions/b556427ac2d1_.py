"""empty message

Revision ID: b556427ac2d1
Revises: 35c3ac923410
Create Date: 2022-03-17 16:35:05.403466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b556427ac2d1'
down_revision = '35c3ac923410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('wq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('wq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('wq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('wq_user_email'), type_='unique')

    # ### end Alembic commands ###