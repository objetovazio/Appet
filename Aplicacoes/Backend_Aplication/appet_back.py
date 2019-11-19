import os
from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask import session
from flask import make_response
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
import Business.Business_TipoServico as b_tipoServ
import Business.Business_Endereco as b_address
import Business.Business_Contato as b_contato
import Business.Business_Avaliacao as b_avaliacao
import Business.Business_Comentario as b_comentario
import Business.Business_Contratacao as b_contrato
import logging

import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = b'\xc2\xbf\xbf\xe8\x82LA\xd3\xe8\xdd\x84U\xeb\xec\x825uq\xee\x96\x19#i\xe2' #os.urandom(24)
#app.run(debug=True)
CORS(app)
session_time_minute = 60

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		#

		if not token:
			print(" >>>>>> token_required() = Nenhum Usuário Logado!!")
			return json.dumps({'token_required': True}), 200, {'ContentType': 'application/json'}
			# return  jsonify({'message': 'Token inexistente. O usuário deve fazer login.'}), 401
		#

		try:
			dataToken = jwt.decode(token, app.secret_key)
			current_user = b_user.verifyToken(dataToken['user_id'], dataToken['email_user'])
			print(" >>>>>> token_required() = Usuário Logado: " + current_user['email'])	

		except Exception as e:
			print(" >>>>>> token_required() = Token Inválido!! Tire o comentário na função para ver detalhes da exception")
			#print(str(e))
			return json.dumps({'token_required': True, 'Exception': str(e)}), 200, {'ContentType': 'application/json'}
			# return jsonify({'message': 'Token inválido.'}), 401

		return f(current_user, *args, **kwargs)
	#end-decorated

	return decorated
#end-token_required

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/Rate', methods=['POST'])
@token_required
def postRate(current_user):
	try:
		is_author_empty = is_parameter_empty(request.form['author'])
		is_service_empty = is_parameter_empty(request.form['service'])
		is_rate_empty = is_parameter_empty(request.form['nota'])
		if(is_author_empty or is_service_empty or is_rate_empty):
			raise Exception('[RATE - POST] Empty Required Parameter ')
	except Exception as err:
		print(err)
		handle_invalid(err)
	rate_data = {
		'user_id':request.form['author'],
		'service_id':request.form['service'],
		'nota':request.form['nota']
	}
	response_request = None
	try:
		rate_data['avaliacao_id']=request.form['id']
		response_request = b_avaliacao.updateAvaliacao(rate_data)
	except Exception as err:
		if(response_request == None):
			response_request = b_avaliacao.createAvaliacao(rate_data)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/Rate',methods=['GET'])
@token_required
def getRate(current_user):
	try:
		is_author_empty		=	is_parameter_empty(request.args.get('author'))
		is_service_empty	=	is_parameter_empty(request.args.get('service'))
		is_rate_empty		=	is_parameter_empty(request.args.get('nota'))
		is_id_empty			=	is_parameter_empty(request.args.get('id'))
		if(is_author_empty and is_service_empty and is_rate_empty and is_id_empty):
			raise Exception('[RATE - GET] Empty Parameters ')
	except Exception as err:
		print(err)
		handle_invalid(err)
	
	query_data ={
		'user_id':request.args.get('author')if not is_author_empty else None,
		'service_id':request.args.get('service')if not is_service_empty else None,
		'nota':request.args.get('nota')if not is_rate_empty else None,
		'avaliacao_id':request.args.get('id'if not is_id_empty else None)
	}
	data_result = b_avaliacao.findAvaliacao(query_data)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/CrediCard', methods=['POST'])
@token_required
def postCrediCard(current_user):
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/CrediCard', methods=['GET'])
@token_required
def getCrediCard(current_user):
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/Comment', methods=['POST'])
@token_required
def postComment(current_user):
	try:
		is_rateId_empty		=	is_parameter_empty(request.form['avaliacaoId'])
		is_comment_empty	=	is_parameter_empty(request.form['comentario'])

		if(is_rateId_empty or is_comment_empty):
			raise Exception('[COMMENT - POST]  Empty Required Parameter')
	except Exception as err:
		print(err)
		handle_invalid(err)
	
	comment_data={
		'aval_id':request.form['avaliacaoId'],
		'comentario':request.form['comentario']
	}
	
	response_request = None
	try:
		comment_data['comentario_id'] = request.form['id']
		response_request = b_comentario.updateComentario(comment_data)
	except Exception as err:
		if(response_request == None):
			response_request = b_comentario.createComentario(comment_data)
	
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/Comment', methods=['GET'])
@token_required
def getComment(current_user):
	try:
		is_rateId_empty		=	is_parameter_empty(request.args.get['avaliacaoId'])
		is_comment_empty	=	is_parameter_empty(request.args.get['comentario'])
		is_id_empty			=	is_parameter_empty(request.args.get['id'])
		if(is_rateId_empty and is_comment_empty and is_id_empty):
			raise Exception('[COMMENT - GET]  Empty Parameters')
	except Exception as err:
		print(err)
		handle_invalid(err)
	
	query_data= {
		'comentario_id': request.args.get['id'] if not is_id_empty else None,
		'comentario': request.args.get['comentario'] if not is_id_empty else None,
		'aval_id':request.args.get['avaliacaoId'] if not is_rateId_empty else None
	}
	data_result = b_comentario.findComentario(query_data)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/Contact', methods=['POST'])
