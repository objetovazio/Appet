function adicionaEndereco (){

	var owner_list = [1];

	var data_request = {
		userId:"1",
		cep:$("#cep").val(),
		bairro:$("#bairro").val(),
		cidade:$("#cidade").val(),
		estado:$("#estado").val(),
		numero:$("#numero").val()
	};
	console.log(data_request);

	if (validaEndereco(data_request) == true) {

		$.post(rota_endereco, data_request, function(){
		}).done( function (){

		$("#cep").val("");
		$("#bairro").val("");
		$("#cidade").val("");
		$("#estado").val("");
		$("#numero").val("");	

		var texto = "Cadastro Endereço realizado!";
		mensagem(texto, "Sucesso", 2000);

		conlose.log(data_request);
		}).fail( function (msg) {

		var texto = "Falha ao realizar cadastro do endereço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
		});
	}
}

	function validaEndereco(endereco){
		var msg = "";
		try {
			if (endereco.cep.length == 0){
			msg = "Preencha o campo CEP";
			throw msg;}
			if (endereco.cep.length != 9){
			msg = "Campo CEP deve ter 9 digitos";
			throw msg;}
			if (endereco.bairro.length == 0){
			msg = "Preencha o campo bairro";
			throw msg;}
			if (endereco.cidade.length == 0) {
			msg = "Preencha o campo cidade";
			throw  msg;}
			if (endereco.numero.length == 0) {
			msg = "Preencha o campo numero"
			throw msg;}
			if ($.isNumeric(endereco.numero) == false) {
			msg = "Campo numero só aceita números"
			throw msg;}
			return true;
		}catch(err) {
		mensagem(msg, "Atencao", 2000);
		    return false;
		}
	}
