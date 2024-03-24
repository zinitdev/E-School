from app import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
# toolbar = DebugToolbarExtension(app)