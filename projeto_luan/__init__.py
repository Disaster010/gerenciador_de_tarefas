from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luan.db'
database = SQLAlchemy(app)

from projeto_luan import routes, models

