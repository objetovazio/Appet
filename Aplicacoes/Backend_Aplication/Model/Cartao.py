from peewee import *
from DatabaseCon import database as db
import Usuario

class Cartao(Model):
    ##ORM reconhece automaticamente como PK
    id_cartao = AutoField()
    nome_titular = CharField()
    validade = CharField()
    cpf_titular = IntegerField()
    numero_cartao = IntegerField()
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)
    class Meta:
        database = db