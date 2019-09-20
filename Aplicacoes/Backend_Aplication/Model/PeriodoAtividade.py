from peewee import *
from DatabaseCon import database as db
import Usuario

class PeriodoAtividade(Model):
    ##ORM reconhece automaticamente como PK
    id_periodo_atividde = AutoField()
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)
    inicioDate = DateField()
    fimDate = DateField()
    class Meta:
        database = db