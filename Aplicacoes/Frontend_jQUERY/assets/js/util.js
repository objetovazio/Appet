

// Mensagem

function mensagem (msg, tipo, tempo){

// Define a cor da mensagem de acordo com o tipo
var cor = ""
if (tipo == "Sucesso"){
  cor = "Cyan";
}else if (tipo == "Erro"){
  cor = "Coral";
}else if (tipo == "Atencao"){
  cor = "Khaki";
}

$("#box-notificacao").css("background-color", cor);
$("#box-notificacao").fadeIn("slow");
$("#msg-notificacao").html(msg);
setTimeout(function(){  $("#box-notificacao").fadeOut("fast");
                        $("#msg-notificacao").html("") }, Number(tempo));
}

// Menu transparente

jQuery(function () {
  jQuery(window).scroll(function () {
    if (jQuery(this).scrollTop() > 200) {
     $("#menu-principal").addClass("menu-principal-transparente");
    } else {
     $("#menu-principal").removeClass("menu-principal-transparente");
    }
  });
});