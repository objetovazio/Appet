$(document).ready(()=>{
    addButtonsEvent()
})

function addButtonsEvent(){
    $('#btn-add').click(()=>{
        addInfoTable();
    });
    $('#service-input').keypress((evt)=>{
        if(evt.which == 13){
            addInfoTable();
        }
    })
    $('#btn-send').click(()=>{
        sendRequest();
    });
}

function addInfoTable(){
    $.get(rota_servico,{service_id:$('#service-input').val()},()=>{

    }).done((response)=>{
        new_row = '<tr id="linha_'+response.id_service+'>'+
        '<td>'+response.id_service +'</td>'+
        '<td>'+response.title +'</td>'+
        '<td>'+response.id_user +'</td>'+
        '<td> <i data-line='+response.id_service+' class="fa fa-trash" aria-hidden="true"></i> </td>'+
        '</tr>';
        $('#services tbody').append(new_row);
    })
}