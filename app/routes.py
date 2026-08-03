from app import app
from flask import request,render_template


@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/perfil")
def perfil():
  return render_template("perfil.html")

@app.route("/login",methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  if request.method == "POST":
    return f"Você enviou os seguintes dados: {request.form}"

@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
  if request.method == "GET":
    return render_template("cadastro.html")
  if request.method == "POST":
    return f"Você enviou os seguintes dados: {request.form}"
