from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Avaliacao import Avaliacao

class Comentario(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_comentario = AutoField()
    comentario = CharField()
    ## FK relacional com o servico que esta recebendo a avalia
    id_avaliacao = ForeignKeyField(Avaliacao)
    