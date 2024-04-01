from flask import Flask, request, render_template, redirect, flash
import requests
import json
from flask_bcrypt import Bcrypt

link = "https://reconview-1410a-default-rtdb.firebaseio.com/"
app = Flask(__name__)
bcrypt = Bcrypt(app)
# Defina a chave secreta aqui
app.secret_key = 'sua_chave_secreta_aqui'


@app.route('/')
def retorno():
    try:
        return render_template('tela_login.html')
    except Exception as e:

        print(f"Erro na rota /: {e}")
        flash('Ocorreu um erro durante a exibição da página de login.')
        return render_template('tela_login.html')
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    try:
        lista_provedores = ["hotmail", "gmail", "outlook"]

        if request.method == 'POST':
            nome = request.form.get('nome')
            sobrenome = request.form.get('sobrenome')
            email = request.form.get('email')
            celular = request.form.get('celular')
            senha = request.form.get('senha')
            senha_confirmacao = request.form.get('senha1')

            if not nome or not email or not senha or not senha_confirmacao or not sobrenome or not celular:
                flash('Preencha todos os campos.')
            elif "@" not in email or email.split("@")[1].split(".")[0] not in lista_provedores:
                flash('Formato de email inválido')
            elif senha != senha_confirmacao:
                flash('As senhas não coincidem.')
            else:
                senha_criptografada = bcrypt.generate_password_hash(senha).decode('utf-8')

                response = requests.get(f'{link}/users.json')
                data = response.json()

                if data:
                    emails_existentes = [user.get('email') for user in data.values() if 'email' in user]
                    if email in emails_existentes:
                        flash('E-mail já cadastrado.')
                    else:
                        dados = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'celular': celular, 'senha': senha_criptografada}
                        criar = requests.post(f'{link}/users.json', data=json.dumps(dados))

                        if criar.status_code == 200:
                            flash('Usuário cadastrado com sucesso.')
                        else:
                            print(f'Falha ao cadastrar usuário. Status Code: {criar.status_code}')
                            flash('Falha ao cadastrar usuário')
                else:
                    dados = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'celular': celular, 'senha': senha_criptografada}
                    criar = requests.post(f'{link}/users.json', data=json.dumps(dados))

                    if criar.status_code == 200:
                        flash('Usuário cadastrado com sucesso.')
                    else:
                        print(f'Falha ao cadastrar usuário. Status Code: {criar.status_code}')
                        flash('Falha ao cadastrar usuário')

        return render_template('tela_cadastro.html')

    except Exception as e:
        print(f"Erro na rota /cadastrar: {e}")
        flash('Ocorreu um erro durante o cadastro.')
        return render_template('tela_cadastro.html')