@token_required
def postContact(current_user):
	try:
		is_owner_empty = is_parameter_empty(request.form['ownerId'])
		is_type_empty = is_parameter_empty(request.form['type'])
		is_content_empty = is_parameter_empty(request.form['content'])
		if(is_owner_empty or is_type_empty or is_content_empty):
			raise Exception('[CONTACT - POST] Empty Required Parameter')
	except Exception as err:
		print(err)
		handle_invalid(err)
	contact_data={
		'owner':request.form['ownerId'],
		'type':request.form['type'],
		'content':request.form['conent']
	}
	
	response_request = None
	try:
		contact_data['id'] = request.form['contactId']
		response_request = b_contato.updateContato(contact_data)
	except Exception as err:
		if(response_request == None):
			response_request = b_contato.createContato(contact_data)
	
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}
	

@app.route('/Contact', methods=['GET'])
@token_required
def getContact(current_user):
	try:
		is_owner_empty = is_parameter_empty(request.args.get('ownerId'))
		is_type_empty = is_parameter_empty(request.args.get('type'))
		is_content_empty = is_parameter_empty(request.args.get('content'))
		is_id_empty = is_parameter_empty(request.args.get('id'))
		if(is_owner_empty and is_type_empty and is_content_empty):
			raise Exception('[CONTACT - GET] No parameters')
	except Exception as err:
		print (err)
		handle_invalid(err)
	query_data ={
		'owner':request.args.get('ownerId') if not is_owner_empty else None,
		'type':request.args.get('type') if not is_type_empty else None,
		'content':request.args.get('content') if not is_content_empty else None,
		'id':request.args.get('id') if not is_id_empty else None
	}
	data_result = b_contato.findContato(query_data)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['POST'])
@token_required
def postAddress(current_user):
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

	print(request.form)
	
	response_request = None
	try:
		address_data['address_id'] = request.form['address_id']
		response_request = b_address.updateUserAddress(address_data)
	except Exception as err:
		if(response_request == None):
			response_request = b_address.createUserAddress(address_data)
	return json.dumps({'success': response_request}), 200, {'ContentType': 'application/json'}

@app.route('/Address', methods=['GET'])
@token_required
def getAddress(current_user):
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
@token_required
def postServiceSchedule(current_user):
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

@app.route('/remove/ServiceSchedule', methods=['POST'])
@token_required
def removeHorario(current_user):
	try:
		is_service_empty = is_parameter_empty(request.form['horarioId'])
		if (is_service_empty):
			raise Exception('[Horario - REMOVE] INVALID REQUEST ')
	except Exception as err:
		print(err)
		handle_invalid(err)
	request_result = b_horarioServico.deleteHorario(request.form['horarioId'])
	if(request_result):
		return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}
	else:
		return json.dumps({'success': request_result}), 500, {'ContentType': 'application/json'}

@app.route('/ServiceSchedule', methods=['GET'])
#@token_required
def getServiceSchedule():
	is_schedule_empty = is_parameter_empty(request.args.get('id'))
	schedule = request.args.get('id') if not is_schedule_empty else None

	is_periodo_empty = is_parameter_empty(request.args.get('periodId'))
	period_id = request.args.get('periodId') if not is_periodo_empty else None
	
	is_begin_empty = is_parameter_empty(request.args.get('beginTime'))
	begin_time = request.args.get('beginTime') if not is_begin_empty else None

	is_end_empty = is_parameter_empty(request.args.get('endTime'))
	end_time = request.args.get('endTime') if not is_end_empty else None

	is_day_empty = is_parameter_empty(request.args.get('weekDay'))
	week_day = request.args.get('weekDay') if not is_day_empty else None

	print(request.args.get)


	if(is_schedule_empty and is_begin_empty and is_end_empty and is_day_empty and is_periodo_empty):
		print('empty request')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	schedule_query = {
		'id':schedule,
		'begin_hour':begin_time ,
		'end_hour':end_time,
		'week_day':week_day,
		'period':period_id
	}
	data_result = b_horarioServico.findSchedule(schedule_query)
	return json.dumps({'success': True,
	'data':data_result}), 200, {'ContentType': 'application/json'}

