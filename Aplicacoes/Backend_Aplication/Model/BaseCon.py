from peewee import *
from peewee import fn


class BaseCon(Model):
    class Meta:
        database = PostgresqlDatabase('eqvhegcr',
                                      user='eqvhegcr',
                                      password='x-x-x-x-x',
                                      host='motty.db.elephantsql.com', port=5432)
