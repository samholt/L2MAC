from app import db
from flask_jwt_extended import get_jwt_identity
from datetime import datetime


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	profile_picture = db.Column(db.String(120), nullable=True)
	bio = db.Column(db.String(280), nullable=True)
	website_link = db.Column(db.String(120), nullable=True)
	location = db.Column(db.String(120), nullable=True)
	is_private = db.Column(db.Boolean, default=False)
	
	def check_password(self, password):
		return check_password_hash(self.password, password)

	def set_password(self, password):
		self.password = generate_password_hash(password)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


class Follow(db.Model):
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class Message(db.Model):
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
