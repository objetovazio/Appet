from peewee import *

# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.BaseCon import BaseCon

class Usuario(BaseCon):
    ##ORM reconhece automaticamente como PK
    usuario_id  = PrimaryKeyField() 
    nome        = CharField()
    email       = CharField(unique = True)
    senha       = CharField()
    sobre       = CharField(null = True)
    is_adm      = IntegerField(default=0)
    is_deleted  = IntegerField(default=0)