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
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['GET'])
def getAddress():
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceSchedule', methods=['POST'])
def postServiceSchedule():
	try:
		is_period_empty = request.form['periodoId'] == None or request.form['periodoId'] == ''
		period_id = request.form['periodoId'] if not is_period_empty else None

		is_begin_empty = request.form['beginTime'] == None or request.form['beginTime'] == ''
		begin_time = request.form['beginTime'] if not is_begin_empty else None

		is_end_empty = request.form['endTime'] == None or request.form['endTime'] == ''
		end_time = request.form['endTime'] if not is_end_empty else None

		is_day_empty = request.form['weekDay'] == None or request.form['weekDay'] == ''
		week_day = request.form['weekDay'] if not is_day_empty else None

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
		print(request.form['serviceSchedule'])
		schedule_data['schedule_id'] = request.form['serviceSchedule'] 
		response_request = b_horarioServico.updateSchedule(schedule_data)
	except Exception as err:
		logging.exception("message")
		if(response_request == None):
			response_request = b_horarioServico.createSchedule(schedule_data)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/ServiceSchedule', methods=['GET'])
def getServiceSchedule():
	is_period_empty = request.args.get('periodoId') == None or request.args.get('periodoId') == ''
	period_id = request.form['periodoId'] if not is_period_empty else None

	is_begin_empty = request.args.get('beginTime') == None or request.args.get('beginTime') == ''
	begin_time = request.form['beginTime'] if not is_begin_empty else None

	is_end_empty = request.args.get('endTime') == None or request.args.get('endTime') == ''
	end_time = request.args.get('endTime') if not is_end_empty else None

	is_day_empty = request.args.get('weekDay') == None or request.args.get('weekDay') == ''
	week_day = request.args.get('weekDay') if not is_day_empty else None

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
		is_begin_empty = request.form['beginDate'] == '' or request.form['beginDate'] == None
		begin_date = request.form['beginDate'] if not is_begin_empty else None

		is_end_empty = request.form['endDate'] == '' or request.form['endDate'] == None
		end_date = request.form['endDate'] if not is_end_empty else None

		is_owner_empty = request.form['ownerId'] == '' or request.form['ownerId'] == None
		owner_id = request.form['ownerId'] if not is_owner_empty else None
		is_pa_update = request.form['periodoAtvidadeId'] != '' and request.form['periodoAtvidadeId']
		if(is_begin_empty or is_end_empty or is_owner_empty):
			raise Exception('empty required parameter')
	except Exception as err:
		return handle_invalid(err)
	ativity_time = {
		'begin':begin_date,
		'end':end_date
	}
	response_request = None
	if(is_pa_update):
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
	is_title_empty	=	request.args.get('title') == '' or request.args.get('title') == None
	title_service	=	request.args.get('title') if not is_title_empty else None

	is_about_empty	=	request.args.get('about') == '' or request.args.get('about') == None
	about_service	=	request.args.get('about') if not is_about_empty else None

	is_price_empty	=	request.args.get('price') == '' or request.args.get('price') == None
	price_service	=	request.args.get('price') if not is_price_empty else None

	is_owner_empty	=	request.args.get('ownerId') == '' or request.args.get('ownerId') == None
	owner_service	=	request.args.get('ownerId') if not is_owner_empty else None

	is_type_empty	=	request.args.get('typeService') == '' or request.args.get('typeService') == None
	type_service	=	request.args.get('typeService')  if not is_type_empty else None	
	if(is_title_empty and is_about_empty and is_price_empty and is_owner_empty and is_type_empty):
		print('empty')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	request_query = {
		'title':title_service,
		'about':about_service,
		'price':price_service,
		'owner':owner_service,
		'type':type_service
	}
	data_result = b_servico.searchService(request_query)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

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
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
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
