# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.Usuario as User
import Model.Contato as Contato
# ---------------------------------

def createContato(contato_data:dict):
    try:
        user_related = User.Usuario.get_by_id(contato_data['user_id'])
        new_contato = Contato.Contato(tipo = contato_data['tipo'], descricao = contato_data['content'], id_usuario = user_related)
        new_contato.save()
        return True
    except Exception as err:
        print(err)
        return False

def updateContato(contato_data:dict):
    old_contato = Contato.Contato.get_by_id(contato_data['contato_id'])
    have_tipo = contato_data['tipo'] != '' and contato_data['tipo'] != None
    have_descricao = contato_data['content'] != '' and contato_data['content'] != None

    old_contato.tipo = contato_data['tipo'] if have_tipo else old_contato.tipo
    old_contato.descricao = contato_data['content'] if have_descricao else old_contato.descricao
    try:
        old_contato.save()
        return True
    except Exception as err:
        print(err)
        return False

def findContato(query_data:dict):
    have_id = query_data['contato_id'] != None and query_data['contato_id'] != ''
    result_query = None
    final_result = []
    if(have_id):
        result_query = Contato.Contato.get_by_id(query_data['contato_id'])
        final_result.append(_makeDic(result_query))
        return final_result
    have_user = query_data['user_id'] != '' and query_data['user_id'] != None
    have_tipo = query_data['tipo'] != '' and query_data['tipo'] != None
    have_descricao = query_data['content'] != '' and query_data['content'] != None

    if(have_user):
        if(have_tipo and have_descricao):
            result_query = Contato.Contato.select().where( (Contato.Contato.id_usuario == query_data['user_id'])&
            (Contato.Contato.tipo.contains(query_data['tipo']))&
            (Contato.Contato.descricao.contains(query_data['content'])) )
        elif(have_tipo):
            result_query = Contato.Contato.select().where( (Contato.Contato.id_usuario == query_data['user_id'])&
            (Contato.Contato.tipo.contains(query_data['tipo'])) )
        elif (have_descricao):
            result_query = Contato.Contato.select().where( (Contato.Contato.id_usuario == query_data['user_id'])&
            (Contato.Contato.descricao.contains(query_data['content'])) )
        else:
            result_query = Contato.Contato.select().where( (Contato.Contato.id_usuario == query_data['user_id']) )
    elif(have_tipo):
        if(have_descricao):
            result_query = Contato.Contato.select().where( (Contato.Contato.tipo.contains(query_data['tipo']))&
            (Contato.Contato.descricao.contains(query_data['content'])) )
        else:
            result_query = Contato.Contato.select().where( (Contato.Contato.tipo.contains(query_data['tipo'])) )
    else:
        result_query = Contato.Contato.select().where( (Contato.Contato.descricao.contains(query_data['content'])) )
    for contanto_find in result_query:
        final_result.append(_makeDic(contanto_find))
    return final_result

def _makeDic(contato_obj:Contato.Contato):
    contato_dic = {
        'id_usuario': contato_obj.id_usuario.id_usuario,
        'tipo':contato_obj.tipo,
        'descricao':contato_obj.descricao,
        'id_contato':contato_obj.id_contato
    }
    return contato_dic