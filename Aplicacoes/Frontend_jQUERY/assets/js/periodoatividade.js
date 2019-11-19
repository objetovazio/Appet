

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

	var anoI = Number(raw_date_bagin[0])
	var mesI = Number(raw_date_bagin[1])
	var diaI = Number(raw_date_bagin[2])

	var anoF = Number(raw_date_end[0])	
	var mesF = Number(raw_date_end[1])
	var diaF = Number(raw_date_end[2])


	if (  (anoI<anoF) ||  (  (anoI==anoF) && (  (mesI<mesF)  || ( ( mesI == mesF ) && ( diaI < diaF ) ) ) )  ){

		owner = $("#id").val();
		var data_request = {
			beginDate:input_date_begin,
			endDate:input_date_end,
			ownerId:owner,
			periodoAtvidadeId:$("#idPeriodo").val()
		};


		if (validaPeriodoAtividade(data_request) == true) {
			
			$.post(rota_periodo_atividade, data_request, function(){
			}).done( function (){

				var texto = "Cadastro do periodo de atividade realizado!";
				mensagem(texto, "Sucesso", 2000);

				$("#idPeriodo").val("");

				 pegaPeriodoAtividade(data_request);

			}).fail( function (msg) {

				var texto = "Falha ao realizar cadastro do periodo de atividade! Status: " + msg.status + " | Motivo: " + msg.responseText ;
				mensagem(texto, "Erro",5000);
			});
		}



	}else{

		var texto = "O intervalo de datas não é válido!" ;
		mensagem(texto, "Atencao",5000);

	}

}


function pegaPeriodoAtividade(periodoAtvidade){
	
	$.get(rota_periodo_atividade, periodoAtvidade, function(){
	}).done( function (dados){

		var periodo = JSON.parse(dados).data[0];

		adicionaLinha(periodo);


	}).fail( function (msg) {

		var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
	});
	
}


function pegaListaPeriodoAtividade(){
	var onwer = $("#id").val()
	var data_request = {
		beginDate:"",
		endDate:"",
		ownerId:onwer,
		periodoAtvidadeId:""
	};
	
	console.log(data_request);
	
	$.get(rota_periodo_atividade, data_request, function(){
	}).done( function (dados){

		var periodo = JSON.parse(dados).data;

		if (periodo.length == 0){

			var texto = "Ainda não há Periodos de Atividade cadastrados! ";
			mensagem(texto, "Atencao",5000);

		}

		$(periodo).each(function(index, elemento) {
			adicionaLinha(elemento);
		});
		


	}).fail( function (msg) {

		var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
	});
	
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

	var linha = "<tr data-id='"+ periodoAtvidade.id_periodo_atividade +"'>" +
		        	"<td data-dInicio = '"+ periodoAtvidade.begin +"'>"+ 
		        		periodoAtvidade.begin +
		        	"</td>" +
		        	"<td data-dFinal = '"+ periodoAtvidade.end +"'>"+ 
		        		periodoAtvidade.end +
		        	"</td>" +
		        	"<td>" + 
		        		"<a onclick='atualizaLinha(this);'  style='cursor:pointer;' title='Editar'><i class='fa fa-pencil'></i></a>" + 
		        		"<a onclick='removeLinha(this);'  style='margin-left: 10px; padding-left:10px;cursor:pointer;' title='Excluir'><i class='fa fa-times'></i></a>" + 
		        	"</td>" +
		      	"</tr>";


	// remove a linha
	// $("#tabelaPeriodo  tr[data-id='" + periodoAtvidade.id_periodo_atividade + "']").remove();
	if ($("#tabelaPeriodo  tr[data-id='" + periodoAtvidade.id_periodo_atividade + "']").length){

		 $("#tabelaPeriodo  tr[data-id='" + periodoAtvidade.id_periodo_atividade + "']").remove();

	}
	// preoend adiciona a primeira linha
	// append adiciona no final
	$("#tabelaPeriodo").prepend(

				"<tr data-id='"+ periodoAtvidade.id_periodo_atividade +"'>" +
		        	"<td data-dInicio = '"+ periodoAtvidade.begin +"'>"+ 
		        		periodoAtvidade.begin +
		        	"</td>" +
		        	"<td data-dFinal = '"+ periodoAtvidade.end +"'>"+ 
		        		periodoAtvidade.end +
		        	"</td>" +
		        	"<td>" + 
		        		"<a onclick='atualizaLinha(this);'  style='cursor:pointer;' title='Editar'><i class='fa fa-pencil'></i></a>" + 
		        		"<a onclick='removeLinha(this);'  style='margin-left: 10px; padding-left:10px;cursor:pointer;' title='Excluir'><i class='fa fa-times'></i></a>" + 
		        	"</td>" +
		      	"</tr>"

			);
	


		
 
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
 // $(elementoExcluir).parents("tr").remove();
}







function listaPeriodo( ){

	  var data_request = {
        beginDate:"",
        endDate:"",
        ownerId: $("#id").val(),
        periodoAtvidadeId:""
      };


	
	$("#periodoatividade").append("<option value='' id='msgEsperaPeriodoAtividade'> Aguarde carregando... </option>");

	$.get(rota_periodo_atividade, data_request, function(){
	}).done( function (dados){
		
		
		$("#msgEsperaPeriodoAtividade").remove();

		var periodo = JSON.parse(dados).data;
		console.log(periodo);

		var ids = '';
		var texto;

		// key é chave do JSON, item é o dado do JSON
		// #tipeservico é o elemento select do html
		$(periodo).each(function(key, item) {
			texto = item.begin +" :: "+ item.end;
			ids = ids + item.id_periodo_atividade + " ";
			$("#periodoatividade").append($("<option>").attr('value',item.id_periodo_atividade).text(texto));
		});

		if( $("#periodoatividade").children('option').length == 1){

			$("#periodoatividade").append("<option value=''>Não há periodos de atividades</option>");
			// console.log($("#periodoatividade option").first().text("Não há periodos de atividades") );
		} 



		$("#periodoatividade").attr('data-ids',ids);
		   $("#periodoatividade").attr('data-ids');

		


		


	}).fail( function (msg) {

		$("#msgEsperaPeriodoAtividade").remove();

		var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
	});
	
}













