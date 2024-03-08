from app import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
	id: int
	username: str
	email: str
	password: str

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))
