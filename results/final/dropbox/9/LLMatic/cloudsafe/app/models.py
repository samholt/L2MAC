from datetime import datetime
from . import db
from sqlalchemy.dialects.postgresql import ARRAY


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	files = db.relationship('File', backref='owner', lazy='dynamic')
	shared_folders = db.Column(db.PickleType(), default=list)
	activities = db.relationship('Activity', backref='user', lazy='dynamic')

	def __init__(self, username, email):
		self.username = username
		self.email = email


class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(128))
	data = db.Column(db.LargeBinary)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	versions = db.Column(db.PickleType(), default=list)
	share_id = db.Column(db.String(36))

	def __init__(self, filename, data, owner):
		self.filename = filename
		self.data = data
		self.owner = owner


class Activity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	action = db.Column(db.String(64))
	target = db.Column(db.String(128))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, action, target, user):
		self.action = action
		self.target = target
		self.user = user
