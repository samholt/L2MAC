from app import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
	id: int
	username: str
	email: str
	password: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(128))

@dataclass
class Post(db.Model):
	id: int
	body: str
	user_id: int

	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
