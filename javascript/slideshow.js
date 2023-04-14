// seleciona o primeiro input
var inputIndex = 1;
var input = document.getElementById("slide" + inputIndex);
if (input) {
  input.checked = true;
}

// variável para controlar se todos os slides foram exibidos uma vez
var todosSlidesExibidos = false;

// alterna a seleção de inputs a cada 5 segundos
var intervalo = setInterval(function() {
  // desmarca o input atual
  var currentInput = document.getElementById("slide" + inputIndex);
  if (currentInput) {
    currentInput.checked = false;
  }

  // incrementa o índice do input
  inputIndex++;

  // se chegou ao fim, volta para o início
  if (inputIndex > 3) {
    // se todos os slides foram exibidos uma vez, para o intervalo
    if (todosSlidesExibidos) {
      clearInterval(intervalo);
    } else {
      // senão, marca que todos os slides foram exibidos uma vez
      todosSlidesExibidos = true;
      inputIndex = 1;
    }
  }

  // seleciona o novo input
  var newInput = document.getElementById("slide" + inputIndex);
  if (newInput) {
    newInput.checked = true;
  }
}, 3000);
