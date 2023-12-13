from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função que cria as tabelas no banco
def criar_tabela():
    conn = sqlite3.connect('dados_reserva.db')
    cursor = conn.cursor()
    comando_sql = '''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        cpf TEXT,
        telefone TEXT,
        data TEXT,
        quantidade_pessoas INTEGER
    );
    '''
    cursor.execute(comando_sql)
    
    # Altera a sequência do ID para começar em 1
    comando_sql_reset_id = '''
    DELETE FROM sqlite_sequence WHERE name='reservas';
    INSERT INTO sqlite_sequence (name, seq) VALUES ('reservas', 0);
    '''
    cursor.executescript(comando_sql_reset_id)

    conn.commit()
    conn.close()

criar_tabela()

# Função para apagar um dado pelo índice
def apagar_dado_por_indice(indice):
    conn = sqlite3.connect('dados_reserva.db')
    cursor = conn.cursor()
    
    # Verificar se o índice existe e apagar o dado correspondente
    comando_sql = '''
    DELETE FROM reservas WHERE id = ?;
    '''
    cursor.execute(comando_sql, (indice,))
    
    conn.commit()
    conn.close()

# Função para apagar todos os dados da tabela
def apagar_todos_os_dados():
    conn = sqlite3.connect('dados_reserva.db')
    cursor = conn.cursor()
    comando_sql = '''
    DELETE FROM reservas;
    '''
    cursor.execute(comando_sql)
    conn.commit()
    conn.close()

# Função para obter a data atual para que caso a data já tenha passado o banco delete os dados referentes a ela sozinho
def obter_data_atual():
    return datetime.now().strftime('%Y-%m-%d')

# Função para inserir os dados no banco
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        data = request.form['data']
        quantidade_pessoas = request.form['quantidade_pessoas']

        # Conectar ao banco de dados
        conn = sqlite3.connect('dados_reserva.db')
        cursor = conn.cursor()

        # Inserir dados na tabela
        comando_sql = '''
        INSERT INTO reservas (nome, email, cpf, telefone, data, quantidade_pessoas)
        VALUES (?, ?, ?, ?, ?, ?);
        '''
        cursor.execute(comando_sql, (nome, email, cpf, telefone, data, quantidade_pessoas))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão
        conn.close()

    return render_template('index.html')

# Função para mostrar os dados que estão no banco
@app.route('/dados', methods=['GET'])
def todos_os_dados():
    conn = sqlite3.connect('dados_reserva.db')
    cursor = conn.cursor()
    
    # Verificar se a data de reserva já passou e excluir automaticamente os dados
    comando_sql = '''
    SELECT * FROM reservas WHERE data >= ?;
    '''
    cursor.execute(comando_sql, (obter_data_atual(),))
    dados = cursor.fetchall()
    
    conn.close()
    return render_template('todos_os_dados.html', dados=dados)

# Rota para apagar um dado por índice
@app.route('/apagar/<int:indice>', methods=['GET'])
def apagar_dado_por_indice_rota(indice):
    with app.app_context():
        apagar_dado_por_indice(indice)
    return redirect(url_for('todos_os_dados'))

# Rota para apagar todos os dados
@app.route('/apagar', methods=['GET'])
def apagar_todos_os_dados_rota():
    with app.app_context():
        apagar_todos_os_dados()
    return redirect(url_for('todos_os_dados'))

if __name__ == '__main__':
    app.run(debug=True)
