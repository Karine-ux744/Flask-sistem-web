from flask import Flask
from app.database import database
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view="login"

load_dotenv()
app.config["SECRET_KEY"] = os.getenv("app.config['SECRET_KEY']")
url_database = os.environ.get('DATABASE_URL')
if url_database and url_database.startswith("postgres://"):
  url_database = url_database.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = url_database or 'sqlite:///local.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)

from app import routes
