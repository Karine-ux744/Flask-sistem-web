from app import app,bcrypt
from flask import render_template,url_for,redirect
from flask_login import login_required,current_user,login_user,logout_user
from app.models import Usuario
from app.database import database
from app.forms import FazerLogin,Cadastrar,EditarPerfil

@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
  form_cadastro = Cadastrar()
  if form_cadastro.validate_on_submit():
    if Usuario.query.filter_by(email=form_cadastro.email.data).first():
      return redirect(url_for("login"))
    senha = bcrypt.generate_password_hash(form_cadastro.senha.data)
    usuario = Usuario(nome=form_cadastro.nome.data,sobrenome=form_cadastro.sobrenome.data,email=form_cadastro.email.data,senha=senha)
    database.session.add(usuario)
    database.session.commit()

    return redirect(url_for("login"))
    
  return render_template("cadastro.html",form=form_cadastro)

@app.route("/login",methods=["GET","POST"])
def login():
  form_login=FazerLogin()
  if form_login.validate_on_submit():
    usuario = Usuario.query.filter_by(email=form_login.email.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha,form_login.senha.data):
      login_user(usuario,remember=True)
      return redirect(url_for("perfil",usuario=usuario.nome))
    
    return redirect(url_for("cadastro"))
    
  return render_template("login.html",form=form_login)

@login_required
@app.route("/perfil/<usuario>")
def perfil(usuario):
  return render_template("perfil.html")

@login_required
@app.route("/perfil/editar",methods=["GET","POST"])
def editar_perfil():
  form_editar_perfil = EditarPerfil()
  if form_editar_perfil.validate_on_submit():
    usuario = current_user
    usuario.nome = form_editar_perfil.nome.data
    usuario.sobrenome = form_editar_perfil.sobrenome.data
    usuario.email = form_editar_perfil.email.data
    senha = bcrypt.genterate_password_hash(form_editar_perfil.senha.data)
    usuario.senha = senha

    database.session.commit()
    return redirect(url_for("perfil",usuario=usuario.nome))
  return render_template("editar_perfil.html",form=form_editar_perfil)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("homepage"))
