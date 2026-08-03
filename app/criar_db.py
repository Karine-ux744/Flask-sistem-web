from app.database import database
from app import app 
from app.models import Usuario

with app.app_context():
  database.create_all()