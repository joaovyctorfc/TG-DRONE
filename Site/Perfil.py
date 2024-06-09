
from flask import Flask, request, render_template, redirect, flash,session
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
        return render_template('tela_principal.html')
    except Exception as e:
        # Trate ou registre o erro conforme necessário
        print(f"Erro na rota /: {e}")
        flash('Ocorreu um erro durante a exibição da página principal.')
        return render_template('tela_principal.html')
@app.route('/perfil', methods=['POST', 'GET'])
def perfil(user_email=['email'], user_nome=['nome']):
    try:
        if 'logged_in' in session and session['logged_in']:
            user_email = session['user_email']
            user_nome = session['user_nome']

            lista_provedores = ["hotmail", "gmail", "outlook"]

            if request.method == 'POST':
              nome = request.form.get('nome')
              sobrenome = request.form.get('sobrenome')
              email = request.form.get('email')
              celular = request.form.get('celular')
              senha = request.form.get('senha')
              senha_confirmacao = request.form.get('senha1')
            else:
                # Se o método for GET, é uma solicitação de carregamento da página de perfil
                # Aqui você deve fazer uma solicitação ao seu servidor para obter os dados do usuário
                response = requests.get(f'{link}/users.json')
                data = response.json()

                # Verifica se há dados de usuário retornados pela solicitação
                if data:
                    # Encontra o usuário com base no email
                    usuario = None
                    for user in data.values():
                        if user.get('email') == user_email:
                            usuario = user
                            break

                    # Verifica se o usuário foi encontrado
                    if usuario:
                        # Preencha os campos do formulário com os dados do usuário
                        return render_template('tela_perfil.html', usuario=usuario)
                    else:
                        flash('Usuário não encontrado.')
                        return redirect('/home')
                else:
                    flash('Não há dados de usuário.')
                    return redirect('/home')

        else:
            return redirect('/home')

    except Exception as e:
        # Trate ou registre o erro conforme necessário
        print(f"Erro na rota /perfil: {e}")
        flash('Ocorreu um erro na página de perfil.')
        return redirect('/home')
