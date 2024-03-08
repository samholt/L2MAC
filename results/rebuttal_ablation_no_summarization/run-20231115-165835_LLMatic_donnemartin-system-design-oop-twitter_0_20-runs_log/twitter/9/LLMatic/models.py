from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	_password = db.Column(db.String(128))
	profile_picture = db.Column(db.String(200))
	bio = db.Column(db.String(500))
	website_link = db.Column(db.String(200))
	location = db.Column(db.String(100))
	is_private = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		raise AttributeError('password: write-only field')

	@password.setter
	def password(self, password):
		self._password = generate_password_hash(password)

	def set_password(self, password):
		self._password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self._password, password)
