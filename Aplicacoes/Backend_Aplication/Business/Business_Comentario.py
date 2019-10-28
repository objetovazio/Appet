# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Comentario as Comentario
import Model.Avaliacao as Avaliacao
# ---------------------------------

def createComentario(comentario_data:dict):
    related_avaliacao = Avaliacao.Avaliacao.get_by_id(comentario_data['aval_id'])
    new_comentario = Comentario.Comentario(comentario = comentario_data['comentario'], id_avaliacao=related_avaliacao)
    try:
        new_comentario.save()
        return True
    except Exception as err:
        print(err)
        return False

def updateComentario(comentario_data:dict):
    old_comentario = Comentario.Comentario.get_by_id(comentario_data['comentario_id'])
    have_comentario = comentario_data['comentario'] != '' and comentario_data['comentario'] != None
    if(have_comentario):
        old_comentario.comentario = comentario_data['comentario']
        old_comentario.save()
        return True
    else:
        print('any valid information wasn\'t passed')
        return False

def findComentario(query_data:dict):
    result_query = None
    final_result = []
    have_id = query_data['comentario_id'] != '' and query_data['comentario_id'] != None
    if(have_id):
        result_query = Comentario.Comentario.get_by_id(query_data['comentario_id'])
        final_result.append(_makeDic(result_query))
        return final_result
    
    have_comentario = query_data['comentario'] != '' and query_data['comentario'] != None
    have_avaliacao = query_data['aval_id'] != '' and query_data['aval_id'] != None

    if(have_comentario):
        if(have_avaliacao):
            result_query = Comentario.Comentario.select().where( (Comentario.Comentario.comentario.contains(query_data['comentario']))&
            (Comentario.Comentario.id_avaliacao == query_data['aval_id']) )
        else:
            result_query = Comentario.Comentario.select().where( (Comentario.Comentario.comentario.contains(query_data['comentario'])))
    else:
        result_query = Comentario.Comentario.select().where((Comentario.Comentario.id_avaliacao == query_data['aval_id']) )
    
    for comentario_find in result_query:
        final_result.append(_makeDic(comentario_find))
    return final_result

def _makeDic(comentario_obj:Comentario.Comentario):
    comentario_dic = {
        'id_comentario':comentario_obj.id_comentario,
        'comentario':comentario_obj.comentario,
        'id_avaliacao':comentario_obj.id_avaliacao
    }
    return comentario_dic