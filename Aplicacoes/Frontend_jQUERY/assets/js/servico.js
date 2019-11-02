function adicionaServico (){

	var data_request = {
		title:$("#titulo").val(),
		about:$("#descricao").val(),
		price:$("#valor").val(),
		ownerId:'1',
		typeService: $("#tiposervico").val(),
		hourService: ''
	};

	if (validaServico(data_request) == true) {

		$.post(rota_servico, data_request, function(){
		}).done( function (){

		$("#titulo").val("");
		$("#descricao").val("");
		$("#valor").val("");
		$('#tiposervico').val("");		

		var texto = "Cadastro do serviço realizado!";
		mensagem(texto, "Sucesso", 2000);

		}).fail( function (msg) {

		var texto = "Falha ao realizar cadastro do serviço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
		});
	}
	
console.log(data_request);
}

function validaServico(servico){
	var msg = "";
	try {
		if (servico.title.length == 0){
		msg = "Preencha o campo titulo";
		throw msg;}	
		if (servico.typeService.length == 0){
		msg = "Selecione o tipo de serviço";
		throw msg;}
		if (servico.about.length == 0) {
		msg = "Preencha o campo descricao";
		throw  msg;}
		if (servico.price.length == 0) {
		msg = "Preencha o campo valor"
		throw msg;}
		if ($.isNumeric(servico.price) == false) {
		msg = "Campo valor só aceita números"
		throw msg;}
		return true;
	}catch(err) {
	mensagem(msg, "Atencao", 2000);
	    return false;
	 }
}
