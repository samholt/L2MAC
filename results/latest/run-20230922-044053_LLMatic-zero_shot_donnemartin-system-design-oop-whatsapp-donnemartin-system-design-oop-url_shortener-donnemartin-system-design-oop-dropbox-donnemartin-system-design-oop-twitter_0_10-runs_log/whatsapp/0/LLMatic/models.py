from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	status_message = db.Column(db.String(100))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	privacy_settings = db.Column(db.String(50), default='Everyone')
	contacts = db.relationship('Contact', backref='user', lazy='dynamic')
	messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='author', lazy='dynamic')
	messages_received = db.relationship('Message', foreign_keys='Message.receiver_id', backref='recipient', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def get_profile_picture(self):
		return self.profile_picture

	def set_status_message(self, message):
		self.status_message = message

	def get_status_message(self):
		return self.status_message

	def update_privacy_settings(self, settings):
		self.privacy_settings = settings

	def block_contact(self, contact):
		contact.blocked = True
		db.session.commit()

	def unblock_contact(self, contact):
		contact.blocked = False
		db.session.commit()

	def send_message(self, recipient, text):
		msg = Message(author=self, recipient=recipient, body=text)
		db.session.add(msg)
		db.session.commit()


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	contact_id = db.Column(db.Integer)
	blocked = db.Column(db.Boolean, default=False)


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	text = db.Column(db.String(140))
	read = db.Column(db.Boolean, default=False)
	image = db.Column(db.String(20), nullable=True)
