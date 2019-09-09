from peewee import *
from DatabaseCon import database as db
import Avaliacao

class Comentario(Model):
    ##ORM reconhece automaticamente como PK
    id_comentario = AutoField()
    comentario = CharField()
    ## FK relacional com o servico que esta recebendo a avalia
    id_avaliacao = ForeignKeyField(Avaliacao)
    class Meta:
        database = db
    