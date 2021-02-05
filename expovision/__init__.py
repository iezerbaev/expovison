from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from confing import Config

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)