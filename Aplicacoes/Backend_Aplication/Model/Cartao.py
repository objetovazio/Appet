from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Usuario import Usuario

class Cartao(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_cartao = AutoField()
    nome_titular = CharField()
    validade = CharField()
    cpf_titular = IntegerField()
    numero_cartao = IntegerField()
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)