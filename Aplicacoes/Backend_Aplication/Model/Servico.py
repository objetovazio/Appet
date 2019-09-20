from peewee import *
from DatabaseCon import database as db
import Usuario
import TIpoServico

class Servico(Model):
    ##ORM reconhece automaticamente como PK
    id_servico = AutoField()
    titulo = CharField()
    descricao = CharField()
    preco = FloatField()
    ## FK relacional com o usuario dono de tal contato
    ## Referencia a pessoa que criou o serviço
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com o usuario dono de tal contato
    id_tipo = ForeignKeyField(TIpoServico)
    class Meta:
        database = db