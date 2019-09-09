from peewee import *
from DatabaseCon import database as db

class TipoServico(Model):
    ##ORM reconhece automaticamente como PK
    id_tipo = AutoField()
    nome_tipo = CharField()
    class Meta:
        database = db