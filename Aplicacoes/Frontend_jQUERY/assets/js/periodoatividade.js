

function adicionarPeriodoAtividade(){
	
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
	
	
	var data_request = {
		beginDate:input_date_begin,
		endDate:input_date_end,
		ownerId:"1",
		periodoAtvidadeId:$("#idPeriodo").val()
	};


	if (validaPeriodoAtividade(data_request) == true) {

		$.post(rota_periodo_atividade, data_request, function(){
		}).done( function (){

		var texto = "Cadastro do periodo de atividade realizado!";
		mensagem(texto, "Sucesso", 2000);
		$("#dataInicial").val("");
		$("#dataFinal").val("");

		}).fail( function (msg) {

		var texto = "Falha ao realizar cadastro do periodo de atividade! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
		});
	}
	
	console.log(data_request);

}


function validaPeriodoAtividade(periodoAtvidade) {
	var msg = "";
	try {
		if ($.isNumeric(periodoAtvidade.beginDate) == false){
			msg = "Informe a data no campo data inicial";
			throw msg;}	
		if ($.isNumeric(periodoAtvidade.endDate) == false){
			msg = "Informe a data no campo data final";
			throw msg;}
		return true;
	}catch(err) {
	mensagem(msg, "Atencao", 2000);
	    return false;
	 }
}