#datas sao recebidas no formado yyyyMMdd
@app.route('/AtivityTime', methods=['POST'])
@token_required
def postAtivityTime(current_user):
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
@token_required
def getAtivityTime(current_user):
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
	return json.dumps({'success': True,'data':data_result}), 200, {'ContentType': 'application/json'}


@app.route('/Service', methods=['POST'])
@token_required
def postService(current_user):
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
@token_required
def getService(current_user):
	is_title_empty	=	is_parameter_empty(request.args.get('title'))
	title_service	=	request.args.get('title') if not is_title_empty else None

	is_about_empty	=	is_parameter_empty(request.args.get('about'))
	about_service	=	request.args.get('about') if not is_about_empty else None

	is_price_empty	=	is_parameter_empty(request.args.get('price'))
	price_service	=	float(request.args.get('price')) if not is_price_empty else None

	is_owner_empty	=	is_parameter_empty(request.args.get('ownerId'))
	owner_service	=	request.args.get('ownerId') if not is_owner_empty else None
	is_type_empty	=	is_parameter_empty(request.args.get('typeService'))
	type_service	=	request.args.get('typeService')  if not is_type_empty else None	

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

@app.route('/remove/Service', methods=['POST'])
@token_required
def removeService(current_user):
	try:
		is_service_empty = is_parameter_empty(request.form['serviceId'])
		if (is_service_empty):
			raise Exception('[SERVICE - REMOVE] INVALID REQUEST ')
	except Exception as err:
		print(err)
		handle_invalid(err)
	request_result = b_servico.deleteService(request.form['serviceId'])
	if(request_result):
		return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}
	else:
		return json.dumps({'success': request_result}), 500, {'ContentType': 'application/json'}

# Rota para criacao e atualizacao de Tipo de Serviço
@app.route('/TypeService', methods=['POST'])
@token_required
def postTypeService(current_user):
	#Apenas admin pode adicionar novos tipos de serivo.
	if(current_user['admin'] == 1):
		name_service_type = request.form('nomeTipoServico')
		result_request =  b_tipoServ.createTypeService(name_service_type)
		return json.dumps({'success': result_request}), 200, {'ContentType': 'application/json'}
	else:
		response = jsonify(str('[USER - REMOVE] INVALID REQUEST '))
		response.status = 401
		return response
	# ADICIONAR CHAMADA DA CAMADA DE NEGOCIO PARA PROCESSAMENTO
	

# Rota para busca de Tipo de Serviço
@app.route('/TypeService', methods=['GET'])
@token_required
def getTypeService(current_user):
	service_query = {}
	is_name_empty = is_parameter_empty (request.args.get('nomeTipoServico'))
	is_id_empty = is_parameter_empty(request.args.get('idType'))
	
	service_query['nome_ts'] = request.args.get('nomeTipoServico') if not is_name_empty else None
	service_query['id_ts'] = request.args.get('idType') if not is_id_empty else None
	
	data_result = b_tipoServ.findTypeService(service_query)
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

#Apagar um usuario nao significa remover da base e sim desativar
@app.route('/remove/user', methods=['POST'])
@token_required
def deleteUser(current_user):
	try:
		is_user_empty = is_parameter_empty(request.form['userId'])
		if (is_user_empty):
			raise Exception('[USER - REMOVE] INVALID REQUEST ')
	except Exception as err:
		print(err)
		handle_invalid(err)
	request_result = b_user.deleteUser(request.form['userId'])
	if(request_result):
		return json.dumps({'success': request_result}), 200, {'ContentType': 'application/json'}
	else:
		return json.dumps({'success': request_result}), 500, {'ContentType': 'application/json'}


# Rota para busca de usuario
@app.route('/user', methods=['GET'])
@token_required
def getUser(current_user):    
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


