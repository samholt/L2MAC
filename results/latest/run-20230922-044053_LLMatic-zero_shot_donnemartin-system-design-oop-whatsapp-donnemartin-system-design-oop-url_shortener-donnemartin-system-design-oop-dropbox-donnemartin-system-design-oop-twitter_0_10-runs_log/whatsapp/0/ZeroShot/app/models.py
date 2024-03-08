from app import db, login_manager
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from datetime import datetime


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	status_message = db.Column(db.String(120), nullable=True)
	privacy_settings = db.Column(db.String(20), nullable=False, default='public')

	def set_password(self, password):
		self.password = pbkdf2_sha256.hash(password)

	def check_password(self, password):
		return pbkdf2_sha256.verify(password, self.password)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
