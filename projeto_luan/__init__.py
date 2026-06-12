from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ti102.db'
app.config['SECRET_KEY'] = '6ebb7ada76a69be57bdc974b81791d5c7a7124ae487050f8aaedc5165f388df4'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from projeto_luan import routes, models
