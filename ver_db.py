from app import app
from app.models import Usuario

with app.app_context():
    usuarios = Usuario.query.all()

    for usuario in usuarios:
        print(usuario.id, usuario.nome, usuario.sobrenome, usuario.email, usuario.senha, usuario.confirmacao_senha)