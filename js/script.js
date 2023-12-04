// script.js
function submitForm() {
    // Obter os valores dos campos
    var nomeCompleto = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var numeroTelefone = document.getElementById("numero").value;
    var cpf = document.getElementById("numero").value;
    var dataEscolhida = document.getElementById("data").value;
    var numeroParticipantes = document.getElementById("numeroParticipantes").value;

    // Construir a URL de redirecionamento com os parâmetros
    var urlConfirmacao = "./confirmacao.html" +
        "?nome=" + encodeURIComponent(nomeCompleto) +
        "&email=" + encodeURIComponent(email) +
        "&telefone=" + encodeURIComponent(numeroTelefone) +
        "&cpf=" + encodeURIComponent(cpf) +
        "&data=" + encodeURIComponent(dataEscolhida) +
        "&participantes=" + encodeURIComponent(numeroParticipantes);

    // Redirecionar para a página de confirmação
    window.location.href = urlConfirmacao;
}
