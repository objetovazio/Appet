function adicionaEndereco (){

	var data_request = {
		userId:$("#id").val(),
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
			if (endereco.cep.length != 8){
			msg = "Campo CEP deve ter 8 digitos";
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


function pegaEndereco(){

	var data_request = {
		userId:$("#id").val(),
		cep:"",
		bairro:"",
		cidade:"",
		estado:"",
		numero:""
	};

	console.log(data_request);

	
	$.get(rota_endereco, data_request, function(){
	}).done( function (dados){


			var endereco = JSON.parse(dados).data[0];

			console.log(endereco);
			
			$("#idEndreco").val(endereco.address_id);
			$("#cep").val(endereco.cep);
			$("#bairro").val(endereco.bairro);
			$("#cidade").val(endereco.city);
			$("#estado").val(endereco.state);
			$("#numero").val(endereco.num);	


		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro do endereço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	
}