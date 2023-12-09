// Função para formatar o telefone
function formatarTelefone(input) {
    // Remove caracteres não numéricos
    var telefone = input.value.replace(/\D/g, '');

    // Adiciona parênteses ao redor dos dois primeiros dígitos
    telefone = '(' + telefone.substring(0, 2) + ')' + telefone.substring(2);

    // Atualiza o valor do campo de entrada
    input.value = telefone;
}

