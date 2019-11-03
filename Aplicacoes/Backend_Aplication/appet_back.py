import os
from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask_cors import CORS
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------
import Business.Business_user as b_user
import Business.Business_periodoAtividade as b_periodoAtividade
import Business.Business_HorarioServico as b_horarioServico
import Business.Business_Servico as b_servico
import Business.Business_TipoServico as TS
import Business.Business_Endereco as b_address
import logging

app = Flask(__name__)
#app.run(debug=True)
CORS(app)

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
	try:
		is_user_empty = is_parameter_empty(request.form['userId'])
		is_cep_empty = is_parameter_empty(request.form['cep'])
		is_bairro_empty = is_parameter_empty(request.form['bairro'])
		is_cidade_empty = is_parameter_empty(request.form['cidade'])
		is_estado_empty = is_parameter_empty(request.form['estado'])
		is_num_empty = is_parameter_empty(request.form['numero'])
		if(is_user_empty or is_cep_empty or is_bairro_empty or is_cidade_empty or is_estado_empty or is_num_empty):
			raise Exception('[ADDRESS - POST]Empty Required Parameter')
	except Exception as err:
		print(err)
		handle_invalid(err)
	address_data = {
		'user_id':request.form['userId'],
		'cep':request.form['cep'],
		'bairro':request.form['bairro'],
		'city':request.form['cidade'],
		'state':request.form['estado'],
		'num':request.form['numero']
	}

	response_request = None
	try:
		address_data['id'] = request.form['id']
		response_request = b_address.updateUserAddress(address_data)
	except Exception as err:
		if(response_request == None):
			response_request = b_address.createUserAddress(address_data)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['GET'])
def getAddress():
	is_user_empty	=	is_parameter_empty(request.args.get('userId'))
	is_cep_empty	=	is_parameter_empty(request.args.get('cep'))
	is_bairro_empty	=	is_parameter_empty(request.args.get('bairro'))
	is_cidade_empty	=	is_parameter_empty(request.args.get('cidade'))
	is_estado_empty	=	is_parameter_empty(request.args.get('estado'))
	is_num_empty	=	is_parameter_empty(request.args.get('numero'))
	if(is_user_empty and is_cep_empty and is_bairro_empty and is_cidade_empty and is_estado_empty and is_num_empty):
		print('empty request')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	query_data ={
		'user_id':		request.args.get('userId'),
		'cep':			request.args.get('cep'),
		'bairro':		request.args.get('bairro'),
		'city':			request.args.get('cidade'),
		'state':		request.args.get('estado'),
		'num':			request.args.get('numero'),
		'address_id':	request.args.get('id')
	}
	data_result = b_address.findAddress(query_data)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceSchedule', methods=['POST'])
def postServiceSchedule():
	try:
		is_period_empty = is_parameter_empty(request.form['periodoId'])
		period_id = int(request.form['periodoId']) if not is_period_empty else None

		is_begin_empty = is_parameter_empty(request.form['beginTime'])
		begin_time = request.form['beginTime'] if not is_begin_empty else None

		is_end_empty = is_parameter_empty(request.form['endTime'])
		end_time = request.form['endTime'] if not is_end_empty else None

		is_day_empty = is_parameter_empty(request.form['weekDay'])
		week_day = int(request.form['weekDay']) if not is_day_empty else None

		if(is_period_empty or is_begin_empty or is_end_empty or is_day_empty):
			raise Exception('[Schedule Service - POST]Empty Required Parameter')
	except Exception as err:
		print(err)
		handle_invalid(err)
	schedule_data = {
		'period_id':period_id,
		'begin_hour':begin_time,
		'end_hour':end_time,
		'week_day':week_day
	}
	response_request = None
	try:
		schedule_data['schedule_id'] = request.form['serviceSchedule'] 
		response_request = b_horarioServico.updateSchedule(schedule_data)
	except Exception as err:
		logging.exception("message")
		if(response_request == None):
			response_request = b_horarioServico.createSchedule(schedule_data)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceSchedule', methods=['GET'])