# Rota para busca de usuario
@app.route('/currentUser', methods=['GET'])
@token_required
def getCurrentUser(current_user):
		data_result = current_user #b_user.findUsers(user_query)
		return json.dumps({'success': True,
		'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/login', methods=['POST'])
def loginUser():    
	is_email_empty = is_parameter_empty(request.form['emailUser'])
	email_user = request.form['emailUser'] if not is_email_empty else None
		
	is_password_empty = is_parameter_empty(request.form['senha'])
	password = request.form['senha'] if not is_password_empty else None
	
	if(is_email_empty or is_password_empty):
		print('empty')
		return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
	else:
		user_query = {
			'email_user': email_user,
			'password': password
		}
		data_result = b_user.userLogin(user_query)

		if data_result:
			# the token time is defined by session_time_minute variable
			token = jwt.encode({'user_id': data_result['user_id'], 'email_user' : data_result['email'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=session_time_minute)}, app.secret_key)		
			return json.dumps({'success': True, 'token': token.decode('UTF-8')}), 200, {'ContentType': 'application/json'}
		else:
			return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
#end-loginuser

@app.route('/getsession', methods=['GET'])
@token_required
def getSession(current_user):
	if current_user:
		return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

	return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
#end-getrSession

@app.route('/contratacao', methods=['GET'])
@token_required
def getContratacao(current_user):
	try:
		is_id_empty			=	is_parameter_empty(request.args.get('id'))
		is_token_empty		=	is_parameter_empty(request.args.get('token'))
		is_buyer_empty		=	is_parameter_empty(request.args.get('comprador'))
		is_service_empty	=	is_parameter_empty(request.args.get('servico'))
		is_method_empty		=	is_parameter_empty(request.args.get('metodo'))
		is_status_empty		=	is_parameter_empty(request.args.get('status'))
		if(is_id_empty and is_token_empty and is_token_empty and is_service_empty and is_method_empty and is_status_empty):
			raise Exception('[CONTRATACAO - GET] Empty Parameters ')
	except Exception as err:
		print(err)
		return handle_invalid(err)
	query_data = {
		'id_contratacao':request.args.get('id') if not is_id_empty else None,
		'payment_token':request.args.get('token') if not is_token_empty else None,
		'id_buyer':request.args.get('comprador') if not is_buyer_empty else None,
		'id_service':request.args.get('servico') if not is_service_empty else None,
		'payment_method':request.args.get('metodo') if not is_method_empty else None,
		'payment_status':request.args.get('status') if not is_status_empty else None
	}
	data_result = b_contrato.findContratacao(query_data)
	return json.dumps({'success': True,
		'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/contratacao', methods=['POST'])
@token_required
def postContratacao(current_user):
	try:
		is_token_empty		=	is_parameter_empty(request.form['token'])
		is_buyer_empty		=	is_parameter_empty(request.form['comprador'])
		is_service_empty	=	is_parameter_empty(request.form['servico'])
		is_method_empty		=	is_parameter_empty(request.form['metodo'])
		is_status_empty		=	is_parameter_empty(request.form['status'])
		is_request_empty	=	is_parameter_empty(request.form['data_req'])
		is_work_empty		=	is_parameter_empty(request.form['data_serv'])
		is_price_empty		=	is_parameter_empty(request.form['preco'])
		is_hour_empty		=	is_parameter_empty(request.form['horario'])

		have_empty_data = is_request_empty or is_work_empty or is_price_empty or is_hour_empty
		have_empty_data = have_empty_data or  is_token_empty or is_buyer_empty or is_service_empty or is_method_empty or is_status_empty
		if(have_empty_data):
			raise Exception('[CONTRATACAO - POST] Empty required parameter')
	except Exception as err:
		print(err)
		handle_invalid(err)
	
	contratacao_data={
		'payment_token':request.form['token'],
		'id_buyer':request.form['comprador'],
		'id_service':request.form['servico'],
		'payment_method':request.form['metodo'],
		'payment_status':request.form['status'],
		'date_request':request.form['data_req'],
		'date_work':request.form['data_serv'],
		'price':float(request.form['preco']),
		'hour':request.form['horario']
	}
	response_request = None
	try:
		contratacao_data['id_contratacao'] = request.form['id']
	except Exception as err:
		if(response_request == None):
			response_request = b_contrato.createContratacao(contratacao_data)
	return json.dumps({'success': response_request}),200, {'ContentType': 'application/json'}


@app.route('/relatorio/weekDayServices')
def getMetricsWeekDay():
	data_result = b_horarioServico.weekdayMetrics()
	return json.dumps({'success': True,
		'data':data_result}), 200, {'ContentType': 'application/json'}

@app.route('/relatorio/typeServices')
def getMetricsTypeService():
	data_result = b_servico.typeRegistredMetrics()
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