from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon

class TipoServico(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_tipo = AutoField()
    nome_tipo = CharField()