from flask import Flask
from flask_login import LoginManager, current_user
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

with app.app_context():
	db.create_all()

import views
