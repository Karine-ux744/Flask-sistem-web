from app import app
from flask import request,render_template,url_for,redirect
from app.models import Usuario
from app.database import database


@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/login",methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    return redirect(url_for("cadastro"))

@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
  if request.method == "GET":
    return render_template("cadastro.html")
  elif request.method == "POST":
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    email = request.form["email"]
    senha = request.form["senha"]
    confirmacao_senha = request.form["confirmacao_senha"]

    usuario_novo = Usuario(nome=nome,sobrenome=sobrenome,email=email,senha=senha,confirmacao_senha=confirmacao_senha)
    database.session.add(usuario_novo)
    database.session.commit()

    return redirect(url_for("login"))

@app.route("/perfil")
def perfil():
  return render_template("perfil.html")
