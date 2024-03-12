from app import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash

@dataclass
class User(db.Model):
	id: int
	username: str
	email: str
	password: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)

	def __repr__(self):
		return '<User %r>' % self.username
