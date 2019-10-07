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
import Business.Business_user as b_user
import Business.Business_periodoAtividade as b_periodoAtividade

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

#datas sao recebidas no formado yyyyMMdd
@app.route('/AtivityTime', methods=['POST'])
def postAtivityTime():
    try:
        is_begin_empty = request.form['beginDate'] == '' or request.form['beginDate'] == None
        begin_date = request.form['beginDate'] if not is_begin_empty else None

        is_end_empty = request.form['endDate'] == '' or request.form['endDate'] == None
        end_date = request.form['endDate'] if not is_end_empty else None

        is_owner_empty = request.form['ownerId'] == '' or request.form['ownerId'] == None
        owner_id = request.form['ownerId'] if not is_owner_empty else None

        if(is_begin_empty or is_end_empty or is_owner_empty):
            raise Exception('empty required parameter')
    except Exception as err:
        return handle_invalid(err)
    ativity_time = {
        'begin':begin_date,
        'end':end_date
    }
    response_request = None
    if(request.form['periodoAtvidadeId']!= '' or request.form['periodoAtvidadeId']!= None):
        response_request = b_periodoAtividade.updatePeriodoAtividade(ativity_time,request.form['periodoAtvidadeId'])
    else:
        response_request = b_periodoAtividade.createPeriodoAtividade(ativity_time,owner_id)
    # ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
    return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/AtivityTime', methods=['GET'])
def getAtivityTime():
    is_begin_empty = request.args.get('beginDate') == '' or request.args.get('beginDate') == None
    begin_date = request.args.get('beginDate') if not is_begin_empty else None

    is_end_empty = request.args.get('endDate') == '' or request.args.get('endDate') == None
    end_date = request.args.get('endDate') if not is_end_empty else None

    is_owner_empty = request.args.get('ownerId') == '' or request.args.get('ownerId') == None
    owner_id = request.args.get('ownerId') if not is_owner_empty else None

    if(is_begin_empty and is_end_empty and is_owner_empty):
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}        
    ativity_time = {
        'begin':begin_date,
        'end':end_date,
        'owner_id':owner_id
    }
    data_result = b_periodoAtividade.findPeriodoAtividade(ativity_time)
    return json.dumps({'success': True,
        'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/Service', methods=['POST'])
def postService():
    try:
        is_title_empty = request.form['title'] == '' or request.form['title'] == None
        title_service = request.form['title'] if not is_title_empty else None

        is_about_empty = request.form['about'] == '' or request.form['about'] == None
        about_service = request.form['about'] if not is_about_empty else None

        is_price_empty = request.form['price'] == '' or request.form['price'] == None
        price_service = request.form['price'] if not is_price_empty else None

        is_owner_empty = request.form['ownerId'] == '' or request.form['ownerId'] == None
        owner_service = request.form['ownerId'] if not is_owner_empty else None

        is_type_empty = request.form['typeService'] == '' or request.form['typeService'] == None
        type_service = request.form['typeService']  if not is_type_empty else None

        is_hours_empty = request.form['hourService'] == '' or request.form['hourService'] == None
        hours_service = request.form['hourService'] if not is_hours_empty else None
        
        if(is_title_empty and is_about_empty and is_price_empty and is_owner_empty and is_type_empty and is_hours_empty):
            raise Exception ('empty requeired parameters for creation')

    except Exception as err:
        print (err)
        handle_invalid(err)

    service_request = {
        'title':title_service,
        'about':about_service,
        'price':price_service,
        'owner':owner_service,
        'type':type_service
        'hour':hours_service
    }
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
        print("here")
        request_result = b_user.updateUser(user_data, request.form['userId'])
    else:
        request_result = b_user.createUser(user_data)

    return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}

# Rota para busca de usuario
@app.route('/user', methods=['GET'])
def getUser():    
    is_name_empty =  request.args.get('nomeUser') == '' or request.args.get('nomeUser') == None
    name_user = request.args.get('nomeUser') if not is_name_empty else None    

    is_email_empty = request.args.get('emailUser') == '' or request.args.get('emailUser') == None
    email_user = request.args.get('emailUser') if not is_email_empty else None

    is_about_empty = request.args.get('sobre') == '' or request.args.get('sobre') == None
    about_user = request.args.get('sobre') if not is_about_empty else None

    if( is_name_empty and is_email_empty and is_about_empty):
        print('empty')
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        user_query = {
            'user_name': name_user,
            'email_user': email_user,
            'about_user': about_user
        }
        data_result = b_user.findUsers(user_query)
        return json.dumps({'success': True,
        'data':data_result}), 200, {'ContentType': 'application/json'}
    


        

def handle_invalid(erroType):
    response = jsonify(str(erroType))
    response.status_code = 400
    return response
