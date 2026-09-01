from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from app.models import Usuario
from app.validators import validar_senha


class FazerLogin(FlaskForm):
  email = StringField("Email",validators=[DataRequired(),Email()])
  senha = PasswordField("Senha",validators=[DataRequired(),validar_senha])
  botao_enviar = SubmitField("Entrar")

class Cadastrar(FlaskForm):
  nome = StringField("Nome",validators=[DataRequired()])
  sobrenome = StringField("Sobrenome",validators=[DataRequired()])
  email = StringField("E-mail",validators=[DataRequired(),Email()])
  senha = PasswordField("Senha",validators=[DataRequired(),validar_senha])
  confirmacao_senha = PasswordField("Confirme sua senha",validators=[DataRequired(),EqualTo("senha")])
  botao_enviar=SubmitField("Cadastrar")

  def validate_email(self,email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
      return ValidationError("Esse e-mail já está cadastrado. Faça login para continuar.")

class EditarPerfil(FlaskForm):
  nome = StringField("Nome",validators=[DataRequired(),Length(100)])
  sobrenome = StringField("Sobrenome",validators=[DataRequired(),Length(100)])
  senha = PasswordField("Senha",validators=[DataRequired(),validar_senha])
  confimacao_senha = PasswordField("Confirme a senha",validators=[DataRequired(),EqualTo(senha)])
