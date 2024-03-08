from app import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
	id: int
	username: str
	email: str
	password: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)

@dataclass
class Post(db.Model):
	id: int
	user_id: int
	content: str

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	content = db.Column(db.String(280), nullable=False)

@dataclass
class Follow(db.Model):
	follower_id: int
	followed_id: int

	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
