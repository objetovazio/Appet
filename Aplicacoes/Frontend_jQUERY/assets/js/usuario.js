


function adicionaUsuario (){

	var data_request = {
		userId:"",
		nomeUser:$("#nome").val(),
		emailUser:$("#email").val(),
		senha:$("#senha").val(),
		sobre: ""
	};

	if (validaUsuario( data_request ) == true){

		$.post(rota_user, data_request, function(){
		}).done( function (){

			var texto = "Cadastro realizado!";
			mensagem(texto, "Sucesso", 2000);

			$("#nome").val("");
			$("#email").val("");
			$("#senha").val("");


		}).fail( function (msg) {

			var texto = "Falha ao realizar cadastro! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	}
}


function pegaUsuario (){

	var data_request = {
		userId: "",
		nomeUser:"",
		emailUser: "carla@gmail.com",
		senha:"",
		sobre:""
	};
	
	$.get(rota_user, data_request, function(){
	}).done( function (dados){

		// convert a strgin em objeto e ao mesmo tempo
		// acessa a chave data no indice 0
		var usuario = JSON.parse(dados).data[0];

		$("#id").val(usuario["user_id"]);
		$("#nome").val(usuario["name"]);
		$("#email").val(usuario["email"]);
		$("#senha").val(usuario["password"]);
		$("#sobre").val(usuario["about"]);
	
	}).fail( function (msg) {

		var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
		mensagem(texto, "Erro",5000);
	});

}


function atualizaUsuario(){

	var data_request = {
		userId:$("#id").val(),
		nomeUser:$("#nome").val(),
		emailUser:$("#email").val(),
		senha:$("#senha").val(),
		sobre:$("#sobre").val()
	};

	console.log(data_request);

	if (validaUsuario( data_request ) == true){

		$.post(rota_user, data_request, function(){
		}).done( function (){

			var texto = "Atualização realizada!";
			mensagem(texto, "Sucesso", 2000);

		}).fail( function (msg) {

			var texto = "Falha ao realizar a atualização! Status: " + msg.status + " | Motivo: " + msg.responseText ;
			mensagem(texto, "Erro",5000);
		});
	}
}

                                                               
function validaUsuario( usuario ){
	var msg = "";
	try { 
		if (usuario.nomeUser.length == 0){
			 msg = "Preencha o campo nome";
		 	 throw msg;}
		if (usuario.emailUser.length == 0) {
			msg = "Preencha o campo e-mail";
			throw  msg;}
		// verifica '@' e '.' 
		var indice = Number(usuario.emailUser.indexOf("@"));
		if ( !(indice > 0) || !(usuario.emailUser.includes(".", indice)) ) {
			msg = "Utilize um e-mail válido";
			throw msg;}
		if (usuario.senha.length == 0) {
			msg = "Preencha o campo senha"
			throw msg;}
		return true;
	}catch(err) {
		mensagem(msg, "Atencao",2000);
    	return false;
  	}

}

// function getUsuario (){

// 	var data_request = {
// 		userId:$("#id").val(),
// 		nomeUser:$("#nome").val(),
// 		emailUser:$("#email").val(),
// 		senha:$("#senha").val(),
// 		sobre:$("#sobre").val()
// 	};

// 	$.get(url_request, data_request,function(result){
		
// 		alert(result);

// 	}
// }




// 	var data_request = {
// 		userId:vid, nomeUser:vnome, emailUser:vemail, senha:vsenha, sobre:vsobre
// 	};

// 	$.get(url_request,data_request,function(result){
// 			alert(result);
// 	})

// 	// $.getJSON(url_request, data_request, function(result){
// 	// 	console.log(result);
// 	//  });

// })