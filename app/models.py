from app.database import database

class Usuario(database.Model):
  id = database.Column(database.Integer,primary_key=True)
  nome = database.Column(database.String(100),nullable=False)
  sobrenome = database.Column(database.String(100),nullable=False)
  email = database.Column(database.String(150),nullable=False,unique=True)
  senha = database.Column(database.String(300),nullable=False)