

    
async function ler() {

	return new Promise( (resolve, reject) => {
		$.getJSON("../assets/js/data/ajuda.json", function(){})
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


function verifica(a, b){
      // verifica se cada parte da palavra está contida no texto chave
      var texto = removeAcento(b);
      var lista_palavras = texto.split(" ");
      var quant =  lista_palavras.length;
      for (var i = 0; i < quant; i++) {
        if(! String(a).toLowerCase().includes(lista_palavras[i].toLowerCase())){
           return false;
        }
      }
      return true;
}


function removeAcento(text){   
    text = " " + text.toUpperCase() + " ";                                                         
    text = text.replace(new RegExp('[ÁÀÂÃ]','gi'), 'A');
    text = text.replace(new RegExp('[ÉÈÊ]','gi'), 'E');
    text = text.replace(new RegExp('[ÍÌÎ]','gi'), 'I');
    text = text.replace(new RegExp('[ÓÒÔÕÖ]','gi'), 'O');
    text = text.replace(new RegExp('[ÚÙÛÜ]','gi'), 'U');
    text = text.replace(new RegExp('[Ç]','gi'), 'C');
    text = text.replace(new RegExp(' D[AEO] ','gi'), ' ');
    text = text.replace(new RegExp(' N[AO] ','gi'), ' ');
    text = text.replace(new RegExp(' EM ','gi'), ' ');
    text = text.replace(new RegExp(' COM ','gi'), ' ');
    text = text.replace(new RegExp(' COMO ','gi'), ' ');
    text = text.replace(new RegExp(' QUE ','gi'), ' ');
    text = text.replace(new RegExp(' [OA]S ','gi'), ' ');
    text = text.replace(new RegExp(' A ','gi'), ' ');
    text = text.replace(new RegExp(' E ','gi'), ' ');   
    text = text.replace(new RegExp(' O ','gi'), ' ');
    text = text.replace(new RegExp(' AO ','gi'), ' ');
    text = text.replace(new RegExp('^[ ]','m'), '');
    text = text.replace(new RegExp('[ ]$','m'), '');
    return text.toLowerCase();                
}

function adicionaLista (array){

      $("#lista-assunto").children().remove();
      $(array).each(function(index, el) {
        $("#lista-assunto").append("<li onclick='mostrar(this)' style='cursor:pointer;'><b>"+ el.head +"</b> <i style='cursor:pointer; color: #2a2a2a ' class='fa fa-chevron-down'></i><br><span class='display-none' style='max-width:70%;'>"+ el.body +"</span></li><br>");
      });
      
 }

