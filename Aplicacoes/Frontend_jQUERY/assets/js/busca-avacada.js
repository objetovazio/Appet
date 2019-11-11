$(document).ready(function () {
    getTypeService();
    $('#searchBtn').click(()=>{
        var typeService = $('#tiposervico').children("option:selected").val();
        var bairroText = $('#Bairro').val();
        var cidadeText = $('#Cidade').val();
        var estatoText = $('#Estado').val();
        typeServiceQuery = typeService != 0 ? ('serv='+typeService+'&') : 'serv=none&';
        bairroQuery = bairroText != ''? ('bairro='+bairroText.replace(/ /g,'_')) : 'bairro=none&';
        cidadeQuery = cidadeText != ''? ('cidade='+cidadeText.replace(/ /g,'_')) : 'cidade=none&'; 
        estadoQuery = estatoText != ''? ('estado='+estatoText.replace(/ /g,'_')) : 'estado=none';
        
        window.location.href = './resultado-busca.html?'+typeServiceQuery+bairroQuery+cidadeQuery+estadoQuery;
    });
});

function getTypeService(){
    $.get(rota_tipo_servico,{},()=>{

    }).done((dataResponse)=>{
        typeServicesData = JSON.parse(dataResponse).data;
        typeServicesData.forEach( (currentValue)=>{
            $('#tiposervico').append(
                '<option value="'+currentValue.id+'">'+currentValue.nome+"</option>"
            );
        });
    })
}