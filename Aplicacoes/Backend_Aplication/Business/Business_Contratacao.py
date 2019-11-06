# used to resolve the path problem
import sys
from datetime import date
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Usuario as User
import Model.Servico as Servico
import Model.Contratacao as Contrato
import Model.HorarioServico as HorarioServ
from enum import Enum
# ---------------------------------

class PaymentMethod(Enum):
    BOLETO = 1
    PAYPAL = 2

class PaymentStatus(Enum):
    AGUARDANDO = 1
    CANCELADO = 2
    APROVADO = 3

def createContratacao(contrato_data:dict):
    related_buyer = User.Usuario.get_by_id(contrato_data['id_buyer'])
    related_serv = Servico.Servico.get_by_id(contrato_data['id_service'])
    related_hour = HorarioServ.HorarioServico.get_by_id(contrato_data['hour'])

    d_work = date(int(contrato_data['date_work'][0:4]), int(
            contrato_data['date_work'][4:6]), int(contrato_data['date_work'][6:8]))
    d_req = d_work = date(int(contrato_data['date_request'][0:4]), int(
            contrato_data['date_request'][4:6]), int(contrato_data['date_request'][6:8]))

    nem_contrato = Contrato.Contratacao(
        data_solicitacao = d_req,data_agendamento = d_work,horario_agendamento = related_hour,
        forma_pagamento = contrato_data['payment_method'],valor = contrato_data['price'],
        status_pagamento = contrato_data['payment_status'],token_pagamento = contrato_data['payment_token'],
        id_usuario=related_buyer, id_servico=related_serv,status_contratacao = 1
    )
    try:
        nem_contrato.save()
        return True
    except Exception as err:
        print(err)
        return False

# Only allowed find a Contratacao using :
# ID_CONTRATACAO,TOKEN_PAGAMENTO, ID_USUARIO,ID_SERVICO, FORMA_PAGAMENTO, STATUS_PAGAMENTO
def findContratacao(query_data:dict):
    result_query = None
    final_result = []
    have_id = query_data['id_contratacao'] != None
    if(have_id):
        result_query = Contrato.Contratacao.get_by_id(query_data['id_contratacao'])
        final_result.append(_makeDic(result_query))
        return final_result
    have_token = query_data['payment_token'] != None
    have_user = query_data['id_buyer'] != None
    have_serv = query_data['id_service'] != None
    have_method = query_data['payment_method'] != None
    have_status = query_data['payment_status'] != None
    if(have_token):
        if(have_user and have_serv and have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_user and have_serv and have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif (have_user and have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_user and have_serv and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif (have_serv and have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_user and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif (have_user and have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif (have_user and have_serv):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service'])
            )
        elif(have_serv and have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) 
            )
        elif (have_serv and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_user):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_usuario == query_data['id_buyer'])
            )
        elif(have_serv):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.id_servico == query_data['id_service'])
            )
        elif(have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif(have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token']) &
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        else:
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.token_pagamento == query_data['payment_token'])
            )
    elif (have_user):
        if(have_serv and have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_serv and have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif (have_serv and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif (have_serv):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.id_servico == query_data['id_service'])
            )
        elif(have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif(have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer']) &
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        else:
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_usuario == query_data['id_buyer'])
            )
    elif(have_serv):
        if(have_method and have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        elif(have_method):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
        elif (have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_servico == query_data['id_service']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        else:
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.id_servico == query_data['id_service'])
            )
    elif (have_method):
        if(have_status):
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method']) &   
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )
        else:
            result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.forma_pagamento == query_data['payment_method'])
            )
    else:
        result_query = Contrato.Contratacao.select().where(
                (Contrato.Contratacao.status_pagamento == query_data['payment_status'])
            )

    for find_contrato in result_query:
        final_result.append(_makeDic(find_contrato))
    return final_result


def _makeDic(contrato_obj:Contrato.Contratacao):
    contrato_dic ={
    'id_contratacao':contrato_obj.id_contratacao,
    'data_solicitacao':contrato_obj.data_solicitacao,
    'data_agendamento':contrato_obj.data_agendamento,
    'forma_pagamento':contrato_obj.forma_pagamento,
    'valor':contrato_obj.valor,
    'status_pagamento':contrato_obj.status_pagamento,
    'token_pagamento':contrato_obj.token_pagamento,
    'status_contratacao':contrato_obj.status_contratacao,
    'id_usuario':contrato_obj.id_usuario.id_usuario,
    'id_servico':contrato_obj.id_servico.id_servico
    }
    return contrato_dic