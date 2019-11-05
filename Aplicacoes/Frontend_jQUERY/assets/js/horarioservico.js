function adicionaHorarioDisp(){

    //formato aaaaMMdd

	raw_date_bagin = $("#dataInicial").val().split('-');
	if ((raw_date_bagin[0].length == 4) && (raw_date_bagin[1].length == 2) && (raw_date_bagin[2].length == 2)){
		input_date_begin = raw_date_bagin[0]+raw_date_bagin[1]+raw_date_bagin[2];
	}else{
		input_date_begin = "";
	}

	//formato aaaaMMdd
	raw_date_end = $("#dataFinal").val().split('-');
	if((raw_date_end[0].length == 4) && (raw_date_end[1].length == 2) && (raw_date_end[2].length == 2)){
		input_date_end = raw_date_end[0]+raw_date_end[1]+raw_date_end[2];
	}else{
		input_date_end = "";
    }

    console.log($('#horario-inicial').val())
    
    raw_time_begin = $("#horarioInicial").val();
    raw_time_end = $("#horarioFinal").val();

	var data_request = {
		beginDate:input_date_begin,
        endDate:input_date_end,
        beginTime:input_time_begin,
        endTime:input_time_end,
        weekDay: $("#diaSemana").val(),
		ownerId:"1",
		horarioId:$("#idHorario").val()
    }

};

/*
function validaData(){

}


function validacao(data_request){
    if (validaData){
        if (validaHorario){
            enviaPostHorario(data_request);
        }
        else{
            alert("Insira um horário válido!");
        }
    }
    else{
        alert("Insira uma data válida!");
    }
}

function enviaPostHorario(data_request){


}
*/