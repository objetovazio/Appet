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


			var endereco = JSON.parse(dados).data;
			console.log(endereco);
			if(endereco.length){
				$("#idEndreco").val(endereco[0].id_address);
				$("#cep").val(endereco[0].cep);
				$("#bairro").val(endereco[0].bairro);
				$("#cidade").val(endereco[0].city);
				$("#estado").val(endereco[0].state);
				$("#numero").val(endereco[0].num);
			}	

		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro do endereço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	
}



function atualizaEndereco(){




	var data_request = {
		userId:$("#id").val(),
		cep:$("#cep").val(),
		bairro:$("#bairro").val(),
		cidade:$("#cidade").val(),
		estado:$("#estado").val(),
		numero:$("#numero").val(),
		address_id:$("#idEndreco").val()
	};


	console.log("enviou");
	console.log(data_request);

	$.post(rota_endereco, data_request, function(){
	}).done( function (){

		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro do endereço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	
}