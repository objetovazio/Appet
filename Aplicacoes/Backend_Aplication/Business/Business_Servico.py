# used to resolve the path problem
import Model.TipoServico as TS
import Model.Usuario as User
import Model.Servico as Serv
import Model.ServicoHorario as SH
import Model.HorarioServico as HS
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------


def createService(serv_data, owner_id, type_id):
    new_type = TS.TipoServico.get_by_id(type_id)
    new_owner = User.Usuario.get_by_id(owner_id)
    new_serv = Serv.Servico(titulo=serv_data['title'], descricao=serv_data['about'],
                            preco=serv_data['price'], id_usuario=new_owner, id_tipo=new_type)
    try:
        new_serv.create_table()
        for horario_prestacao in serv_data['hour']:
            new_horario = HS.HorarioServico.get_by_id(horario_prestacao)
            new_link = SH.ServicoHorario(id_usuario = new_owner, id_horarioservico = new_horario)
            new_link.create_table()
            new_link.save()
        new_serv.save()
    except Exception as err:
        print(err)
        return False
    return True


def updateService(serv_data, owner_id, type_id):
    old_serv = Serv.Servico.get_by_id(serv_data['serv_id'])
    old_serv.titulo = serv_data['title']
    old_serv.descricao = serv_data['about']
    old_serv.preco = serv_data['price']
    new_type = TS.TipoServico.get_by_id(type_id)
    old_serv.id_tipo = new_type
    try:
        old_serv.save
    except Exception as err:
        print(err)
        return False
    return True


def searchService(serv_query):
    result_query = None
    if(serv_query('title') != None):
        if(serv_query('about') != None and serv_query('price') != None):
            result_query = Serv.Servico.select().where((Serv.Servico.titulo.contains(serv_query('titulo'))) &
                                                       (Serv.Servico.descricao.contains(serv_query('about'))) &
                                                       (Serv.Servico.preco == serv_query('price')))
        else:
            if(serv_query('about') != None):
                result_query = Serv.Servico.select().where((Serv.Servico.titulo.contains(serv_query('titulo'))) &
                                                           (Serv.Servico.descricao.contains(serv_query('about'))))
            elif(serv_query('price') != None):
                result_query = Serv.Servico.select().where((Serv.Servico.titulo.contains(serv_query('titulo'))) &
                                                           (Serv.Servico.preco == serv_query('price')))
            else:
                result_query = Serv.Servico.select().where(
                    (Serv.Servico.titulo.contains(serv_query('titulo'))))
    elif(serv_query('about') != None):
        if(serv_query('price') != None):
            result_query = Serv.Servico.select().where(((Serv.Servico.descricao.contains(serv_query('about'))) &
                                                        (Serv.Servico.preco == serv_query('price'))))
        else:
            result_query = Serv.Servico.select().where(
                ((Serv.Servico.descricao.contains(serv_query('about')))))
    else:
        result_query = Serv.Servico.select().where(
            ((Serv.Servico.preco == serv_query('price'))))
    final_resul = []
    for ser_find in result_query:
        final_resul.append(_makeDic(ser_find))
    return final_resul

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
