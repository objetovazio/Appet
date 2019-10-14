# used to resolve the path problem
import Model.Cartao as Card
import Model.Usuario as User
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
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

    have_titular = cardData['owner_name'] == '' or cardData['owner_name'] == None
    have_validade = cardData['expiration'] == '' or cardData['expiration'] == None
    have_cpf = cardData['cpf'] == '' or cardData['cpf'] == None
    have_numero = cardData['number'] == '' or cardData['number'] == None

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