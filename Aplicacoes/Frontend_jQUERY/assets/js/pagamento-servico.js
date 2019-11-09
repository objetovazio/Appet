const pagamento_data = {}
location.search.substr(1).split("&").forEach(function (item) { pagamento_data[item.split("=")[0]] = item.split("=")[1] });

$(document).ready(function () {
    setPageValues(pagamento_data);
    $('#cpf-payer').mask('000.000.000-00', { reverse: true });
    $('#cpf-payer').keyup(function (e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value
        }
    });
    startPagamentos();

});

//START PAGE ZONE
function setPageValues(data) {
    dataContratacao = "" + data.data.slice(6, 8) + "/" + data.data.slice(4, 6) + "/" + data.data.slice(0, 4);
    $('#data-servico').text(dataContratacao);
    $('#media-avaliacao').text(pagamento_data.rateServ);
    $('#media-avaliacao').val(pagamento_data.rateServ);
    var addressServ = String(pagamento_data.addressServ).replace(/_/g,' ').replace(/-/g,',');
    $('#endereco').val(addressServ);
    $('#endereco').text(addressServ);
    getUserPromise(data.usuario).then((buyerResponse) => {
        $('#nome-usuario').val(buyerResponse.name);
    });
    getServicePromise(data.servico).then((response) => {
        if(String(response.price).split('.')[1].length > 1){
            $('#preco-servico').text(response.price);
            $('#preco-servico').val(response.price);
        }
        else{
            $('#preco-servico').text(String(response.price)+'0');
            $('#preco-servico').val(String(response.price)+'0');
        }
        
        getUserPromise(response.id_user).then((ownerResponse) => {
            $('#nome-prestador').text(ownerResponse.name);
        })
    });
    getHorarioPromise(data.horario).then((horarioResponse) => {
        begin = horarioResponse.begin_time.slice(0, 2) + ':' + horarioResponse.begin_time.slice(2, 4) + ':' + horarioResponse.begin_time.slice(4, 6);
        end = horarioResponse.end_time.slice(0, 2) + ':' + horarioResponse.end_time.slice(2, 4) + ':' + horarioResponse.end_time.slice(4, 6);
        horario = begin + ' - ' + end;
        $('#horario-servico').text(horario);
        $('#horario-servico').val(horario);
    })
}

function getServicePromise(idServico) {
    return new Promise((resolve, reject) => {
        $.get(rota_servico, { service_id: idServico }, function () {
        }).done(function (dados) {
            resolve(JSON.parse(dados).data[0]);
        })
    });
}
function getUserPromise(idUser) {
    return new Promise((resolve, reject) => {
        $.get(rota_user, { userId: idUser }, () => { }).done((data) => {
            resolve(JSON.parse(data).data[0]);
        });
    });
}
function getHorarioPromise(idHorario) {
    return new Promise((resolve, reject) => {
        $.get(rota_horario_Servico, { id: idHorario }, () => { }).done((data) => {
            resolve(JSON.parse(data).data[0]);
        });
    });
}

//PAGAMENTO ZONE
function startPagamentos() {
    paypal.Buttons({
        createOrder: function (data, actions) {
            // Set up the transaction
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: $('#preco-servico').val()
                    }
                }]
            });
        },
        onApprove: function (data, actions) {
            // Capture the funds from the transaction
            return actions.order.capture().then(function (details) {
                // Show a success message to your buyer
                token_paypal = details.purchase_units[0].payments.captures[0].id
                registre_contrato = send_registre(token_paypal, 2, 3).then((isRegistred) => {
                    if (isRegistred) {
                        alert('Transaction completed by ' + details.payer.name.given_name);
                    }
                    else {
                        window.location.replace('./pagamento-reprovado.html');
                    }
                })

            });
        },
        onCancel: function (data, actions) {
            window.location.replace('./pagamento-reprovado.html');
        },
        onError: function(err){
            window.location.replace('./pagamento-reprovado.html');
        }
    }).render('#paypal-area');
    $('#boleto-button').click(function (event) {
        //insert validation or mask
        if ($('#cpf-payer').val()) {
            $.post('https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge',
                {
                    token: 'BBCAB4FCBDDB9DE190DE24D621FA18715E29716C68B05AF51F061B611E1ADAAE',
                    description: 'Appet Contratacao Servico',
                    amount: $('#preco-servico').val(), // this will be the value of service 
                    payerName: $('#nome-usuario').val(), // information based on the user logged
                    payerCpfCnpj: $('#cpf-payer').val() //this will be the value at cpf-payer
                    //notificationUrl: url da rota que ira manipular pagamento do boleto
                }
            ).done(function (data) {
                var response_boleto = data.data.charges[0];
                token_boleto = response_boleto.code
                registre_contrato = send_registre(token_boleto, 1, 1).then((isRegistred) => {
                    if (isRegistred) {
                        window.open(response_boleto.link, '_blank');
                        window.location.replace('./pagamento-aprovado.html');
                    }
                    else {
                        window.location.replace('./pagamento-reprovado.html');
                    }
                })

            })
        }
        else {
            alert('empty');
        }
    })
}

function send_registre(tokenPayment, method, sstatus) {
    var today = new Date()
    return new Promise((resolve, reject) => {
        $.post(rota_contratacao,
            {
                'token': tokenPayment,
                'comprador': pagamento_data.usuario,
                'servico': pagamento_data.servico,
                'metodo': method,
                'status': sstatus,
                'data_req': formated = String(today.getFullYear()) + String(today.getMonth()) + String(today.getDay()),
                'data_serv': pagamento_data.data,
                'preco': $('#preco-servico').val(),
                'horario': pagamento_data.horario

            }).done(function (data) {
                //resolver isso depois
                resolve(data === "{\"success\": true}");
            });
    });
}