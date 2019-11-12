from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.PeriodoAtividade import PeriodoAtividade

class HorarioServico(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_horario_servico = AutoField()
    ## FK relacional com o usuario dono de tal contato
    id_periodo = ForeignKeyField(PeriodoAtividade)
    dia_semana = IntegerField()
    horario_inicio = TimeField()
    horario_fim = TimeField()
    is_deleted = IntegerField(default=0)