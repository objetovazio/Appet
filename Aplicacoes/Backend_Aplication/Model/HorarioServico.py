from peewee import *
from DatabaseCon import database as db
import PeriodoAtividade

class HorarioServico(Model):
    ##ORM reconhece automaticamente como PK
    id_horario_servico = AutoField()
    ## FK relacional com o usuario dono de tal contato
    id_periodo = ForeignKeyField(PeriodoAtividade)
    dia_semana = IntegerField()
    horario_inicio = TimeField()
    horario_fim = TimeField()

    class Meta:
        database = db