$(document).ready(function () {
    $('#searchBtn').click(()=>{
        var termInput = $('#searchTerm').val();
        window.location.href = './resultado-busca.html?desc='+termInput;
    });
});