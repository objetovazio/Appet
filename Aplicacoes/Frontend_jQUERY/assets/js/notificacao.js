
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


// function sleep(milliseconds) {

//   var start = new Date().getTime();
//   for (var i = 0; i < 1e7; i++) {
//     if ((new Date().getTime() - start) > milliseconds){
//       break;
//     }
//   }
// }

