function strip(str) {
    return str.replace(/^\s+|\s+$/g, '');
}


// Mensagem
function mensagem(msg, tipo, tempo) {

  // Define a cor da mensagem de acordo com o tipo
  var cor = ""
  if (tipo == "Sucesso") {
    cor = "Cyan";
  } else if (tipo == "Erro") {
    cor = "Coral";
  } else if (tipo == "Atencao") {
    cor = "Khaki";
  }

  $("#box-notificacao").css("background-color", cor);
  $("#box-notificacao").fadeIn("slow");
  $("#msg-notificacao").html(msg);
  setTimeout(function () {
    $("#box-notificacao").fadeOut("fast");
    $("#msg-notificacao").html("")
  }, Number(tempo));
}

// Menu transparente

jQuery(function () {
  jQuery(window).scroll(function () {
    if (jQuery(this).scrollTop() > 200) {
      $("#menu-principal").addClass("menu-principal-transparente");
      $("#topo").removeClass("topo-visivel");
    } else {
      $("#menu-principal").removeClass("menu-principal-transparente");

      $("#topo").addClass("topo-visivel");
    }
  });
});

// Função ir ao topo

function paraTopo() {
  $('html, body').animate({ scrollTop: 0 }, 'slow');
}

$(function () {
  $("#header").load("./templates/header.html");
  $("#footer").load("./templates/footer.html");
})
