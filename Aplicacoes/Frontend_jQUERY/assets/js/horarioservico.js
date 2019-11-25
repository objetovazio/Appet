function adicionaHorario(){

    var raw_time_begin = $("#horarioInicial").val();
    var raw_time_end = $("#horarioFinal").val();

    var horaInicio = raw_time_begin.split(":")[0]  + raw_time_begin.split(":")[1] + "00";
    var horaFinal = raw_time_end.split(":")[0]  + raw_time_end.split(":")[1] + "00";
    


    var data_request = {
        periodoId: $("#periodoatividade").children("option:selected").val(),
        beginTime:horaInicio,
        endTime:horaFinal,
        weekDay: $("#diaSemana").val(),
       
    }
    //adicionar no array
    //obj.key3 = "value3";
    //obj["key3"] = "value3";

   if( $("#idHorario").val().length != 0){
        data_request.serviceSchedule = $("#idHorario").val();
   }

    console.log("enviado");
    console.log(data_request);
    if (validarHorarioServico(data_request)){


            $.post(rota_horario_Servico, data_request, function(){
            }).done( function (){

                $("#horarioInicial").val("");
                $("#horarioFinal").val("");
                $("#idHorario").val("");

                pegaHorarioServico( data_request );

                var texto = "";
                if( "serviceSchedule" in data_request){
                    texto = "Atualização de Horário de Serviço realizado!";
                }else{
                    texto = "Cadastro de Horário de Serviço realizado!";
                }
                
                mensagem(texto, "Sucesso", 2000);

            }).fail( function (msg) {
                var texto = "";
                if(data_request.serviceSchedule.length == 0){
                    texto = "Falha ao realizar cadastro do Horário de Serviço!";
                }else{
                    texto = "Falha ao realizar atualização do Horário de Serviço!";
                }
                texto = texto + "Status: " + msg.status + " | Motivo: " + msg.responseText ;
                mensagem(texto, "Erro",5000);
            });
    }
   

};


function pegalistaHorarioServico( ){


        var ids = $("#periodoatividade").attr('data-ids').split(" ");
        //remove  o ultimo elemento e retorna ele
        ids.pop();

        // alert(ids);
        console.log(ids);

        var data_request = {
        id:"",
        periodId: JSON.stringify(ids),
        beginTime:"",
        endTime:"",
        weekDay: ""
       
    }
    console.log("enviou");
     
    console.log(data_request);
    
    $.get(rota_horario_Servico, data_request, function(){
    }).done( function (dados){

        var horario_servico = JSON.parse(dados).data;

        console.log("recebeu");
        console.log(horario_servico);

        $(horario_servico).each(function(index, elemento) {
            adicionaLinhaH(elemento);
        });
      


    }).fail( function (msg) {

        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
        mensagem(texto, "Erro",5000);
    });
    
}



function pegaHorarioServico( data_request ){
    
    $.get(rota_horario_Servico, data_request, function(){
    }).done( function (dados){

        var horario_servico = JSON.parse(dados).data;

        console.log("recebeu");
        console.log(horario_servico);

        $(horario_servico).each(function(index, elemento) {
            adicionaLinhaH(elemento);
        });
      


    }).fail( function (msg) {

        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
        mensagem(texto, "Erro",5000);
    });
    
}


function validarHorarioServico(horario_servico) {
    var msg = "";
    try {


        if (horario_servico.periodoId.includes("-1")){
            msg = "Selecione um período de atividade";
            throw msg;}

         if (horario_servico.periodoId.length==0){
            msg = "Selecione um Periodo de Atividade";
            throw msg;}

        if ($.isNumeric(horario_servico.beginTime) == false){
            msg = "Informe a hora no campo horário inicial";
            throw msg;} 
        if ($.isNumeric(horario_servico.endTime) == false){
            msg = "Informe a hora no campo horário final";
            throw msg;}

        if (Number(horario_servico.beginTime) >= Number(horario_servico.endTime)){
            msg = "Intervalo de Horários Inválido";
            throw msg;}



        return true;
    }catch(err) {
    mensagem(msg, "Atencao", 2000);
        return false;
     }
}






