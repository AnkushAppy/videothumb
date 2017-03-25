from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
db = SQLAlchemy(app)


app.config.from_object('config')
from app import views