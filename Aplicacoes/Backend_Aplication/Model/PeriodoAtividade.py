from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Usuario import Usuario

class PeriodoAtividade(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_periodo_atividde = AutoField()
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)
    inicioDate = DateField()
    fimDate = DateField()