from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)
	
	def set_password(self, password):
		self.password = generate_password_hash(password)
	
	def check_password(self, password):
		return check_password_hash(self.password, password)
	
	def get_token(self, expires_in=600):
		return create_access_token(identity=self.id, expires_delta=timedelta(seconds=expires_in))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Follow(db.Model):
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.Text, nullable=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
