from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	bio = db.Column(db.String(280))
	website = db.Column(db.String(120))
	location = db.Column(db.String(120))
	profile_picture = db.Column(db.String(120))
	is_private = db.Column(db.Boolean, default=False)
	
	# Relationships
	posts = db.relationship('Post', backref='author', lazy=True)
	comments = db.relationship('Comment', backref='author', lazy=True)
	likes = db.relationship('Like', backref='user', lazy=True)
	followers = db.relationship('Follow', backref='follower', lazy=True)
	following = db.relationship('Follow', backref='followee', lazy=True)
	messages_sent = db.relationship('Message', backref='sender', lazy=True)
	messages_received = db.relationship('Message', backref='receiver', lazy=True)
	notifications = db.relationship('Notification', backref='user', lazy=True)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	# Relationships
	comments = db.relationship('Comment', backref='post', lazy=True)
	likes = db.relationship('Like', backref='post', lazy=True)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


class Follow(db.Model):
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	followee_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Notification(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class TrendingTopic(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	topic = db.Column(db.String(80), nullable=False)
	count = db.Column(db.Integer, default=0)
