from peewee import *
from DatabaseCon import database as db
import Pessoa

class Contato(Model):
    ##ORM reconhece automaticamente como PK
    id_contato = AutoField()
    ## Enum representante do tipo de contato
    tipo = IntegerField() 
    ## Valor do contato em questao
    descricao = CharField() 
    ## FK relacional com o usuario dono de tal contato
    id_pessoa = ForeignKeyField(Pessoa)
    class Meta:
        database = db