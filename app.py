from flask import Flask, render_template, request

app = Flask(__name__)

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
    return "Dados do cadastro recebidos"

@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
  if request.method == "GET":
    return render_template("cadastro.html")
  if request.method == "POST":
    return "Dados para criar conta recebidos."

if __name__ == "__main__":
  app.run(debug=True)
