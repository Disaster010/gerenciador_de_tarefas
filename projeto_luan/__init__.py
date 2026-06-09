from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luan.db'
app.config['SECRET_KEY'] = '3618c02e8d11425b382fdea1829da17ddfa8fed787c52daff6ba9fa55fc3d15b'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from projeto_luan import routes, models

