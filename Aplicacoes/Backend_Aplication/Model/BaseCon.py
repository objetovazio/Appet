from peewee import *


class BaseCon(Model):
    class Meta:
        database = PostgresqlDatabase('eqvhegcr',
                                      user='eqvhegcr',
                                      password='XxX',
                                      host='motty.db.elephantsql.com', port=5432)
