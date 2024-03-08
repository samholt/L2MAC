from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
socketio = SocketIO(app)

from user import User
from message import Message
from group import Group
from user_controller import user_blueprint
from message_controller import message_blueprint
from group_controller import group_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(message_blueprint)
app.register_blueprint(group_blueprint)

if __name__ == '__main__':
    socketio.run(app)
