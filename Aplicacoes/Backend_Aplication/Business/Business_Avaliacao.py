# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Usuario as User
import Model.Servico as Servico
import Model.Avaliacao as Avaliacao
# ---------------------------------

def createAvaliacao(avalicao_data:dict):
    related_user = User.Usuario.get_by_id(avalicao_data['user_id'])
    related_servico = Servico.Servico.get_by_id(avalicao_data['service_id'])
    new_avaliacao = Avaliacao.Avaliacao(id_usuario=related_user, id_servico=related_servico, nota=avalicao_data['nota'])
    try:
        new_avaliacao.create_table()
        new_avaliacao.save()
        return True
    except Exception as err:
        print(err)
        return False

##avaliacao so se atualiza a nota registrada
def updateAvaliacao(avaliacao_data:dict):
    old_avaliacao = Avaliacao.Avaliacao.get_by_id(avaliacao_data['avaliacao_id'])

    have_nota = avaliacao_data['nota'] != '' and avaliacao_data['nota'] != None
    
    if(have_nota):
        old_avaliacao.nota = avaliacao_data['nota']
        old_avaliacao.save()
        return True
    else:
        print('any valid information wasn\'t passed')
        return False

def findAvaliacao(query_data:dict):
    result_query = None
    final_result = []
    have_id = query_data['avaliacao_id'] != '' and query_data['avaliacao_id'] != None
    if(have_id):
        result_query = Avaliacao.Avaliacao.get_by_id(query_data['avaliacao_id'])
        final_result.append(_makeDic(result_query))
        return final_result
    
    have_nota = query_data['nota'] != '' and query_data['nota'] != None
    have_user = query_data['user_id'] != '' and query_data['user_id'] != None
    have_serv = query_data['service_id'] != '' and query_data['service_id'] != None

    if(have_nota):
        if(have_user and have_serv):
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.nota >(0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.nota <(-0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.id_usuario == query_data['user_id'] )&
            (Avaliacao.Avaliacao.id_servico == query_data['service_id'])
            )
        elif(have_user):
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.nota >(0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.nota <(-0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.id_usuario == query_data['user_id'] )
            )
        elif(have_serv):
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.nota >(0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.nota <(-0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.id_servico == query_data['service_id'])
            )
        else:
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.nota >(0.1)+query_data['nota'] )&
            (Avaliacao.Avaliacao.nota <(-0.1)+query_data['nota'] )
            )
    if(have_user):
        if(have_serv):
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.id_usuario == query_data['user_id'] )&
            (Avaliacao.Avaliacao.id_servico == query_data['service_id'])
            )
        else:
            result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.id_usuario == query_data['user_id'] )
            )
    else:
        result_query = Avaliacao.Avaliacao.select().where( (Avaliacao.Avaliacao.id_servico == query_data['service_id'])
            )
    for avaliacao_find in result_query:
        final_result.append(_makeDic(avaliacao_find))
    return final_result


def _makeDic(avaliacao_obj):
    avaliacao_dic = {
        'id_avaliacao':avaliacao_obj.id_avaliacao,
        'nota':avaliacao_obj.nota,
        'id_usuario':avaliacao_obj.id_usuario.usuario_id,
        'id_servico':avaliacao_obj.id_servico.id_servico
    }
    return avaliacao_dic