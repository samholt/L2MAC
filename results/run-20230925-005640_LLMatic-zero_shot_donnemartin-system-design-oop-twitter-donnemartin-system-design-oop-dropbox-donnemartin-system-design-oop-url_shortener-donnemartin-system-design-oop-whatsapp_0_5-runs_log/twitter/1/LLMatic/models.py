from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


db = SQLAlchemy()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	profile_picture = db.Column(db.String(200), nullable=True)
	bio = db.Column(db.String(280), nullable=True)
	website_link = db.Column(db.String(200), nullable=True)
	location = db.Column(db.String(100), nullable=True)
	is_private = db.Column(db.Boolean, default=False)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	image_url = db.Column(db.String(200), nullable=True)
	created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Retweet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Follow(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Notification(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	content = db.Column(db.String(280), nullable=False)
	created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Trend(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hashtag = db.Column(db.String(80), unique=True, nullable=False)
	count = db.Column(db.Integer, default=0)
