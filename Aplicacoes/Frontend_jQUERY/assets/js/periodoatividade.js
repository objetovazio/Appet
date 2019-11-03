

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
		console.log("entrou 1")
		$.post(rota_periodo_atividade, data_request, function(){
		}).done( function (){

			console.log("entrou 2")

			var texto = "Cadastro do periodo de atividade realizado!";
			mensagem(texto, "Sucesso", 2000);

			$("#idPeriodo").val("");


			 pegaPeriodoAtividade(data_request);


		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro do periodo de atividade! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	}
	
	console.log("saiu")

}


function pegaPeriodoAtividade(periodoAtvidade){
	
	
	if (validaPeriodoAtividade(periodoAtvidade) == true) {


		console.log("dados enviados");
		console.log(periodoAtvidade);

		

		$.get(rota_periodo_atividade, periodoAtvidade, function(){
		}).done( function (dados){


			console.log("dados recebidos");
			console.log(dados);
			
			var periodo = JSON.parse(dados).data[0];

			console.log(periodo);

			adicionaLinha(periodo);


		}).fail( function (msg) {

			var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	}

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


function adicionaLinha(periodoAtvidade) {

	console.log(periodoAtvidade);
	// var datainicio = periodoAtvidade.beginDate.slice(0, 4) +"-"+ 
 //        			 periodoAtvidade.beginDate.slice(4, 6) +"-"+  
 //        			 periodoAtvidade.beginDate.slice(6);
 //    var datafinal = periodoAtvidade.endDate.slice(0, 4) +"-"+  
 //        			periodoAtvidade.endDate.slice(4, 6) +"-"+  
 //        			periodoAtvidade.endDate.slice(6);

	// $("#tabelaPeriodo").append(
	// 	"<tr data-id='"+ periodoAtvidade. +"'>" +
 //        	"<td data-dInicio = '"+ datainicio +"'>"+ 
 //        		datainicio +
 //        	"</td>" +
 //        	"<td data-dFinal = '"+ datafinal +"'>"+ 
 //        		datafinal +
 //        	"</td>" +
 //        	"<td>" + 
 //        		"<a onclick='atualizaLinha(this);'  style='margin-left: 15px;padding-left:10px;cursor:pointer;' title='Editar'><i class='fa fa-pencil'></i></a>" + 
 //        		"<a onclick='removeLinha(this);'  style='margin-left: 20px; padding-left:10px;cursor:pointer;' title='Excluir'><i class='fa fa-times'></i></a>" + 
 //        	"</td>" +
 //      	"</tr>");     
}

function removeLinha(elementoExcluir){
	var id = $(elementoExcluir).parents("tr").data("id");
	$(elementoExcluir).parents("tr").remove();
	alert("será apagado id = " + id);
}


function atualizaLinha(elementoAtualiza){

	var id = $(elementoAtualiza).parents("tr").data("id");
	var dInicial = $(elementoAtualiza).parents("tr").children()[0].attributes[0].value;
	var dFinal = $(elementoAtualiza).parents("tr").children()[1].attributes[0].value;

	$("#idPeriodo").val(id);
	$("#dataInicial").val(dInicial);
	$("#dataFinal").val(dFinal);

	// var a = $(elementoAtualiza).parents("tr").children().each(function(){
 //  		 alert($(this).text());
 // 	});


	$(elementoAtualiza).parents("tr").remove();

}








