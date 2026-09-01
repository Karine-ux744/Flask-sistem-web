from app.database import database
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def user_loader(id_usuario):
  return database.session.get(Usuario,int(id_usuario))

class Usuario(database.Model,UserMixin):
  id = database.Column(database.Integer,primary_key=True)
  nome = database.Column(database.String(100),nullable=False)
  sobrenome = database.Column(database.String(100),nullable=False)
  email = database.Column(database.String(150),nullable=False,unique=True)
  senha = database.Column(database.String(300),nullable=False)