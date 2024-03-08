from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	status = db.Column(db.String(140))
	profile_pic = db.Column(db.String(20), default='default.jpg')
	messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='author', lazy='dynamic')
	messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')
	last_message_read_time = db.Column(db.DateTime)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def avatar(self, size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

	def __repr__(self):
		return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	body = db.Column(db.String(140))
	imestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	status = db.Column(db.String(10), default='unread')

	def __repr__(self):
		return '<Message {}>'.format(self.body)
