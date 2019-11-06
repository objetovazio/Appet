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
from Model.HorarioServico import HorarioServico

class Contratacao(BaseCon):
    ##ORM reconhece automaticamente como PK
    id_contratacao = AutoField()
    data_solicitacao = DateField()
    data_agendamento = DateField()
    horario_agendamento = ForeignKeyField(HorarioServico)
    forma_pagamento = CharField()
    valor = IntegerField()
    status_pagamento = IntegerField()
    token_pagamento = CharField()
    status_contratacao = IntegerField()
    ## FK relacional com contrato com o usuario que contratou o servico
    id_usuario = ForeignKeyField(Usuario)
    ## FK relacional com contrato com o servico contratado.
    id_servico = ForeignKeyField(Servico)
    