from flask import Flask
from app.database import database
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
database.init_app(app)
app.config["SECRET_KEY"] = "6e734149ec202e64c8ca"
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view="login"

from app import routes

