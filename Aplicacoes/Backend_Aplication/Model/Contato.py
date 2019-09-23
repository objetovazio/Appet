from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Usuario import Usuario

class Contato(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_contato = AutoField()
    ## Enum representante do tipo de contato
    tipo = IntegerField() 
    ## Valor do contato em questao
    descricao = CharField() 
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)