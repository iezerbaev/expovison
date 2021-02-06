from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


from config import Config

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index' 
login_manager.login_message = 'Для доступа к данной странице нужно сделать регистрацию или войти в свой аккаунт!'
login_manager.login_message_category = 'info'

from expovision import routes