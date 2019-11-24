

    
async function ler() {

	return new Promise( (resolve, reject) => {
		$.getJSON( rota_arquivo_json + "/ajuda.json", function(){})
			.done( function(data){  resolve(data.ajuda);
								    $("#carregando").html("");})
			.fail( function(msg){reject("Erro ao tentar ler arquivo Json " + msg);
										$("#carregando").html("");});
	});
}

function carregarArquivo() {
    return new Promise(  (resolve, reject) => {
	    try {
	    	$("#carregando").html("<div id='spinnerloading' class='d-flex justify-content-center'><div class='spinner-grow' role='status'><span style='margin: auto;' class='sr-only'>Loading...</span></div></div>");

	    	var x = ler().then(); 
	    	resolve(x);

	    } catch(e) {
	    	reject(e);
	    }     
    });
}
