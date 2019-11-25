const busca_data = {}
location.search.substr(1).split("&").forEach(function (item) { busca_data[item.split("=")[0]] = item.split("=")[1] });
$(document).ready(function () {
    console.log(busca_data);


    $('#resultArea').html("<div id='spinnerloading' class='d-flex justify-content-center'><div class='spinner-grow' role='status'><span style='margin: auto;' class='sr-only'>Loading...</span></div></div>");
  
    
    mountPageData();

});

function mountPageData() {
    if (Object.keys(busca_data).length == 1) {
        getSimpleServicePromise().then((simpleData) => {
            setInformationPage(simpleData);
        });
    } else {
        getAdvancedServicePromise().then((advancedData) => {
            setInformationPage(advancedData);
        });
    }
}

function setInformationPage(serviceData) {

    if (serviceData != undefined){

           serviceData.forEach((currentService) => {

        contaQuantidade();
        addHtmlResult(currentService.id_service)
        isBrokenValue = String(currentService.price).split('.').length > 1;
        if (isBrokenValue) {
            if (String(currentService.price).split('.')[1].length > 1) {
                $('#value' + currentService.id_service).val(currentService.price);
                $('#value' + currentService.id_service).text(currentService.price);
            }
            else {
                $('#value' + currentService.id_service).val(String(currentService.price) + '0');
                $('#value' + currentService.id_service).text(String(currentService.price) + '0');
            }
        } else {
            $('#value' + currentService.id_service).val(String(currentService.price) + '.00');
            $('#value' + currentService.id_service).text(String(currentService.price) + '.00');
        }
        userOwner = getUserPromise(currentService.id_user).then((currentOwner) => {
            $('#owner' + currentService.id_service).val(currentOwner.name);
            $('#owner' + currentService.id_service).text(currentOwner.name);
            $('#aTitle' + currentService.id_service).attr('title', currentOwner.name);
        });
        addressOwner = getAddressOwner(currentService.id_user).then((currentAddress) => {
            var addressLine = currentAddress.bairro + ", " + currentAddress.city + ", " + currentAddress.state;
            $('#address' + currentService.id_service).val(addressLine);
            $('#address' + currentService.id_service).text(addressLine);
        });
        getRateServicePromice(currentService.id_service).then((rate) => {
            console.log(rate)
            var rateSerivce = 0;
            if (rate.length > 0) {
                var rateAmount = 0;
                var numRate = 0;
                rate.forEach((currentRate) => {
                    rateAmount = rateAmount + currentRate.nota;
                    numRate = numRate + 1;
                })
                rateSerivce = rateAmount / numRate;
            }
            $('#avg' + currentService.id_service).val(rateSerivce);
            $('#avg' + currentService.id_service).text(rateSerivce);
        })
    });
    redirectLogic();
    
    }
 

    $('#spinnerloading').remove();
}

function redirectLogic() {
    $('a').click((event) => {
        console.log(event);
        var serviceContractData = event.currentTarget.innerText.split('\n');
        var selectedService = event.currentTarget.id.slice(6);
        var rateService = serviceContractData[2].slice(11).replace(' ', '');
        //var serviceValue = serviceContractData[4].slice(20).replace(' ','');
        var addressService = serviceContractData[6].slice(10).replace(/ /g, '_').replace(/,/g, '-');
        var today = new Date();
        var formatDateRequest = String(today.getFullYear()) + String(today.getMonth()) + String((today.getDate() > 10) ? today.getDate() : '0' + String(today.getDate()));
        var parametersUrl = 'usuario=2&servico=' + selectedService + '&horario=6&data=' + formatDateRequest + '&rateServ=' + rateService + '&addressServ=' + addressService;
        document.location.href = './pagamento-servico.html?' + parametersUrl;
    })
}


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
        endereco = getOwnerByAddress().then((responsePromise) => {
            console.log(responsePromise)
            dataSend = null;
            if (responsePromise != null) {
                dataSend = {
                    'typeService': busca_data.serv != 'none' ? busca_data.serv : '',
                    'ownerId': JSON.stringify(responsePromise)
                };
            } else {
                dataSend = {
                    'typeService': busca_data.serv !='none' ? busca_data.serv : ''
                };
            }
            console.log(dataSend);
            $.get(rota_servico, dataSend, function () {
            }).done(function (dados) {
                resolve(JSON.parse(dados).data);
            })
        });

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

function getOwnerByAddress() {
    return new Promise((resolve, reject) => {
        have_value = busca_data.bairro != 'none' || busca_data.cidade != 'none' || busca_data.estado != 'none'
        if (have_value) {
            dataSend = {
                'bairro': busca_data.bairro != 'none' ? busca_data.bairro.replace(/_/g, ' ') : '',
                'cidade': busca_data.cidade != 'none' ? busca_data.cidade.replace(/_/g, ' ') : '',
                'estado': busca_data.estado != 'none' ? busca_data.estado.replace(/_/g, ' ') : ''
            }
            console.log(dataSend);
            $.get(rota_endereco, dataSend, function () {

            }).done((responseGet) => {
                jsonResponse = JSON.parse(responseGet).data;
                users_id = [];
                jsonResponse.forEach((currentData) => {
                    if (!users_id.includes(currentData.id_user)) {
                        users_id.push(currentData.id_user);
                    }
                })
                resolve(users_id);
            })
        }
        else {
            resolve(null)
        }
    })

}

function addHtmlResult(currentServId) {
    var infoServHtml = `
            <div class="row" style="cursor:pointer" id="result_IDSERV>
            <div class="col-md-12 mb-4 bg-light" style="">
              <div class="form-group">
                <div class="form-group">
                  <a   id="aTitle_IDSERV"style="color: black" title=_TITLEID>
                    <div class="form-group">
                      <div class="row shadow-sm mb-1">
                        <div class="col-md-4 p-3" style=""><img class="img-fluid d-block rounded-circle mx-auto shadow-none"
                            src="assets/image/icone_padrao.png" width="200" height="200"></div>
                        <div class="my-2 col-md-7" style="">
                          <div class="card">
                            <div class="card-body shadow-sm">
                              <h5 class="card-title mb-3"><b id="owner_IDSERV"></b></h5>
                              <p class="card-text">Avaliação: <b id="avg_IDSERV"> </b> <i class="fa fa-3 fa-star" style="color:yellow"></i>
                              </p>
                              <p class="card-text">Valor do Serviço: <b>R$</b> <b id="value_IDSERV"></b></p>
                              <p class="card-text" contenteditable="true">Endereço: <b id="address_IDSERV"></b>
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
          `;
    $('#resultArea').append(
        infoServHtml.replace(/_IDSERV/g, currentServId)
    );
}


function contaQuantidade(){

   var quant =  Number( $("#quantResultado").text() );
   $("#quantResultado").text(quant + 1);
}