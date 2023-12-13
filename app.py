from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

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
    conn.commit()
    conn.close()

criar_tabela()

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

@app.route('/dados', methods=['GET'])
def todos_os_dados():
    conn = sqlite3.connect('dados_reserva.db')
    cursor = conn.cursor()
    comando_sql = '''
    SELECT * FROM reservas;
    '''
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    conn.close()
    return render_template('todos_os_dados.html', dados=dados)

# Nova rota para apagar todos os dados
@app.route('/apagar', methods=['GET'])
def apagar_dados():
    with app.app_context():
        apagar_todos_os_dados()
    return redirect(url_for('todos_os_dados'))

if __name__ == '__main__':
    app.run(debug=True)
