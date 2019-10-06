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
from Business.Business_user import *

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
    try:
        is_name_empty = request.form['nomeUser'] == '' or request.form['nomeUser'] == None
        name_user = request.form['nomeUser'] if not is_name_empty else None

        is_email_empty = request.form['emailUser'] == '' or request.form['emailUser'] == None
        email_user = request.form['emailUser'] if not is_email_empty else None
        
        is_password_empty = request.form['senha'] == '' or request.form['senha'] == None
        password = request.form['senha'] if not is_password_empty else None

        is_about_empty = request.form['sobre'] == '' or request.form['sobre'] == None
        about_user = request.form['sobre'] if not is_about_empty else None
        
        is_user_update = request.form['userId'] != '' and request.form['userId']
        if (is_name_empty or is_email_empty or is_password_empty):
            raise Exception('empty required parameter')
    except Exception as err:
        return handle_invalid(err)
    user_data = {'name': name_user,
                'email': email_user,
                'password': password,
                'about':about_user}
    request_result = None
    if(is_user_update):
        request_result = updateUser(user_data, request.form['userId'])
    else:
        request_result = createUser(user_data)

    return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}

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
    response = jsonify(str(erroType))
    response.status_code = 400
    return response
