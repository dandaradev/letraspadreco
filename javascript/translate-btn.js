var div = document.getElementById("conteudo");
var conteudoInicial = div.innerHTML;
var novoConteudo = div.getAttribute("data-novo-conteudo");

function alterarConteudo() {
  div.innerHTML = novoConteudo;
}

function recuperarConteudo() {
  div.innerHTML = conteudoInicial;
}
