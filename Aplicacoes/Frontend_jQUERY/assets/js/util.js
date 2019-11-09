

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

function verificarRotaLogado() {
  var rotas_unlogged = ['index.html', 'cadastro-servico.html', 'login.html', 'novo-usuario.html'];
  var rotaAtual = document.location.href.match(/[^\/]+$/)[0];

  if (!rotas_unlogged.includes(rotaAtual)) {
    $.ajaxSetup({
      headers: {
        'x-access-token': $.cookie('token')
      }
    });

    $.get(rota_sessao, function (logged_user) {
      var data = JSON.parse(logged_user);

      if (data['success'] == false) {
        if (!rotas_unlogged.includes(rotaAtual)) {
          mensagem("Usuário deve estar logado para acessar página atual.", "Erro", 5000);
          setTimeout(function () {
            window.location = './index.html';
          }, 2000);
        }
      }
    }).fail(function (msg) {
      var texto = " " + msg.status + " | Motivo: " + msg.responseText;
      mensagem(texto, "Erro", 5000);
    });;
  }
}


$(function () {
  $("#header").load("./templates/header.html");
  $("#footer").load("./templates/footer.html");


  verificarRotaLogado();
})