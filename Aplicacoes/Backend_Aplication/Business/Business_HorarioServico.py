# used to resolve the path problem
from datetime import time
import Model.PeriodoAtividade as PA
import Model.HorarioServico as HS
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
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
	query_result = None
	is_period_empty = query_param['period_id'] == None
	is_begin_empty = query_param['begin_hour'] == None
	is_end_empty = query_param['end_hour'] == None
	is_day_empty = query_param['week_day'] == None
	if (not is_period_empty):
		if(not is_begin_empty and not is_end_empty and not is_day_empty):
			begin_time = time(query_param['begin_hour'][0:2],
							  query_param['begin_hour'][2:4], query_param['begin_hour'][4:6])
			end_time = time(query_param['end_hour'][0:2],
							query_param['end_hour'][2:4], query_param['end_hour'][4:6])
			query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
															(HS.HorarioServico.dia_semana == query_param['week_day']) &
															(HS.HorarioServico.horario_inicio == begin_time) &
															(HS.HorarioServico.horario_fim == end_time))
		elif(not is_begin_empty):
			begin_time = time(query_param['begin_hour'][0:2],
							  query_param['begin_hour'][2:4], query_param['begin_hour'][4:6])
			if(not is_end_empty):
				end_time = time(query_param['end_hour'][0:2],
								query_param['end_hour'][2:4], query_param['end_hour'][4:6])
				query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
																(HS.HorarioServico.horario_inicio == begin_time) &
																(HS.HorarioServico.horario_fim == end_time))
			elif(not is_day_empty):
				query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
																(HS.HorarioServico.dia_semana == query_param['week_day']) &
																(HS.HorarioServico.horario_inicio == begin_time))
			else:
				query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
																(HS.HorarioServico.dia_semana == query_param['week_day']) &
																(HS.HorarioServico.horario_inicio == begin_time) &
																(HS.HorarioServico.horario_fim == end_time))
		elif(not is_end_empty):
			end_time = time(query_param['end_hour'][0:2],
							query_param['end_hour'][2:4], query_param['end_hour'][4:6])
			if(not is_day_empty):
				query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
																(HS.HorarioServico.dia_semana == query_param['week_day']) &
																(HS.HorarioServico.horario_fim == end_time))
			else:
				query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
																(HS.HorarioServico.horario_fim == end_time))
		elif(not is_day_empty):
			query_result = HS.HorarioServico.select().where((HS.HorarioServico.id_periodo == query_param['period_id']) &
															(HS.HorarioServico.dia_semana == query_param['week_day']))
		else:
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.id_periodo == query_param['period_id']))

	elif(not is_begin_empty):
		begin_time = time(query_param['begin_hour'][0:2],
						  query_param['begin_hour'][2:4], query_param['begin_hour'][4:6])
		if(not is_end_empty and not is_day_empty):
			end_time = time(query_param['end_hour'][0:2],
							query_param['end_hour'][2:4], query_param['end_hour'][4:6])
			query_result = HS.HorarioServico.select().where((HS.HorarioServico.dia_semana == query_param['week_day']) &
															(HS.HorarioServico.horario_inicio == begin_time) &
															(HS.HorarioServico.horario_fim == end_time))
		elif(not is_end_empty):
			end_time = time(query_param['end_hour'][0:2],
							query_param['end_hour'][2:4], query_param['end_hour'][4:6])
			query_result = HS.HorarioServico.select().where((HS.HorarioServico.horario_inicio == begin_time) &
															(HS.HorarioServico.horario_fim == end_time))
		elif(not is_day_empty):
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.dia_semana == query_param['week_day']) &
				(HS.HorarioServico.horario_inicio == begin_time))
		else:
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_inicio == begin_time))

	elif(not is_end_empty):
		end_time = time(query_param['end_hour'][0:2],
						query_param['end_hour'][2:4], query_param['end_hour'][4:6])
		if(not is_day_empty):
			query_result = HS.HorarioServico.select().where((HS.HorarioServico.dia_semana == query_param['week_day']) &
															(HS.HorarioServico.horario_fim == end_time))
		else:
			query_result = HS.HorarioServico.select().where(
				(HS.HorarioServico.horario_fim == end_time))

	else:
		query_result = HS.HorarioServico.select().where(
			(HS.HorarioServico.dia_semana == query_param['week_day']))
	final_result = []
	for schedule_find in query_result:
		final_result.append(_makeResultDic(schedule_find))
	return final_result


def _makeResultDic(schedule_data):
	result = {
		'schedule_id': schedule_data.id_horario_servico,
		'period_id': schedule_data.id_periodo.id_periodo_atividde,
		'week_day': schedule_data.dia_semana,
		'begin_time': schedule_data.horario_inicio.strftime('%H%M%S'),
		'end_time': schedule_data.horario_fim.strftime('%H%M%S')
	}
	return result
