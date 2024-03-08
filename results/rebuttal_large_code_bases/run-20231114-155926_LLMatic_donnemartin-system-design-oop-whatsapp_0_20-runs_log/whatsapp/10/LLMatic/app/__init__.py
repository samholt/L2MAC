import os
from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/mydatabase')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.googlemail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', '587'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

import app.views
