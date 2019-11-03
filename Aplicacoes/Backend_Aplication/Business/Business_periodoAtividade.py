# used to resolve the path problem
from datetime import date
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)

import Model.Usuario as User
import Model.PeriodoAtividade as PA
# ---------------------------------

# POST METHOD ZONE

# periodo_data = (DIC) informações referente ao periodo que ira ser cadastrado
# owner_id = (NUM) id do proprietario do periodo
def createPeriodoAtividade(periodo_data, owner_id):
    try:
        owner_user = User.Usuario.get_by_id(owner_id)

        date_begin = date(int(periodo_data['begin'][0:4]), int(
            periodo_data['begin'][4:6]), int(periodo_data['begin'][6:8]))

        date_end = date(int(periodo_data['end'][0:4]), int(
            periodo_data['end'][4:6]), int(periodo_data['end'][6:8]))

        # o link de foreign key é feito atraves do
        new_periodo_atividade = PA.PeriodoAtividade(
            inicioDate=date_begin,
            fimDate=date_end,
            id_usuario=owner_user
        )
        new_periodo_atividade.save()
        return True
    except Exception as err:
        print(err)
        return False

def updatePeriodoAtividade(periodo_data, id_pd):
    old_pa = PA.PeriodoAtividade.get_by_id(id_pd)
    begin = date(int(periodo_data['begin'][0:4]), int(
                periodo_data['begin'][4:6]), int(periodo_data['begin'][6:8])) if periodo_data['begin'] != None else None
    end = date(int(periodo_data['end'][0:4]), int(
                periodo_data['end'][4:6]), int(periodo_data['end'][6:8])) if periodo_data['end'] != None else None
    old_pa.inicioDate = begin if begin != None else old_pa.inicioDate
    old_pa.fimDate = end if end != None else old_pa.fimDate
    try:
        old_pa.save()
    except Exception as err:
        print(err)
        return False
    return True
# END ZONE

# GET METHOD ZONE

# periodo_seach = (DIC) possui os parametros para a busca da informacao
def findPeriodoAtividade(periodo_search):
    query_result = None
    if(periodo_search['begin'] != None):
        if(periodo_search['end'] != None and periodo_search['owner_id'] != None):
            date_begin = date(int(periodo_search['begin'][0:4]), int(
                periodo_search['begin'][4:6]), int(periodo_search['begin'][6:8]))
            date_end = date(int(periodo_search['end'][0:4]), int(
                periodo_search['end'][4:6]), int(periodo_search['end'][6:8]))
            query_result = PA.PeriodoAtividade.select().where((PA.PeriodoAtividade.inicioDate == date_begin) &
                                                              (PA.PeriodoAtividade.fimDate == date_end) &
                                                              (PA.PeriodoAtividade.id_usuario == periodo_search['owner_id']))
        else:
            if(periodo_search['end'] != None):
                date_begin = date(int(periodo_search['begin'][0:4]), int(
                    periodo_search['begin'][4:6]), int(periodo_search['begin'][6:8]))
                date_end = date(int(periodo_search['end'][0:4]), int(
                    periodo_search['end'][4:6]), int(periodo_search['end'][6:8]))
                query_result = PA.PeriodoAtividade.select().where((PA.PeriodoAtividade.inicioDate == date_begin) &
                                                                  (PA.PeriodoAtividade.fimDate == date_end))
            elif(periodo_search['owner_id'] != None):
                date_begin = date(int(periodo_search['begin'][0:4]), int(
                    periodo_search['begin'][4:6]), int(periodo_search['begin'][6:8]))
                query_result = PA.PeriodoAtividade.select().where((PA.PeriodoAtividade.inicioDate == date_begin) &
                                                                  (PA.PeriodoAtividade.id_usuario == periodo_search['owner_id']))
            else:
                date_begin = date(int(periodo_search['begin'][0:4]), int(
                    periodo_search['begin'][4:6]), int(periodo_search['begin'][6:8]))
                query_result = PA.PeriodoAtividade.select().where(
                    (PA.PeriodoAtividade.inicioDate == date_begin))
    
    elif(periodo_search['end'] != None):
        if(periodo_search['owner_id']):
            date_end = date(int(periodo_search['end'][0:4]), int(
                periodo_search['end'][4:6]), int(periodo_search['end'][6:8]))
            query_result = PA.PeriodoAtividade.select().where((PA.PeriodoAtividade.fimDate == date_end) &
                                                              (PA.PeriodoAtividade.id_usuario == periodo_search['owner_id']))
        else:
            date_end = date(int(periodo_search['end'][0:4]), int(
                periodo_search['end'][4:6]), int(periodo_search['end'][6:8]))
            query_result = PA.PeriodoAtividade.select().where(
                (PA.PeriodoAtividade.fimDate == date_end))
    else:
        query_result = PA.PeriodoAtividade.select().where(
            (PA.PeriodoAtividade.id_usuario == periodo_search['owner_id']))
    final_result = []
    for find_pa in query_result:
        final_result.append(_makeResultDic(find_pa))

    # dataInicial = final_result[0]['begin'][0:4] + final_result[0]['begin'][5:7]  + final_result[0]['begin'][8:]
    # dataFinal = final_result[0]['end'][0:4] + final_result[0]['end'][5:7]  + final_result[0]['end'][8:]

    for i in range (len(final_result)): 
        dataInicial = str(final_result[i]['begin'])
        dataFinal = str(final_result[i]['end'])
        final_result[i]['begin'] = dataInicial
        final_result[i]['end'] = dataFinal
    return final_result

def _makeResultDic(pa_obj):
    pa_dic = {
        'id_periodo_atividade': pa_obj.id_periodo_atividde,
        'begin':pa_obj.inicioDate,
        'end':pa_obj.fimDate,
        'id_owner':pa_obj.id_usuario.usuario_id
    }
    return pa_dic



# END ZONE
