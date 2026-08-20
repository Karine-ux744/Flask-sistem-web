from app import app
from flask import request,render_template,url_for,redirect, session
from app.models import Usuario
from app.database import database
import re
from werkzeug.security import generate_password_hash,check_password_hash


@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/login",methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    senha_login = request.form["senha"].strip()
    email_login = request.form["email"].strip()

    consulta = database.select(Usuario).where(Usuario.email==email_login)
    resultado_consulta = database.session.execute(consulta)
    usuario = resultado_consulta.scalar_one_or_none()

    if not usuario:
      return redirect(url_for('cadastro'))
    elif check_password_hash(usuario.senha,senha_login):
      session["usuario_id"] = usuario.id
      return redirect(url_for("perfil",usuario=usuario))
    else:
      return "Senha incorreta, tente novamente."

@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
  if request.method == "GET":
    return render_template("cadastro.html")
  elif request.method == "POST":
    nome = request.form["nome"].strip()
    sobrenome = request.form["sobrenome"].strip()
    email = request.form["email"].strip()
    senha = request.form["senha"].strip()
    confirmacao_senha = request.form["confirmacao_senha"].strip()
    dados = [nome,sobrenome,email,senha,confirmacao_senha]

   #nome só aceita letras, espaço, acento e limite de caracteres
    padrao_nome = re.search(r"^[a-zA-ZÀ-ÖØ-öø-ÿ ]{1,50}$",nome)
   #sobrenome a mesma coisa do nome
    padrao_sobrenome = re.search(r"^[a-zA-ZÀ-ÖØ-öø-ÿ ]{1,50}$",sobrenome)
   #senha deve ter pelo menos 1 maiúscula, pelo menos 1 minúscula, pelo menos 1 carcter especial, pelo menos 1 número, pelo menos 8 carcteres
    padrao_senha = re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&*])(?=.*\d)[a-zA-Z\d!@#$%&*]{8,}",senha)
   #senha e confirmacao_senha devem ser iguais
    if "" in dados:
      return "Preencha todos campos!"
    if senha != confirmacao_senha:
      return "As senhas devem ser iguais."
   #email deve estar no formato de email
    padrao_email = re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+",email)
    if not padrao_nome:
      return"Por favor, insira um nome válido."
    if not padrao_sobrenome:
      return"Por favor, insira uma sobrenome válido."
    if not padrao_senha:
      return"Por favor, insira uma senha válida."
    if not padrao_email:
      return"Por favor, insira um email válido."
    
    consulta = database.select(Usuario).where(Usuario.email==email)
    resultado_consulta = database.session.execute(consulta)
    usuario_cadastrado = resultado_consulta.scalar_one_or_none()
    if usuario_cadastrado:
      return "Esse e-mail já está cadastrado. Faça o login para entrar"

    hash_senha = generate_password_hash(senha)
    usuario_novo = Usuario(nome=nome,sobrenome=sobrenome,email=email,senha=hash_senha)
    database.session.add(usuario_novo)
    database.session.commit()

    return redirect(url_for("login"))

@app.route("/perfil",methods=["GET","POST"])
def perfil():
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return redirect(url_for("login"))

    usuario = database.session.get(Usuario, usuario_id)

    if request.method == "POST":
        feedback = request.form["feedback"]
        print(feedback)

    return render_template("perfil.html", usuario=usuario)

@app.route("/logout")
def logout():
  usuario_id = session.get("usuario_id")
  print("O usuário está logado mas está saindo")

  if not usuario_id:
    return redirect(url_for("login"))
  session.pop("usuario_id",None)
  print("O usuário não está logado mais")
  return redirect(url_for("homepage"))
