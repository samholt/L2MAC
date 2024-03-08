from app import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
	username: str
	email: str
	password: str

	username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)

@dataclass
class Post(db.Model):
	id: int
	username: str
	content: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
	content = db.Column(db.String(280), nullable=False)

	db.create_all()
