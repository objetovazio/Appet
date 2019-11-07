# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Usuario as User
import Model.Endereco as Address
# ---------------------------------


def createUserAddress(address_data: dict):
    try:
        user_related = User.Usuario.get_by_id(address_data['user_id'])
        new_address = Address.Endereco(id_usuario=user_related, cep=address_data['cep'], nome_bairro=address_data['bairro'],
                                        nome_cidade=address_data['city'], nome_estado=address_data['state'], num_endereco=address_data['num'])
        new_address.create_table()
        new_address.save()
        return True
    except Exception as err:
        print(err)
        return False

def  updateUserAddress(address_data:dict):
    old_address = Address.Endereco.get_by_id(address_data['address_id'])

    have_cep = address_data['cep'] != '' and address_data['cep'] != None
    have_bairro = address_data['bairro'] != '' and address_data['bairro'] != None
    have_city = address_data['city'] != '' and address_data['city'] != None
    have_state = address_data['state'] != '' and address_data['state'] != None
    have_num = address_data['num'] != '' and address_data['num'] != None

    old_address.cep = address_data['cep'] if have_cep else old_address.cep
    old_address.bairro = address_data['bairro'] if have_bairro else old_address.bairro
    old_address.nome_cidade = address_data['city'] if have_city else old_address.nome_cidade
    old_address.nome_estado = address_data['state'] if have_state else old_address.nome_estado
    old_address.num_endereco = address_data['num'] if have_num else old_address.num_endereco
    try:
        old_address.save()
        return True
    except Exception as err:
        print(err)
        return False

def findAddress(query_data:dict):
    result_query = None
    final_result = []
    have_id = query_data['address_id'] != '' and query_data['address_id'] != None
    if(have_id):
        result_query = Address.Endereco.get_by_id(query_data['address_id'])
        final_result.append(_makeDic(result_query))
        return final_result

    have_user = query_data['user_id'] != '' and query_data['user_id'] != None
    if(have_user):
        result_query = Address.Endereco.select().where((Address.Endereco.id_usuario == query_data['user_id']))
        for address_find in result_query:
            final_result.append(_makeDic(address_find))
        return final_result

    have_cep = query_data['cep'] != '' and query_data['cep'] != None
    have_bairro = query_data['bairro'] != '' and query_data['bairro'] != None
    have_city = query_data['city'] != '' and query_data['city'] != None
    have_state = query_data['state'] != '' and query_data['state'] != None
    have_num = query_data['num'] != '' and query_data['num'] != None

    if(have_cep):
        if(have_bairro and have_city and have_state and have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        elif (have_bairro):
            if(have_city and have_state):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
            elif (have_city and have_num):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            elif (have_state and have_num):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_cidade.contains(query_data['bairro']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            elif (have_state):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
            elif (have_city):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city'])) )
            elif (have_num):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            else:
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_bairro.contains(query_data['bairro'])) )
        elif(have_city):
            if(have_state and have_num):
                result_query = result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            elif(have_state):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
            elif (have_num):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            else:
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_cidade.contains(query_data['city'])) )
        elif(have_state):
            if(have_num):
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
            else:
                result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
        elif(have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) &
            (Address.Endereco.num_endereco == query_data['num']) )
        else:
            result_query = Address.Endereco.select().where((Address.Endereco.cep == query_data['cep']) )
    elif(have_bairro):
        if(have_city and have_state and have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        elif(have_city and have_state):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
        elif(have_city and have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        elif(have_state and have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        elif(have_city):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_cidade.contains(query_data['city'])) )
        elif(have_state):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
        elif(have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        else:
            result_query = Address.Endereco.select().where((Address.Endereco.nome_bairro.contains(query_data['bairro'])) )
    elif(have_city):
        if(have_state and have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        elif(have_state):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.nome_estado.contains(query_data['state'])) )
        elif(have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_cidade.contains(query_data['city']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        else:
            result_query = Address.Endereco.select().where((Address.Endereco.nome_cidade.contains(query_data['city'])) )
    elif(have_state):
        if(have_num):
            result_query = Address.Endereco.select().where((Address.Endereco.nome_estado.contains(query_data['state']))&
            (Address.Endereco.num_endereco == query_data['num']) )
        else:
            result_query = Address.Endereco.select().where((Address.Endereco.nome_estado.contains(query_data['state'])))
    else:
        result_query = Address.Endereco.select().where((Address.Endereco.num_endereco == query_data['num']) )
    
    for address_find in result_query:
        final_result.append(_makeDic(address_find))

    return final_result 

def _makeDic(address_obj:Address.Endereco):
    address_dict = {
        'id_address':address_obj.id_endereco,
        'id_user':address_obj.id_usuario.usuario_id,
        'cep':address_obj.cep,
        'bairro':address_obj.nome_bairro,
        'city':address_obj.nome_cidade,
        'state':address_obj.nome_estado,
        'num':address_obj.num_endereco
    }
    return address_dict