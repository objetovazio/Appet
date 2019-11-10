
function pegaServico (){

	var data_request = {
		id_ts: "",
		nome_ts:""
	};
	
	$.get(rota_tipo_servico, data_request, function(){
	}).done( function (dados){

		// convert a string em objeto e ao mesmo tempo
		// acessa a chave data no indice 0
		var servico = JSON.parse(dados).data;
		
		// key é chave do JSON, item é o dado do JSON
		// #tipeservico é o elemento select do html
		$(servico).each(function(key, item) {
			$("#tiposervico").append($("<option>").attr('value',item.id).text( item.nome));
		});
	
	}).fail( function (msg) {

		var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
	});

}
