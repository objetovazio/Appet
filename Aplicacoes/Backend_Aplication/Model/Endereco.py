from peewee import *
from DatabaseCon import database as db
import Usuario

class Endereco(Model):
    ##ORM reconhece automaticamente como PK
    id_endereco = AutoField()
    cep = IntegerField()
    nome_bairro = CharField()
    nome_cidade = CharField()
    nome_estado = CharField()
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)
    class Meta:
        database = db