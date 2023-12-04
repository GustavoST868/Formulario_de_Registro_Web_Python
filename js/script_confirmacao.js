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

    } else {
        // Se não houver parâmetros, exibir uma mensagem padrão
        document.querySelector("#nome-confirmacao").innerText = "Erro!";
    }

    // ... outros processamentos na página de confirmação
});

function submitForm() {
    var params = new URLSearchParams(window.location.search);
    var email = params.get("email");

    // Construa o link com os dados preenchidos
    var mailtoLink = `mailto:${email}?subject=Confirmação&body=Detalhes da confirmação:%0A%0A
        Nome: ${params.get("nome")}%0A
        E-mail: ${email}%0A
        Telefone: ${params.get("telefone")}%0A
        CPF: ${params.get("cpf")}%0A
        Data: ${params.get("data")}%0A
        Participantes: ${params.get("participantes")}`;

    // Abra o cliente de e-mail padrão com os dados preenchidos
    window.location.href = mailtoLink;

    // Redirecione para a página final
    window.location.href = "./final.html";
}