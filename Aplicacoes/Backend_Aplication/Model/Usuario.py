from peewee import *

# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------

from Model.DatabaseCon import database as db

class Usuario(Model):
    ##ORM reconhece automaticamente como PK
    usuario_id = PrimaryKeyField() 
    nome = CharField()
    email = CharField()
    senha = CharField()
    sobre = CharField(null = True)
    class Meta:
        database = PostgresqlDatabase('eqvhegcr',
                              user='eqvhegcr',
                              password='-------',
                              host='motty.db.elephantsql.com', port=5432)