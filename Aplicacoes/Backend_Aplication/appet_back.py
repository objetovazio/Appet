import os
from flask import Flask
from flask import json
from flask import jsonify
from flask import request
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------
from Model.Usuario import *

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/createUser', methods=['POST'])
def createUser():
     name_user = request.args.post('nomeUser')
    email_user = request.args.post('emailUser')
    password = request.args.post('senha')
    about_user = request.args.post('sobre')
    if(name_user == '' or email_user == '' or password == ''):
        return handle_invalid('Empty parameters')
    else:
        new_user = None
        if(about_user != None and about_user != ''):
            new_user = Usuario(nome = name_user, email = name_user, senha = password, sobre = about_user)
        else:
            new_user = Usuario(nome = name_user, email = name_user, senha = password)
        print(new_user.nome)
        new_user.save()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        


def handle_invalid(erroType):
    response = jsonify(erroType)
    response.status_code = 400
    return response
