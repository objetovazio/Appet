function adicionaServico (){

	var data_request = {
		title:$("#titulo").val(),
		about:$("#descricao").val(),
		prince:$("#valor").val(),
		owner:1, 
		type: tipoServico($("#tiposervico").val()),
		hour: //lista de sericoHorario 
	};

	if (validaServico(data_request) == true) {
		$.post(rota_servico, data_request, function(){
		}).done( function (){

			var texto = "Cadastro do serviço realizado!";
			mensagem(texto, "Sucesso", 2000);

			$("#titulo").val("");
			$("#descricao").val("");
			$("#valor").val("");


		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro do serviço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	}
	console.log(data_request.value());		
}

function validaServico(servico){
	var msg = "";
	try { 
		if (servico.titulo.length == 0){
			 msg = "Preencha o campo titulo";
		 	 throw msg;}
		if (servico.about.length == 0) {
			msg = "Preencha o campo de descricao";
			throw  msg;}
		if (servico.prince.length == 0) {
			msg = "Preencha o campo de valor"
			throw msg;}
		if ($.isNumeric(servico.prince) == false) {
			msg = "Campo valor só aceita números"
			throw msg;}	
		return true;
	}catch(err) {
		mensagem(msg, "Atencao",2000);
    	return false;
  	}	
}

function tipoServico(strservico){
	var idServico;
	if (strservico == "Passeio") {
		idServico = "1";
	}
	if (strservico == "Adestramento") {
		idServico = "2";
	}
	if (strservico == "Petshop") {
		idServico = "3";
	}
	return idServico;
}