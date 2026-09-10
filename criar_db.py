from app.database import database
from app import app 
from app.models import Usuario

url_database = os.environ.get('DATABASE_URL')
if url_database and url_database.startswith("postgres://"):
  url_database = url_database.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_DATABASE_URI'] = url_database or 'sqlite:///local.db'

with app.app_context():
  database.create_all()