def getServiceSchedule():
	is_period_empty = is_parameter_empty(request.args.get('periodoId'))
	period_id = int(request.form['periodoId']) if not is_period_empty else None

	is_begin_empty = is_parameter_empty(request.args.get('beginTime'))
	begin_time = request.form['beginTime'] if not is_begin_empty else None

	is_end_empty = is_parameter_empty(request.args.get('endTime'))
	end_time = request.args.get('endTime') if not is_end_empty else None

	is_day_empty = is_parameter_empty(request.args.get('weekDay'))
	week_day = int(request.args.get('weekDay')) if not is_day_empty else None

	if(is_period_empty and is_begin_empty and is_end_empty and is_day_empty):
		print('empty request')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	schedule_query = {
		'period_id':period_id,
		'begin_hour':begin_time,
		'end_hour':end_time,
		'week_day':week_day
	}
	data_result = b_horarioServico.findSchedule(schedule_query)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

#datas sao recebidas no formado yyyyMMdd
@app.route('/AtivityTime', methods=['POST'])
def postAtivityTime():
	try:
		is_begin_empty = is_parameter_empty(request.form['beginDate'])
		begin_date = request.form['beginDate'] if not is_begin_empty else None

		is_end_empty = is_parameter_empty(request.form['endDate'])
		end_date = request.form['endDate'] if not is_end_empty else None

		is_owner_empty = is_parameter_empty(request.form['ownerId'])
		owner_id = int(request.form['ownerId']) if not is_owner_empty else None
		
		is_periodoAtvidadeId_empty =  is_parameter_empty( request.form['periodoAtvidadeId'] )
		periodoAtvidadeId = int(request.form['periodoAtvidadeId']) if not is_periodoAtvidadeId_empty else None
		
		if(is_begin_empty or is_end_empty or is_owner_empty):
			raise Exception('empty required parameter')
	except Exception as err:
		return handle_invalid(err)
	ativity_time = {
		'begin':begin_date,
		'end':end_date
	}
	response_request = None

	try:
		#usado para verificar se é update ou create
		if (periodoAtvidadeId == None):
			response_request = b_periodoAtividade.createPeriodoAtividade(ativity_time, owner_id)
		else:
			response_request = b_periodoAtividade.updatePeriodoAtividade(ativity_time, periodoAtvidadeId)
		
		if (response_request == False):
			raise Exception('Erro no Banco de Dados')

		return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

	except Exception as err:
		return erro_interno(err)


@app.route('/AtivityTime', methods=['GET'])
def getAtivityTime():
	is_begin_empty = is_parameter_empty(request.args.get('beginDate'))
	begin_date = request.args.get('beginDate') if not is_begin_empty else None

	is_end_empty = is_parameter_empty(request.args.get('endDate'))
	end_date = request.args.get('endDate') if not is_end_empty else None

	is_owner_empty = is_parameter_empty(request.args.get('ownerId'))
	owner_id = int(request.args.get('ownerId')) if not is_owner_empty else None

	is_id_empty = is_parameter_empty(request.args.get('paId'))
	id_pa = int(request.args.get('paId')) if not is_id_empty else None

	if(is_begin_empty and is_end_empty and is_owner_empty):
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}  

	ativity_time = {
		'begin':begin_date,
		'end':end_date,
		'owner_id':owner_id,
		'id':id_pa
	}

	data_result = b_periodoAtividade.findPeriodoAtividade(ativity_time)
	print(ativity_time)
	print(data_result)
	return json.dumps({'success': True,'data':data_result}), 200, {'ContentType': 'application/json'}


@app.route('/Service', methods=['POST'])
def postService():
	try:
		is_title_empty = is_parameter_empty(request.form['title'])
		title_service = request.form['title'] if not is_title_empty else None

		is_about_empty = is_parameter_empty(request.form['about'])
		about_service = request.form['about'] if not is_about_empty else None

		is_price_empty = is_parameter_empty(request.form['price'])
		price_service = request.form['price'] if not is_price_empty else None

		is_owner_empty = is_parameter_empty(request.form['ownerId'])
		owner_service = request.form['ownerId'] if not is_owner_empty else None

		is_type_empty = is_parameter_empty(request.form['typeService'])
		type_service = request.form['typeService']  if not is_type_empty else None

		is_hours_empty = is_parameter_empty(request.form['hourService'])
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
		'type':type_service,
		'hour':hours_service
	}
	response_request = None
	try:
		service_request['service_id'] = request.form['serviceId']
		response_request = b_servico.updateService(service_request)
	except Exception as err:
		if (response_request == None):
			response_request = b_servico.createService(service_request)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/Service', methods=['GET'])
