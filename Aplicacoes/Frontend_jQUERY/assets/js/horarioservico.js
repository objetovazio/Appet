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
		horarioId:$("#idHorario").val()
    }

     console.log(data_request);
    if (validarHorarioServico(data_request)){


            $.post(rota_horario_Servico, data_request, function(){
            }).done( function (){

                $("#horarioInicial").val("");
                $("#horarioFinal").val("");


                pegaHorarioServico();

                var texto = "Cadastro de Horário de Serviço realizado!";
                mensagem(texto, "Sucesso", 2000);

            }).fail( function (msg) {

                var texto = "Falha ao realizar cadastro do Horário de Serviço! Status: " + msg.status + " | Motivo: " + msg.responseText ;
                mensagem(texto, "Erro",5000);
            });
    }
   

};




function pegaHorarioServico(){


        $("#periodoatividade option").each(function() {
             alert( $(this).val() );
        }); 

        var data_request = {
        periodoId: "",
        beginTime:"",
        endTime:"",
        weekDay: "",
        horarioId:"",
        id:""
    }


    
    $.get(rota_horario_Servico, data_request, function(){
    }).done( function (dados){

        var horario_servico = JSON.parse(dados);

        console.log(horario_servico);
        adicionaLinhaH(horario_servico);


    }).fail( function (msg) {

        var texto = "Falha ao tentar recuperar dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText ;
        mensagem(texto, "Erro",5000);
    });
    
}


function validarHorarioServico(horario_servico) {
    var msg = "";
    try {

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

    var linha = "<tr data-id='"+ horario_servico.id +"'>" +
                    "<td data-pAtividade = '"+ horario_servico.period +"'>"+ 
                        horario_servico.period +
                    "</td>" +
                    "<td data-week = '"+ horario_servico.week_day +"'>"+ 
                        horario_servico.week_day +
                    "</td>" + 
                    "<td data-tInicio = '"+ horario_servico.begin_hour +"'>"+ 
                        horario_servico.begin_hour +
                    "</td>" +
                    "<td data-tFinal = '"+ horario_servico.end_time +"'>"+ 
                        horario_servico.end_time +
                    "</td>" +
                    "<td>" + 
                        "<a onclick='atualizaLinha(this);'  style='cursor:pointer;' title='Editar'><i class='fa fa-pencil'></i></a>" + 
                        "<a onclick='removeLinha(this);'  style='margin-left: 10px; padding-left:10px;cursor:pointer;' title='Excluir'><i class='fa fa-times'></i></a>" + 
                    "</td>" +
                "</tr>";


    // remove a linha
    // $("#tabelaPeriodo  tr[data-id='" + periodoAtvidade.id_periodo_atividade + "']").remove();
    if ($("#tabelaPeriodo  tr[data-id='" + horario_servico.id + "']").length){

         $("#tabelaPeriodo  tr[data-id='" + horario_servico.id + "']").remove();

    }
    // preoend adiciona a primeira linha
    // append adiciona no final
    $("#tabelaPeriodo").prepend(linha );
    


        
 
}

function removeLinhaH(elementoExcluir){
    var id = $(elementoExcluir).parents("tr").data("id");
    $(elementoExcluir).parents("tr").remove();
    alert("será apagado id = " + id);
}


function atualizaLinhaH(elementoAtualiza){

    // var id = $(elementoAtualiza).parents("tr").data("id");
    // var dInicial = $(elementoAtualiza).parents("tr").children()[0].attributes[0].value;
    // var dFinal = $(elementoAtualiza).parents("tr").children()[1].attributes[0].value;

    // $("#idPeriodo").val(id);
    // $("#dataInicial").val(dInicial);
    // $("#dataFinal").val(dFinal);

}
