# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Cartao as Card
import Model.Usuario as User
# ---------------------------------


def createCard(cardData: dict):
	try:
		user_related = User.Usuario.get_by_id(int(cardData['user_id']))
		new_card_info = Card.Cartao(id_usuario=user_related, nome_titular=cardData['owner_name'], validade=cardData[
									'expiration'], cpf_titular=cardData['cpf'], numero_cartao=cardData['number'])
		new_card_info.create_table()
		new_card_info.save()
		return True
	except Exception as err:
		print(err)
		return False


def updateCard(cardData: dict):
	old_card = Card.Cartao.get_by_id(int(cardData['card_id']))

	have_titular = cardData['owner_name'] != '' and cardData['owner_name'] != None
	have_validade = cardData['expiration'] != '' and cardData['expiration'] != None
	have_cpf = cardData['cpf'] != '' and cardData['cpf'] != None
	have_numero = cardData['number'] != '' and cardData['number'] != None

	new_titular = cardData['owner_name'] if have_titular else old_card.nome_titular
	new_validade = cardData['expiration'] if have_validade else old_card.validade
	new_cpf = cardData['cpf'] if have_cpf else old_card.cpf_titular
	new_numero = cardData['number'] if have_numero else old_card.numero_cartao

	old_card.nome_titular = new_titular
	old_card.validade = new_validade
	old_card.cpf_titular = new_cpf
	old_card.numero_cartao = new_numero
	try:
		old_card.save()
		return True
	except Exception as err:
		print(err)
		return False


def findCard(queryData: dict):
	result_query = None
	have_id = queryData['card_id'] != '' and queryData['card_id'] != None
	if(have_id):
		result_query = Card.Cartao.get_by_id(int(queryData['card_id']))

	have_titular = queryData['owner_name'] != '' and queryData['owner_name'] != None
	have_validade = queryData['expiration'] != '' and queryData['expiration'] != None
	have_cpf = queryData['cpf'] != '' and queryData['cpf'] != None
	have_numero = queryData['number'] != '' and queryData['number'] != None

	if(have_titular):
		if(have_cpf and have_numero and have_validade):
			result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.numero_cartao == queryData('number')) &
													  (Card.Cartao.validade == queryData('expiration')))
		elif(have_cpf):
			if(have_numero):
				result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.numero_cartao == queryData('number')))
			elif(have_validade):
				result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.validade == queryData('expiration')))
			else:
				result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.cpf_titular == queryData('cpf')))
		elif(have_numero):
			if(have_validade):
				result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.numero_cartao == queryData('number')) &
													  (Card.Cartao.validade == queryData('expiration')))
			else:
				result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.numero_cartao == queryData('number')))
		elif(have_validade):
			result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))) &
													  (Card.Cartao.validade == queryData('expiration')))
		else:
			result_query = Card.Cartao.select().where((Card.Cartao.nome_titular.contains(queryData('owner_name'))))
	elif(have_cpf):
		if(have_numero and have_validade):
			result_query = Card.Cartao.select().where((Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.numero_cartao == queryData('number')) &
													  (Card.Cartao.validade == queryData('expiration')))
		elif(have_numero):
			result_query = Card.Cartao.select().where((Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.numero_cartao == queryData('number')))
		elif(have_validade):
			result_query = Card.Cartao.select().where((Card.Cartao.cpf_titular == queryData('cpf')) &
													  (Card.Cartao.validade == queryData('expiration')))
		else:
			result_query = Card.Cartao.select().where((Card.Cartao.cpf_titular == queryData('cpf')))
	elif(have_numero):
		if(have_validade):
			result_query = Card.Cartao.select().where((Card.Cartao.numero_cartao == queryData('number')) &
													  (Card.Cartao.validade == queryData('expiration')))
		else:
			result_query = Card.Cartao.select().where((Card.Cartao.numero_cartao == queryData('number')))
	elif(have_validade):
		result_query = Card.Cartao.select().where((Card.Cartao.validade == queryData('expiration')))
	else:
		return 0
	final_result = []
	for result in result_query:
		final_result.append(_makeDic(result))
	return final_result

def _makeDic(card_data):
	card_dic = {
		'id': card_data.id_cartao,
		'nome_titular': card_data.nome_titular,
		'validade':card_data.validade,
		'cpf_titular':card_data.cpf_titular,
		'numero_cartao':card_data.numero_cartao,
		'id_usuario':card_data.id_usuario.id_usuario
	}
	return card_dic