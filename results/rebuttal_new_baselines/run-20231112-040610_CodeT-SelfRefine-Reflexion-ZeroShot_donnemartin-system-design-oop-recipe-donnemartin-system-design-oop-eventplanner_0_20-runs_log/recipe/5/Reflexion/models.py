from dataclasses import dataclass
from db import db

@dataclass
class User(db.Model):
	id: int
	username: str
	email: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

@dataclass
class Recipe(db.Model):
	id: int
	title: str
	instructions: str
	user_id: int

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), nullable=False)
	instructions = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
