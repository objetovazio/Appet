from peewee import *
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon
from Model.Usuario import Usuario
from Model.TipoServico import TipoServico

class Servico(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_servico = AutoField()
    titulo = CharField()
    descricao = CharField()
    preco = FloatField()
    ## FK relacional com o usuario dono de tal contato
    ## Referencia a pessoa que criou o serviço
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com o usuario dono de tal contato
    id_tipo = ForeignKeyField(TipoServico)
    is_deleted = IntegerField(default=0)