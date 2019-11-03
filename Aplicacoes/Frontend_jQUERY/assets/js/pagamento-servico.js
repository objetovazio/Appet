paypal.Buttons({
    createOrder: function (data, actions) {
        // Set up the transaction
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: '4.00'
                }
            }]
        });
    },
    onApprove: function (data, actions) {
        actions.redirect('https://www.google.com');
        // Capture the funds from the transaction
        return actions.order.capture().then(function (details) {
            // Show a success message to your buyer
            alert('Transaction completed by ' + details.payer.name.given_name);
        });
    },
    onCancel: function (data, actions) {
        actions.redirect('https://www.youtube.com');
    }
}).render('#paypal-area');
$('#boleto-button').click(function (event) {
    //insert validation or mask
    if ($('#cpf-payer').val()) {
        $.post('https://sandbox.boletobancario.com/boletofacil/integration/api/v1/issue-charge',
            {
                token: 'BBCAB4FCBDDB9DE190DE24D621FA18715E29716C68B05AF51F061B611E1ADAAE',
                description: 'Appet Contratacao Servico',
                amount: '20.00', // this will be the value of service 
                payerName: 'Bicicleta Eletrica', // information based on the user logged
                payerCpfCnpj: '94648945123' //this will be the value at cpf-payer
                //notificationUrl: url da rota que ira manipular pagamento do boleto
            }
        ).done(function (data) {
            var response_boleto = data
            console.log(data);
            window.open(response_boleto.data.charges[0].link, '_blank').focus()
        })
    }
    else {
        alert('empty');
    }
})
$(document).ready(function () {
    var pagamento_data = {}
    location.search.substr(1).split("&").forEach(function (item) { pagamento_data[item.split("=")[0]] = item.split("=")[1] });
    setPageValues(pagamento_data);
    $('#cpf-payer').mask('000.000.000-00', { reverse: true });
    $('#cpf-payer').keyup(function (e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value
        }
    });

});

function setPageValues(data) {
    dataContratacao = "" + data.data.slice(6,8) + "/" + data.data.slice(4,6) + "/" + data.data.slice(0,4);
    $('#data-servico').text(dataContratacao);
    usuario = getUserById(data.usuario);
    servico = getServicoById(data.servico);//necessario ver como buscar as demais informacoes
}

function getUserById(idUser) {

    var data_request = {
        userId: idUser,
        nomeUser: "",
        emailUser: "",
        senha: "",
        sobre: ""
    };

    $.get(rota_user, data_request, function () {
    }).done(function (dados) {

        // convert a strgin em objeto e ao mesmo tempo
        // acessa a chave data no indice 0
        var usuario = JSON.parse(dados).data[0];
        $('#nome-usuario').val(usuario['name']);

    }).fail(function (msg) {

        var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText;
        mensagem(texto, "Erro", 5000);
    });

}

function getServicoById(idService) {

    var data_request = {
        title:'',
		about:'',
		price:'',
		ownerId:'',
		typeService: '',
        hourService: '',
        service_id:idService
    };

    $.get(rota_servico, data_request, function () {
    }).done(function (dados) {

        // convert a strgin em objeto e ao mesmo tempo
        // acessa a chave data no indice 0
        var servico = JSON.parse(dados).data[0];
        $("#preco-servico").val(servico["price"]);
    }).fail(function (msg) {

        var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText;
        mensagem(texto, "Erro", 5000);
    });

}

function getSchedule(idSchedule){
    var data_request = {
        periodoId:idSchedule,
		beginTime:'',
		endTime:'',
		weekDay:''
    };
    $.get(rota_horario_Servico,data_request,function(){
    }).done(function(dados){
       horario = dados.begin_hour +" - " +dados.end_hour
       $('#horario-servico').val(horario)
    }).fail(function (msg) {

        var texto = "Falha ao tentar recuperar os dados do servidor! Status: " + msg.status + " | Motivo: " + msg.responseText;
        mensagem(texto, "Erro", 5000);
    });
}