def getService():
	is_title_empty	=	is_parameter_empty(request.args.get('title'))
	title_service	=	request.args.get('title') if not is_title_empty else None

	is_about_empty	=	is_parameter_empty(request.args.get('about'))
	about_service	=	request.args.get('about') if not is_about_empty else None

	is_price_empty	=	is_parameter_empty(request.args.get('price'))
	price_service	=	float(request.args.get('price')) if not is_price_empty else None

	is_owner_empty	=	is_parameter_empty(request.args.get('ownerId'))
	owner_service	=	int(request.args.get('ownerId')) if not is_owner_empty else None

	is_type_empty	=	is_parameter_empty(request.args.get('typeService'))
	type_service	=	int(request.args.get('typeService'))  if not is_type_empty else None	

	is_id_empty		=	is_parameter_empty(request.args.get('service_id'))
	id_service		=	int(request.args.get('service_id') ) if not is_id_empty else None

	if(is_title_empty and is_about_empty and is_price_empty and is_owner_empty and is_type_empty and is_id_empty):
		print('empty')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	request_query = {
		'title':title_service,
		'about':about_service,
		'price':price_service,
		'owner':owner_service,
		'type':type_service,
		'id_service':id_service
	}
	data_result = b_servico.searchService(request_query)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

# Rota para criacao e atualizacao de Tipo de Serviço
@app.route('/TypeService', methods=['POST'])
def postTypeService():
	name_service_type = request.form('nomeTipoServico')
	print(name_service_type)
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Rota para busca de Tipo de Serviço
@app.route('/TypeService', methods=['GET'])
def getTypeService():
	service_query = {}
	have_name = not is_parameter_empty(request.args.get('nomeTipoServico'))
	if(have_name):
		service_query['nome_ts'] = request.args.get('nomeTipoServico')
	else:
		service_query['nome_ts'] = None
	service_query['id_ts'] = None
	data_result = TS.findTypeService(service_query)
	return json.dumps({'success': True,
		'data':data_result}), 200, {'ContentType': 'application/json'}

# Rota para criacao e atualizacao de usuario
@app.route('/user', methods=['POST'])
def postUser():
	try:
		is_name_empty = is_parameter_empty(request.form['nomeUser'])
		name_user = request.form['nomeUser'] if not is_name_empty else None

		is_email_empty = is_parameter_empty(request.form['emailUser'])
		email_user = request.form['emailUser'] if not is_email_empty else None
		
		is_password_empty = is_parameter_empty(request.form['senha'])
		password = request.form['senha'] if not is_password_empty else None

		is_about_empty = is_parameter_empty(request.form['sobre'])
		about_user = request.form['sobre'] if not is_about_empty else None
		
		is_user_update = not is_parameter_empty(request.form['userId'])
		if (is_name_empty or is_email_empty or is_password_empty):
			raise Exception('empty required parameter')
	except Exception as err:
		return handle_invalid(err)
	user_data = {'name': name_user,
				'email': email_user,
				'password': password,
				'about':about_user}
	request_result = None

	try:
		if(is_user_update):
			request_result = b_user.updateUser(user_data, request.form['userId'])
		else:
			if(request_result == None):
				request_result = b_user.createUser(user_data)
		
		if (request_result == False):
			raise Exception('Erro no Banco de Dados')
		return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}
	except Exception as err:
		return erro_interno(err)

# Rota para busca de usuario
@app.route('/user', methods=['GET'])
def getUser():    
	is_name_empty =  is_parameter_empty(request.args.get('nomeUser'))
	name_user = request.args.get('nomeUser') if not is_name_empty else None    

	is_email_empty = is_parameter_empty(request.args.get('emailUser'))
	email_user = request.args.get('emailUser') if not is_email_empty else None

	is_about_empty = is_parameter_empty(request.args.get('sobre'))
	about_user = request.args.get('sobre') if not is_about_empty else None

	is_id_empty = is_parameter_empty(request.args.get('userId'))
	user_id = request.args.get('userId') if not is_id_empty else None

	if( is_name_empty and is_email_empty and is_about_empty and is_id_empty):
		print('empty')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	else:
		user_query = {
			'user_name': name_user,
			'email_user': email_user,
			'about_user': about_user,
			'user_id': user_id
		}
		data_result = b_user.findUsers(user_query)
		return json.dumps({'success': True,
		'data':data_result}), 200, {'ContentType': 'application/json'}
	


		

def handle_invalid(erroType):
	response = jsonify(str(erroType))
	response.status_code = 400
	return response

def erro_interno (erroType):
	response = jsonify(str(erroType))
	response.status_code = 500
	return response

def is_parameter_empty(pass_parameter:str):
	return pass_parameter == None or pass_parameter == ''