from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Servico import Servico
from Model.HorarioServico import HorarioServico

#MODEL DE LINK ENRTE SERVICO E HORARIO DE PRESTACAO
class ServicoHorario(BaseCon):
    id_servico = ForeignKeyField(Servico)
    id_horarioservico = ForeignKeyField(HorarioServico)