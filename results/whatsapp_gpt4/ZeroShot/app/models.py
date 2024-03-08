from app import db, login_manager
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	status_message = db.Column(db.String(100), nullable=True)
	last_seen = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	privacy_settings = db.relationship('PrivacySettings', backref='user', lazy=True)
	contacts = db.relationship('Contact', backref='user', lazy=True)
	messages = db.relationship('Message', backref='user', lazy=True)
	groups = db.relationship('Group', backref='user', lazy=True)
	statuses = db.relationship('Status', backref='user', lazy=True)

	def set_password(self, password):
		self.password = pbkdf2_sha256.hash(password)

	def check_password(self, password):
		return pbkdf2_sha256.verify(password, self.password)

	def __repr__(self):
		return f'User({self.email}, {self.profile_picture})'

# Other models for Contact, Message, Group, Status, PrivacySettings will be defined here
