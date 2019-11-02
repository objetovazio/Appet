
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------
import Model.TipoServico as TS

def createTypeService(ts_name:str):
    new_typeService = TS.TipoServico(nome_tipo = ts_name)
    try:
        new_typeService.save()
        return True
    except Exception as err:
        print(err)
        return False

def updateTypeService(ts_data:dict):
    old_ts = TS.TipoServico.get_by_id(ts_data['id_ts'])
    old_ts.nome_tipo = ts_data['nome_ts']
    try:
        old_ts.save()
        return True
    except Exception as err:
        print(err)
        return False

def findTypeService(data_query:dict):
    result_query = None
    have_id = data_query['id_ts'] != '' and data_query['id_ts'] != None
    if(have_id):
        result_query = TS.TipoServico.get_by_id(data_query['id_ts'])
    else:
        if(data_query['nome_ts']):
            result_query = TS.TipoServico.select().where(TS.TipoServico.contains(data_query['nome_ts']))
        else:
            result_query = TS.TipoServico.select()
    final_result = []
    for result in result_query:
        final_result.append(_makeDic(result))
    return final_result

def _makeDic(ts_data):
    ts_dic = {
        'id':ts_data.id_tipo,
        'nome': ts_data.nome_tipo
    }
    return ts_dic