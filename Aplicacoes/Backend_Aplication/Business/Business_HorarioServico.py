# used to resolve the path problem
from datetime import time
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
import Model.PeriodoAtividade as PA
import Model.HorarioServico as HS
# ---------------------------------


def createSchedule(schedule_data):
	try:
		periodo_assign = PA.PeriodoAtividade.get_by_id(
			int(schedule_data['period_id']))
		begin_time = time(int(schedule_data['begin_hour'][0:2]),
						  int(schedule_data['begin_hour'][2:4]), int(schedule_data['begin_hour'][4:6]))
		end_time = time(int(schedule_data['end_hour'][0:2]),
						int(schedule_data['end_hour'][2:4]), int(schedule_data['end_hour'][4:6]))
		new_schedule = HS.HorarioServico(
			id_periodo=periodo_assign, dia_semana=schedule_data['week_day'], horario_inicio=begin_time, horario_fim=end_time)
		new_schedule.save()
		return True
	except Exception as err:
		print(err)
		return False


def updateSchedule(schedule_data: dict):
	old_schedule = HS.HorarioServico.get_by_id(schedule_data['schedule_id'])

	have_new_begin = schedule_data['begin_hour'] != None
	begin_time = schedule_data['begin_hour'] if have_new_begin else old_schedule.horario_inicio

	have_new_end = schedule_data['end_hour'] != None
	end_time = schedule_data['end_hour'] if have_new_end else old_schedule.horario_fim

	period_schedule = None
	have_new_period = schedule_data['period_id']
	if(have_new_period):
		new_period = PA.PeriodoAtividade.get_by_id(schedule_data['period_id'])
		period_schedule = new_period
	else:
		period_schedule = old_schedule.id_periodo

	have_new_day = schedule_data['week_day'] != None
	week_day = schedule_data['week_day'] if have_new_day else old_schedule.dia_semana

	old_schedule.horario_inicio = begin_time
	old_schedule.horario_fim = end_time
	old_schedule.id_periodo = period_schedule
	old_schedule.dia_semana = week_day
	try:
		old_schedule.save()
	except Exception as err:
		print(err)
		return False
	return True


def findSchedule(query_param: dict):
	final_result = []
	query_result = None
	if(query_param['id']!= None):
		query_result = HS.HorarioServico.get_by_id(query_param['id'])
		final_result.append(_makeResultDic(query_result))
		return final_result
	have_begin = query_param['begin_hour'] != None
	have_end = query_param['end_hour'] != None
	have_day = query_param['week_day'] != None
	if(have_begin):
		if(have_end and have_day):
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_inicio == query_param['begin_hour']) &
				(HS.HorarioServico.horario_fim == query_param['end_hour']) &
				(HS.HorarioServico.dia_semana == query_param['week_day'])
			)
		elif(have_end):
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_inicio == query_param['begin_hour']) &
				(HS.HorarioServico.horario_fim == query_param['end_hour'])
			)
		elif(have_day):
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_inicio == query_param['begin_hour']) &
				(HS.HorarioServico.dia_semana == query_param['week_day'])
			)
		else:
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_inicio == query_param['begin_hour'])
			)
	elif(have_end):
		if(have_day):
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_fim == query_param['end_hour']) &
				(HS.HorarioServico.dia_semana == query_param['week_day'])
			)
		else:
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_fim == query_param['end_hour'])
			)
	else:
		query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.dia_semana == query_param['week_day'])
			)
	for schedule_find in query_result:
		final_result.append(_makeResultDic(schedule_find))
	return final_result

def weekdayMetrics():
	query_build = (
		HS.HorarioServico.select(Hs.HorarioServico.dia_semana, fn.COUNT(Serv.Servico.id_tipo).alias('total'))
	)

def _makeResultDic(schedule_data):
	print(schedule_data)
	result = {
		'schedule_id': schedule_data.id_horario_servico,
		'period_id': schedule_data.id_periodo.id_periodo_atividde,
		'week_day': schedule_data.dia_semana,
		'begin_time': schedule_data.horario_inicio.strftime('%H%M%S'),
		'end_time': schedule_data.horario_fim.strftime('%H%M%S')
	}
	return result
