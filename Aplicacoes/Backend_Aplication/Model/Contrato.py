from peewee import *
from DatabaseCon import database as db
import Usuario
import Servico

class Contrato(Model):
    ##ORM reconhece automaticamente como PK
    id_contrato = AutoField()
    data_contratacao = DateField()
    data_prestacao = DateTimeField()
    descricao = CharField()
    ## FK relacional com contrato com o usuario que contratou o servico
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com contrato com o servico contratado.
    id_servico = ForeignKeyField(Servico)
    class Meta:
        database = db
    