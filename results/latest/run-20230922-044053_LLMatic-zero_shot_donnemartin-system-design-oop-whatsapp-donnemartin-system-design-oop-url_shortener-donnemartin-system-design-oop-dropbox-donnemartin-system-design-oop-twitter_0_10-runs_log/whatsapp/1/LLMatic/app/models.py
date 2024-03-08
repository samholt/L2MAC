from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


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
	queued_messages = db.relationship('QueuedMessage', backref='user', lazy='dynamic')
	groups = db.relationship('Group', backref='admin', lazy='dynamic')
	statuses = db.relationship('Status', backref='user', lazy='dynamic')

	# ... rest of the User class ...


class QueuedMessage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	text = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	encrypted = db.Column(db.Boolean, default=False)

# ... rest of the models ...
