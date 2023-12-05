<?php
// Conectar ao banco de dados MariaDB
$servername = "127.0.0.1:3306";
$username = "root";
$password = "lngg1234";
$dbname = "reserva";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar a conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Obter os parâmetros da URL
$nomeCompleto = $_GET["nome"];
$email = $_GET["email"];
$numeroTelefone = $_GET["telefone"];
$cpf = $_GET["cpf"];
$dataEscolhida = $_GET["data"];
$numeroParticipantes = $_GET["participantes"];

// Inserir dados no banco de dados usando instruções preparadas
$sql = $conn->prepare("INSERT INTO sua_tabela (nome, email, telefone, cpf, data_escolhida, participantes) 
                       VALUES (?, ?, ?, ?, ?, ?)");

$sql->bind_param("ssssss", $nomeCompleto, $email, $numeroTelefone, $cpf, $dataEscolhida, $numeroParticipantes);

if ($sql->execute()) {
    echo "Dados inseridos com sucesso no banco de dados";
} else {
    echo "Erro ao inserir dados: " . $sql->error;
    error_log($sql->error); // Adicione esta linha para registrar o erro no log do servidor
}

// Fechar a conexão com o banco de dados
$conn->close();
?>
