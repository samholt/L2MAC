from app import db
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
	
	def __repr__(self):
		return '<User %r>' % self.username


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Post %r>' % self.id


class Follow(db.Model):
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Follow %r>' % self.follower_id


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return '<Message %r>' % self.id
