from Model.Usuario import *
from Model.TipoServico import *
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

app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Rate', methods=['POST'])
def postRate():
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Rate',methods=['GET'])
def getRate():
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/CrediCard', methods=['POST'])
def postCrediCard():
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/CrediCard', methods=['GET'])
def getCrediCard():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Comment', methods=['POST'])
def postComment():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Comment', methods=['GET'])
def getComment():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Contact', methods=['POST'])
def postContact():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Contact', methods=['GET'])
def getContact():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['POST'])
def postAddress():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['GET'])
def getAddress():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceHour', methods=['POST'])
def postServiceHour():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceHour', methods=['GET'])
def getServiceHour():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/AtivityTime', methods=['POST'])
def postAtivityTime():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/AtivityTime', methods=['GET'])
def getAtivityTime():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Service', methods=['POST'])
def postService():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Service', methods=['GET'])
def getService():
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Rota para criacao e atualizacao de Tipo de Serviço
@app.route('/TypeService', methods=['POST'])
def postTypeService():
	name_service_type = request.args.get('nomeTipoServico')
	print(name_service_type)
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Rota para busca de Tipo de Serviço
@app.route('/TypeService', methods=['GET'])
def getTypeService():
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Rota para criacao e atualizacao de usuario
@app.route('/user', methods=['POST'])
def postUser():
    name_user = request.args.post('nomeUser')
    email_user = request.args.post('emailUser')
    password = request.args.post('senha')
    about_user = request.args.post('sobre')
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    # if(name_user == '' or email_user == '' or password == ''):
    #     return handle_invalid('Empty parameters')
    # else:
    #     new_user = None
    #     if(about_user != None and about_user != ''):
    #         new_user = Usuario(nome = name_user, email = name_user, senha = password, sobre = about_user)
    #     else:
    #         new_user = Usuario(nome = name_user, email = name_user, senha = password)
    #     print(new_user.nome)
    #     new_user.save()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Rota para busca de usuario
@app.route('/user', methods=['GET'])
def getUser():
    name_user = request.args.get('nomeUser')
    email_user = request.args.get('emailUser')
    password = request.args.get('senha')
    about_user = request.args.get('sobre')
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


        

def handle_invalid(erroType):
    response = jsonify(erroType)
    response.status_code = 400
    return response
