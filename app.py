from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtem os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        data = request.form['data']
        quantidade_pessoas = request.form['quantidade_pessoas']
        
        string = f'''
        Dados de reserva do formulário:
        nome       = {nome}
        email      = {email}
        cpf        = {cpf}
        telefone   = {telefone}
        data       = {data}
        quantidade = {quantidade_pessoas}
        '''
        print(string)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