function adicionaLinhaH(horario_servico) {

    // console.log(horario_servico);
    var linha = "<tr data-id='"+ horario_servico.schedule_id +"'>" +
                    "<td data-pAtividade = '"+ horario_servico.period_id +"'>"+ 
                       periodo_formato( horario_servico.period_id ) +
                    "</td>" +
                    "<td data-week = '"+ horario_servico.week_day +"'>"+ 
                        semana(horario_servico.week_day) +
                    "</td>" + 
                    "<td data-tInicio = '"+ horario_servico.begin_time +"' data-tFinal = '"+ horario_servico.end_time +"' >"+ 
                        hora_formato ( horario_servico.begin_time ) + " - "  + hora_formato ( horario_servico.end_time ) +
                    "</td>" +
                    "<td>" + 
                        "<a onclick='atualizaLinhaH(this);'  style='cursor:pointer;' title='Editar'><i class='fa fa-pencil'></i></a>" + 
                        "<a onclick='removeLinhaH(this);'  style='margin-left: 10px; padding-left:10px;cursor:pointer;' title='Excluir'><i class='fa fa-times'></i></a>" + 
                    "</td>" +
                "</tr>";


    // remove a linha
    // $("#tabelaPeriodo  tr[data-id='" + periodoAtvidade.id_periodo_atividade + "']").remove();
    if ($("#tabelaHorario  tr[data-id='" + horario_servico.schedule_id + "']").length){

         $("#tabelaHorario  tr[data-id='" + horario_servico.schedule_id + "']").remove();

    }
    // preoend adiciona a primeira linha
    // append adiciona no final
    // console.log(linha);
    $("#tabelaHorario").prepend( linha );
    


        
 
}

function removeLinhaH(elementoExcluir){
    var id = $(elementoExcluir).parents("tr").data("id");
    $.post(rota_remove_horario_Servico, {horarioId: id}, function(){
    }).done( function (){
            $(elementoExcluir).parents("tr").remove();
            var texto = "Remoção de Horário de Serviço realizado!";
            mensagem(texto, "Sucesso", 2000);
    }).fail( function (msg) {
        var texto = "Falha ao realizar remoção do Horário de Serviço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
        mensagem(texto, "Erro",5000);
    });
}


function atualizaLinhaH(elementoAtualiza){

    var idhorarioservico = $(elementoAtualiza).parents("tr").data("id");

    var idperiodo = $(elementoAtualiza).parents("tr").children()[0].attributes[0].value;
    var diasemana = $(elementoAtualiza).parents("tr").children()[1].attributes[0].value;
    var horainicial = $(elementoAtualiza).parents("tr").children()[2].attributes[0].value;
    var horafinal = $(elementoAtualiza).parents("tr").children()[2].attributes[1].value;

    $("#horarioInicial").val(horainicial.slice(0, 2)+":"+horainicial.slice(2, 4)+":00");
    $("#horarioFinal").val(horafinal.slice(0, 2)+":"+horafinal.slice(2, 4)+":00");
    $("#periodoatividade").val(idperiodo).change();
    $("#diaSemana").val(diasemana).change();
    $("#idHorario").val(idhorarioservico);

}



function semana ( numero ){

    if (numero == "1") return "Domingo";
    if (numero == "2") return "Segunda";
    if (numero == "3") return "Terça";
    if (numero == "4") return "Quarta";
    if (numero == "5") return "Quinta";
    if (numero == "6") return "Sexta";
    if (numero == "7") return "Sábado";

}


function hora_formato( numero ){

    return numero.slice(0, 2) + ":" + numero.slice(2, 4);

}


function periodo_formato( numero ){

    var texto = "";
    $("#periodoatividade option").each(function () {
        if ($(this).val() != "" && $(this).val() == numero){
             texto =  $(this).text();

        }
     });

    return texto;
}