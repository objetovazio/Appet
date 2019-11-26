$(document).ready(() => {
    addButtonsEvent()
})

function addButtonsEvent() {
    $('#btn-add').click(() => {
        addInfoTable();
    });
    $('#service-input').keypress((evt) => {
        if (evt.which == 13) {
            addInfoTable();
        }
    })
    $('#btn-send').click(() => {
        sendRequest();
    });

    $('#users').delegate('.remove-item', 'click', (evt) => {
        id_linha = evt.target.dataset.line;
        $('#linha_' + id_linha).remove();
    })

}

function addInfoTable() {
    $.get(rota_user, { userId: $('#user-input').val() }, () => {

    }).done((response) => {
        obj_result = JSON.parse(response).data[0]
        new_row = '<tr id="linha_' + obj_result.user_id + '" data-line=' + obj_result.user_id + '>' +
            '<td>' + obj_result.user_id + '</td>' +
            '<td>' + obj_result.name + '</td>' +
            '<td> <button class="btn remove-item" type="button" data-line=' + obj_result.user_id + '><i  class="fa fa-trash" aria-hidden="true"></i> </button></td>' +
            '</tr>';
        $('#users tbody').append(new_row);
    })
}
function removeItemList() {
    return 0;
}

function sendRequest() {
    requestIds = [];
    linesRequest = $('#users tbody')[0].children;
    if (linesRequest.length > 0) {
        for (i = 0; i < linesRequest.length; i++) {
            if (!requestIds.includes(linesRequest[i].dataset.line)) {
                requestIds.push(linesRequest[i].dataset.line);
            }
        }
        $.post(rota_remove_user, { userId: JSON.stringify(requestIds) }, () => {

        }).done((response) => {
            var response_success = JSON.parse(response)
            if (response_success.success) {
                alert('Usuario(s) Removidos');
                window.location.href = '/admin-home.html';
            }
            else {
                alert('Erro Ao Remover Usuario(s)');
                window.location.reload();
            }
        })
    }
    else {
        alert('Requisição Vazia');
        window.location.reload();
    }
    console.log(requestIds);

}