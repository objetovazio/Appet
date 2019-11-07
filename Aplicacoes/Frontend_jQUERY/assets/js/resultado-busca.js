const busca_data = {}
location.search.substr(1).split("&").forEach(function (item) { busca_data[item.split("=")[0]] = item.split("=")[1] });
$(document).ready(function () {
    var finded_service = getSimpleServicePromise().then((serviceData) => {
        console.log(serviceData);
        serviceData.forEach((currentService) => {
            userOwner = getUserPromise(currentService.id_user).then(console.log);
            addressOwner = getAddressOwner(currentService.id_user).then(console.log);
            getRateServicePromice(currentService.id_service).then((rate) => {
                console.log(rate)
                var rateSerivce = 0;
                if (rate) {
                    var rateAmount = 0;
                    var numRate = 0;
                    rate.forEach((currentRate) => {
                        rateAmount = rateAmount + currentRate.nota;
                        numRate = numRate + 1;
                    })
                    rateSerivce = rateAmount / numRate;
                }
            })
        });
    });
});

function getSimpleServicePromise() {
    return new Promise((resolve, reject) => {

        $.get(rota_servico, { about: busca_data.desc }, function () {
        }).done(function (dados) {
            resolve(JSON.parse(dados).data);
        })
    });
}

function getAdvancedServicePromise() {
    return new Promise((resolve, reject) => {

        $.get(rota_servico, NaN, function () {
        }).done(function (dados) {
            resolve(JSON.parse(dados).data);
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

function getAddressOwner(idUser) {
    return new Promise((resolve, reject) => {
        $.get(rota_endereco, { userId: idUser }, () => { }).done((data) => {
            resolve(JSON.parse(data).data[0]);
        });
    });

};

function getRateServicePromice(idServico) {
    return new Promise((resolve, reject) => {

        $.get(rota_avaliacao, { service: idServico }, function () {
        }).done(function (dados) {
            resolve(JSON.parse(dados).data);
        })
    });
}