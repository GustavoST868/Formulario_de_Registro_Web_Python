// script.js
function submitForm() {
    var nomeCompleto = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var numeroTelefone = document.getElementById("telefone").value;
    var cpf = document.getElementById("cpf").value;
    var dataEscolhida = document.getElementById("data").value;
    var numeroParticipantes = document.getElementById("numeroParticipantes").value;

    var urlConfirmacao = "./confirmacao.html" +
        "?nome=" + encodeURIComponent(nomeCompleto) +
        "&email=" + encodeURIComponent(email) +
        "&telefone=" + encodeURIComponent(numeroTelefone) +
        "&cpf=" + encodeURIComponent(cpf) +
        "&data=" + encodeURIComponent(dataEscolhida) +
        "&participantes=" + encodeURIComponent(numeroParticipantes);

    window.location.href = urlConfirmacao;
}

$(document).ready(function(){
    $('#telefone').inputmask('(99) 9999-9999', { oncomplete: function(){ alert('Telefone completo!'); } });
    $('#cpf').inputmask('999.999.999-99', { oncomplete: function(){ alert('CPF completo!'); } });
});
