from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def get_token(self):
		return create_access_token(identity=self.id)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id
