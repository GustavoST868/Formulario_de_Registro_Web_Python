document.addEventListener("DOMContentLoaded", function () {
    // Obter os parâmetros da URL
    var params = new URLSearchParams(window.location.search);

    // Verificar se há parâmetros específicos
    if (params.has("nome")) {
        // Exibir os dados na página de confirmação
        var nomeCompleto = params.get("nome");
        var email = params.get("email");
        var numeroTelefone = params.get("telefone");
        var cpf = params.get("cpf");
        var dataEscolhida = params.get("data");
        var numeroParticipantes = params.get("participantes");

        // Atualizar o conteúdo da página de confirmação
        document.querySelector("#nome-confirmacao").innerText = "Nome Completo: " + nomeCompleto;
        document.querySelector("#email-confirmacao").innerText = "E-mail: " + email;
        document.querySelector("#telefone-confirmacao").innerText = "Telefone: " + numeroTelefone;
        document.querySelector("#cpf-confirmacao").innerText = "CPF: " + cpf;
        document.querySelector("#data-confirmacao").innerText = "Data: " + dataEscolhida;
        document.querySelector("#participantes-confirmacao").innerText = "Participantes: " + numeroParticipantes;

        // Enviar dados para o PHP usando AJAX
        enviarDadosParaPHP(nomeCompleto, email, numeroTelefone, cpf, dataEscolhida, numeroParticipantes);
    } else {
        // Se não houver parâmetros, exibir uma mensagem padrão
        document.querySelector("#nome-confirmacao").innerText = "Erro!";
    }

    // ... outros processamentos na página de confirmação
});

function enviarDadosParaPHP(nome, email, telefone, cpf, data, participantes) {
    // Use AJAX para enviar dados para o arquivo PHP
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/php/processar_dados.php?nome=" + nome + "&email=" + email + "&telefone=" + telefone + "&cpf=" + cpf + "&data=" + data + "&participantes=" + participantes, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Redirecione após o envio bem-sucedido
            window.location.href = "/html/final.html";
        }
    };
    xhr.send();
}
