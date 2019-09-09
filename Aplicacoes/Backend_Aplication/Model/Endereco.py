from peewee import *
from DatabaseCon import database as db
import Pessoa

class Endereco(Model):
    ##ORM reconhece automaticamente como PK
    id_endereco = AutoField()
    cep = IntegerField()
    nome_bairro = CharField()
    nome_cidade = CharField()
    nome_estado = CharField()
    ## FK relacional com o usuario dono de tal contato
    id_pessoa = ForeignKeyField(Pessoa)
    class Meta:
        database = db