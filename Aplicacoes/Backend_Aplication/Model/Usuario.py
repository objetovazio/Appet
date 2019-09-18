from peewee import *
from DatabaseCon import database as db

class Pessoa(Model):
    ##ORM reconhece automaticamente como PK
    pessoa_id = AutoField() 
    nome = CharField()
    email = CharField()
    senha = CharField()
    sobre = CharField()
    class Meta:
        database = db