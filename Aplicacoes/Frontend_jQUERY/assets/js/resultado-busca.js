const busca_data = {}
location.search.substr(1).split("&").forEach(function (item) { busca_data[item.split("=")[0]] = item.split("=")[1] });
$(document).ready(function () {
    var finded_service = getSimpleServicePromise().then((serviceData) => {
        
        serviceData.forEach((currentService) => {
            $('#resultArea').append(
            
                '<div class="row" style="" id="result"'+serviceData.id_service+'>'+ 
                `
                <div class="col-md-12 mb-4 bg-light" style="">
                  <div class="form-group">
                    <div class="form-group">
                      <a href="#" style="color: black" title="Carlos Silva">
                        <div class="form-group">
                          <div class="row shadow-sm mb-1">
                            <div class="col-md-4 p-3" style=""><img class="img-fluid d-block rounded-circle mx-auto shadow-none"
                                src="assets/image/icone_padrao.png" width="200" height="200"></div>
                            <div class="my-2 col-md-7" style="">
                              <div class="card">
                                <div class="card-body shadow-sm">
                                  <h5 class="card-title mb-3"><b>_OWNERNAME</b></h5>
                                  <p class="card-text">Avaliação: <b>_AVERATE <i class="fa fa-3 fa-star" style="color:yellow"></i></b>
                                  </p>
                                  <p class="card-text">Valor do Serviço: <b>R$</b> <b>_VALUESERV</b></p>
                                  <p class="card-text" contenteditable="true">Endereço: <b>_ENDERECO</b>
                                  </p>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              `
            );
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