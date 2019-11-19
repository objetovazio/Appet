# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import json
import Model.TipoServico as TS
import Model.Usuario as User
import Model.Servico as Serv
import Model.ServicoHorario as SH
import Model.HorarioServico as HS
from peewee import fn
# ---------------------------------


def createService(serv_data: dict):
	convert_data = {
		'title': serv_data['title'],
		'about': serv_data['about'],
		'price': json.loads(serv_data['price']),
		'owner': json.loads(serv_data['owner']),
		'type': json.loads(serv_data['type']),
		'hour': json.loads(serv_data['hour'])
	}
	new_type = TS.TipoServico.get_by_id(convert_data['type'])
	new_owner = User.Usuario.get_by_id(convert_data['owner'])
	new_serv = Serv.Servico(titulo=convert_data['title'], descricao=convert_data['about'],
							preco=convert_data['price'], id_usuario=new_owner, id_tipo=new_type)
	try:
		new_serv.save()
		for horario_prestacao in convert_data['hour']:
			new_horario = HS.HorarioServico.get_by_id(horario_prestacao)
			new_link = SH.ServicoHorario(
				id_servico=new_serv, id_horarioservico=new_horario)
			new_link.save()
	except Exception as err:
		print(err)
		return False
	return True


# caso seja passado horarios novos, todos os antigos ligados ao servico sao apagados e colocado os novos
def updateService(serv_data: dict):

	old_serv = Serv.Servico.get_by_id(int(serv_data['service_id']))
	is_title_empty = serv_data['title'] == None or serv_data['title'] == ''
	is_about_empty = serv_data['about'] == None or serv_data['about'] == ''
	is_price_empty = serv_data['price'] == None or serv_data['price'] == ''
	is_owner_empty = serv_data['owner'] == None or serv_data['owner'] == ''
	is_type_empty = serv_data['type'] == None or serv_data['type'] == ''
	is_hour_empty = serv_data['hour'] == None or serv_data['hour'] == ''

	convert_data = {
		'title': serv_data['title'] if not is_title_empty else old_serv.titulo,
		'about': serv_data['about'] if not is_about_empty else old_serv.descricao,
		'price': json.loads(serv_data['price']) if not is_price_empty else old_serv.preco,
		'owner': User.Usuario.get_by_id(int(serv_data['owner'])) if not is_owner_empty else old_serv.usuario_id,
		'type': TS.TipoServico.get_by_id(int(serv_data['type'])) if not is_type_empty else old_serv.id_tipo,
		'hour': json.loads(serv_data['hour']) if not is_hour_empty else None
	}

	old_serv.titulo = convert_data['title']
	old_serv.descricao = convert_data['about']
	old_serv.preco = convert_data['price']
	old_serv.id_tipo = convert_data['type']
	try:
		if(convert_data['hour'] != None):

			old_collector = SH.ServicoHorario.delete().where((SH.ServicoHorario.id_servico == old_serv)).execute()
			for new_schedules in convert_data['hour']:
				schedule_obj = HS.HorarioServico.get_by_id(new_schedules)
				schedule_link = SH.ServicoHorario(
					id_servico=old_serv, id_horarioservico=schedule_obj)
				schedule_link.save()

		old_serv.save
	except Exception as err:
		print(err)
		return False
	return True

#adicionar tipo e dono do servico nos parametros de busca
def searchService(serv_query):
	result_query = None
	final_result = []
	if(serv_query['id_service']!= None):
		result_query = Serv.Servico.get_by_id(serv_query['id_service'])
		final_result.append(_makeDic(result_query))
		return final_result

	have_title = serv_query['title'] != None
	have_about = serv_query['about'] != None
	have_price = serv_query['price'] != None
	have_owner = serv_query['owner'] != None
	have_type = serv_query['type'] != None
	if(have_owner):
		serv_query['owner'] = json.loads(serv_query['owner'])
	if(have_title):
		if(have_about and have_price and have_owner and have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.id_tipo == serv_query['type'])&
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_about):
			if(have_price and have_owner):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			elif(have_price and have_type):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			elif(have_type and have_owner):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
			elif (have_price):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			elif(have_owner):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) 
			)
			elif(have_type):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
			else:
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.descricao.contains(serv_query['about']))
			)
		elif(have_price):
			if(have_owner and have_type):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			elif(have_owner):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			elif(have_type):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
			else:
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_owner):
			if(have_type):
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
			else:
				result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) 
			)
		else:
			result_query = Serv.Servico.select().where(
			(Serv.Servico.titulo.contains(serv_query['titulo']))&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
	
	elif(have_about):
		if(have_price and have_owner and have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_price and have_owner):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_price and have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_type and have_owner):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
		elif (have_price):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_owner):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) 
			)
		elif (have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.descricao.contains(serv_query['about'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
		else:
			result_query = Serv.Servico.select().where(
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.descricao.contains(serv_query['about']))
			)
	
	elif(have_price):
		if(have_owner and have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.id_tipo == serv_query['type'])&
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_owner):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		elif(have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.id_tipo == serv_query['type']) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
		else:
			result_query = Serv.Servico.select().where(
			(Serv.Servico.preco < (0.5)+float(serv_query['price'])) &
			(Serv.Servico.is_deleted == 0) &
            (Serv.Servico.preco > (-0.5)+float(serv_query['price']))
			)
	
	elif(have_owner):
		if(have_type):
			result_query = Serv.Servico.select().where(
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) &
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type'])
			)
		else:
			result_query = Serv.Servico.select().where(
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_usuario.in_(serv_query['owner'])) 
			)
	else:
		result_query = Serv.Servico.select().where(
			(Serv.Servico.is_deleted == 0) &
			(Serv.Servico.id_tipo == serv_query['type']) 
			)
	for ser_find in result_query:
		final_result.append(_makeDic(ser_find))
	return final_result

def deleteService(service_ids):
	converted_id = json.loads(service_ids)
	query = Serv.Servico.update(is_deleted = 1).where(Serv.Servico.id_servico.in_(converted_id))
	row_modified = query.execute()
	if(row_modified>0):
		return True
	else:
		return False

#retorna metricas relacionadas ao tipo de servicos cadastrados no sistema
def typeRegistredMetrics():
	query_build = (Serv.Servico
					.select(Serv.Servico.id_tipo, fn.COUNT(Serv.Servico.id_tipo).alias('total') )
					.group_by(Serv.Servico.id_tipo)
					)
	data_result = {}
	for row in query_build:
		data_result[row.id_tipo.nome_tipo] = [row.id_tipo.id_tipo, row.total]
	return data_result


def _makeDic(serv_data):
	result = {
		'id_service': serv_data.id_servico,
		'title': serv_data.titulo,
		'about': serv_data.descricao,
		'price': serv_data.preco,
		'id_user': serv_data.id_usuario.usuario_id,
		'id_type': serv_data.id_tipo.id_tipo
	}
	return result
