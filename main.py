from flask import Flask, request, redirect, session
from database import logar, cadastrar_usuario
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from flask import render_template

# Carregando credenciais para conexão
load_dotenv((find_dotenv()))
password = os.environ.get("MONGODB_PWD")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Estabelencendo conexão com banco de dados
connection_string = f'mongodb+srv://lakdodo:{password}@everymind-challenge.7qpsqlq.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)

# Acessando nossa collections com os dados dos usuários
usuarios_db = client.Usuarios
collection = usuarios_db.Usuarios

# Criando aplicação com rotas
app = Flask(__name__)
app.config['SECRET_KEY'] = f'{SECRET_KEY}'


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form['usuario']
    senha = request.form['senha']
    return logar(login=login, senha=senha)


@app.route('/verificar', methods=['POST'])
def verificar():
    fullname = request.form['fullname']
    login = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    CPF = request.form['CPF']
    return cadastrar_usuario(fullname=fullname, login=login, senha=senha, email=email, CPF=CPF)


@app.route('/loginsucces')
def log_suc():
    return 'LOGIN SUCCESS!'


app.run(debug=True)
