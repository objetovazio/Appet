from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Usuario import Usuario
from Model.Servico import Servico

class Avaliacao(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_avaliacao = AutoField()
    nota = FloatField()
    ## FK relacional com o usuario que efetuou avaliacao
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com o servico que esta recebendo a avalia
    id_servico = ForeignKeyField(Servico)
    