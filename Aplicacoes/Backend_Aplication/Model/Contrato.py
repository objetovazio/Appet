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

class Contrato(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_contrato = AutoField()
    data_contratacao = DateField()
    data_prestacao = DateTimeField()
    descricao = CharField()
    ## FK relacional com contrato com o usuario que contratou o servico
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com contrato com o servico contratado.
    id_servico = ForeignKeyField(Servico)
    