from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from flask import redirect, flash, request, session


# Carregando credenciais para conexão
load_dotenv((find_dotenv()))
password = os.environ.get("MONGODB_PWD")

# Conectando ao servidor
connection_string = f'mongodb+srv://lakdodo:{password}@everymind-challenge.7qpsqlq.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)

# Acessando nossa collections com os dados dos usuários
usuarios_db = client.Usuarios
collection = usuarios_db.Usuarios


def cadastrar_usuario(fullname, login, senha, email, CPF):

    cadastro = {
        "Nome completo": f'{fullname}',
        "login": f"{login}",
        "senha": f"{senha}",
        "email": f"{email}",
        "CPF": f"{CPF}"
    }
    if not collection.find_one({"login": f"{login}"}):
        if not collection.find_one({"email": f"{email}"}):
            if not collection.find_one({"CPF": f"{CPF}"}):
                collection.insert_one(cadastro)
                return redirect('/')
            else:
                flash("CPF já cadastrado.")

                return redirect('/cadastro')
        else:
            flash("Email já cadastrado.")
            return redirect('/cadastro')
    else:
        flash("Usuario já cadastrado")
        return redirect('/cadastro')


def logar(login, senha):
    if collection.find_one({"login": f"{login}"}):

        if collection.find_one({"senha": f"{senha}"}):
            session['usuario_logado'] = request.form['usuario']
            return redirect('/loginsucces')
        else:
            flash("senha incorreta")
            return redirect('/')

    else:
        flash("login inexistente")
        return redirect('/')
