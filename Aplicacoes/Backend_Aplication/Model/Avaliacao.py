from peewee import *
from DatabaseCon import database as db
import Pessoa
import Servico

class Avaliacao(Model):
    ##ORM reconhece automaticamente como PK
    id_avaliacao = AutoField()
    nota = FloatField()
    ## FK relacional com o usuario que efetuou avaliacao
    id_pessoa = ForeignKeyField(Pessoa)
    ## FK relacional com o servico que esta recebendo a avalia
    id_servico = ForeignKeyField(Servico)
    class Meta:
        database = db
    