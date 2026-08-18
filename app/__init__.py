from flask import Flask
from app.database import database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
database.init_app(app)
app.config["SECRET_KEY"] = "chave secreta da sessão"

from app import routes

