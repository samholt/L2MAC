from app import db
from flask_jwt_extended import get_jwt_identity


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return '<User %r>' % self.username


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return '<Post %r>' % self.content
