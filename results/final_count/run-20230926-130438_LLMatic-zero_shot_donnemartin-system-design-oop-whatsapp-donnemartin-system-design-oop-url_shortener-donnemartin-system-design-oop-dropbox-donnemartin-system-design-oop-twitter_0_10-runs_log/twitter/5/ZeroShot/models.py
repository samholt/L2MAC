from app import db
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.orm import backref


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	profile_picture = db.Column(db.String(120), nullable=True)
	bio = db.Column(db.String(280), nullable=True)
	website = db.Column(db.String(120), nullable=True)
	location = db.Column(db.String(120), nullable=True)
	is_private = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<User %r>' % self.username


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=backref('posts', lazy=True))

	def __repr__(self):
		return '<Post %r>' % self.content


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
	post = db.relationship('Post', backref=backref('likes', lazy=True))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user = db.relationship('User', backref=backref('likes', lazy=True))

	def __repr__(self):
		return '<Like %r>' % self.id


class Follow(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	follower = db.relationship('User', backref=backref('following', lazy=True))
	followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	followed = db.relationship('User', backref=backref('followers', lazy=True))

	def __repr__(self):
		return '<Follow %r>' % self.id


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	sender = db.relationship('User', backref=backref('sent_messages', lazy=True))
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	recipient = db.relationship('User', backref=backref('received_messages', lazy=True))
	content = db.Column(db.String(280), nullable=False)

	def __repr__(self):
		return '<Message %r>' % self.content
