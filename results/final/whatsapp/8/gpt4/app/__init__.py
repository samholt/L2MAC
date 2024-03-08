from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_socketio import SocketIO
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
mail = Mail(app)
socketio = SocketIO(app)

from app.users.routes import users
from app.messages.routes import messages
from app.main.routes import main
from app.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(messages)
app.register_blueprint(main)
app.register_blueprint(errors)
