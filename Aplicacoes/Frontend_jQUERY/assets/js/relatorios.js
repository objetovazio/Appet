async function getWeekDayServices(){
    try {
        const res = await $.get(rota_relatorio_weekDayServices);
        const dados = JSON.parse(res);
        return (dados);

    } catch (error) {        
        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + error.status + " | Motivo: " + error.responseText ;
        mensagem(texto, "Erro",5000);
    }

    // $.get(rota_relatorio_weekDayServices, function(){}).done( function(dados) {
        
    //     var rel1 = JSON.parse(dados);
        

    // }).fail(function(msg){
    //     var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
    //     mensagem(texto, "Erro",5000);
    // })

}

async function getTypeServices(){
    try {
        const res = await $.get(rota_relatorio_typeServices);

        const dados = JSON.parse(res);
        return (dados);
    
    } catch (error) {
        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + error.status + " | Motivo: " + error.responseText ;
        mensagem(texto, "Erro",5000);
    }

    // $.get(rota_relatorio_typeServices, function(){}).done( function(dados) {
        
    //     var rel2 = JSON.parse(dados);


    // }).fail(function(msg){
    //     var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
    //     mensagem(texto, "Erro",5000);
    // })
}



async function getDataTypeService(idtype){
    
    var data_request = {
        typeService: idtype
    };

    try {
        const res = await $.get(rota_servico, data_request);
      
        const dados = JSON.parse(res);
        
        return (dados);
    
    } catch (error) {
        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + error.status + " | Motivo: " + error.responseText ;
        mensagem(texto, "Erro",5000);
    }

    // $.get(rota_relatorio_typeServices, function(){}).done( function(dados) {
        
    //     var rel2 = JSON.parse(dados);


    // }).fail(function(msg){
    //     var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
    //     mensagem(texto, "Erro",5000);
    // })
}

