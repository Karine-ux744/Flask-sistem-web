from flask import Flask, render_template, request
from app.database import database

app = Flask(__name__)
app.conig["SQL_DATABASE_URI"] = "sqlite:///site.db"
database.init_app(app)

from app import routes

