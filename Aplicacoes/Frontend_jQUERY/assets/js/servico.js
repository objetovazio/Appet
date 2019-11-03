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


function pegaListaServico (){

	var data_request = {
		title:"",
		about:"",
		price:"",
		ownerId:'1',
		typeService: "",
		hourService: ""
	};

	$.get(rota_servico, data_request, function () {
	}).done(function (dados) {

			// convert a strgin em objeto e ao mesmo tempo
			// acessa a chave data
			var servico = JSON.parse(dados).data;
			console.log(servico);
			var texto = ""
			$(servico).each(function(index, elemento) {
				console.log(elemento.about);
				texto += "<p onclick='mostrar(this)'> 	&bull; <em style='cursor:pointer; font-style: oblique; text-shadow'>"+elemento.title+"</em> <em style='font-size:14px; margin-left:4px;  cursor:pointer'>  &#8212; R$ "+
				 elemento.price +" </em> <i style='float:right; cursor:pointer; color: gray  ' class='fa fa-chevron-down'></i> <br>"+
				"<span class='display-none' style='font-size:15px;'>&nbsp;&nbsp;&nbsp;tipo: "+elemento.id_type + "<br>&nbsp;&nbsp;&nbsp;sobre: " +elemento.about+ "<br>"+"</span></p>";
			});

			$("#cardServicoConteudo").html( texto);
			
			


		}).fail(function (msg) {

			var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText;
			mensagem(texto, "Erro", 5000);
		});
	
	
}


function mostrar(elemento){

	// var elemento = $(elemento).children();
	// var atributo = elemento.css("display");
	if ($(elemento).children('span').hasClass('display-none')){

		
		$(elemento).children('span').removeClass('display-none');
		$(elemento).children('i').removeClass('fa-chevron-down');
		$(elemento).children('i').addClass('fa-chevron-up');

	}else {

		$(elemento).children('span').addClass('display-none');
		$(elemento).children('i').addClass('fa-chevron-down');
		$(elemento).children('i').removeClass('fa-chevron-up');
	}

}



