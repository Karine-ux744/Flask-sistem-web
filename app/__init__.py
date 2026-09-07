from flask import Flask
from app.database import database
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
database.init_app(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view="login"

load_dotenv()
secret_key = os.getenv("app.config['SECRET_KEY']")
from app import routes
