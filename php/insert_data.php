<?php
// Get data from the POST request
$nomeCompleto = $_POST['nome'];
$email = $_POST['email'];
$numeroTelefone = $_POST['telefone'];
$cpf = $_POST['cpf'];
$dataEscolhida = $_POST['data'];
$numeroParticipantes = $_POST['participantes'];

// Your database connection details
$servername = "Localhost";
$username = "root";
$password = "lngg1234";
$dbname = "reserva";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data into the database
$sql = "INSERT INTO your_table_name (nome, email, telefone, cpf, data, participantes)
VALUES ('$nomeCompleto', '$email', '$numeroTelefone', '$cpf', '$dataEscolhida', '$numeroParticipantes')";

if ($conn->query($sql) === TRUE) {
    echo "Data inserted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();
?>
