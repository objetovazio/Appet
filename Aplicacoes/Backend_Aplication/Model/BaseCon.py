from peewee import *



class BaseCon(Model):
    class Meta:
        database = PostgresqlDatabase('eqvhegcr',
                                      user='eqvhegcr',
                                      password='1-1-1',
                                      host='motty.db.elephantsql.com', port=5432)
