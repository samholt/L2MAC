from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from cryptography.fernet import Fernet
from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	profile_picture = db.Column(db.String(120))
	status_message = db.Column(db.String(120))
	privacy_settings = db.Column(db.String(120))
	blocked_contacts = db.Column(db.PickleType)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def get_reset_password_token(self, secret_key, expires_in=600):
		s = URLSafeTimedSerializer(secret_key)
		return s.dumps({'reset_password': self.id}, salt='reset-password-salt')

	@staticmethod
	def verify_reset_password_token(token, secret_key, expires_in=600):
		s = URLSafeTimedSerializer(secret_key)
		try:
			data = s.loads(token, salt='reset-password-salt', max_age=expires_in)
		except:
			return None
		return data['reset_password']

	def block_contact(self, contact):
		if contact not in self.blocked_contacts:
			self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		if contact in self.blocked_contacts:
			self.blocked_contacts.remove(contact)


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	content = db.Column(db.String(120))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	read_receipt = db.Column(db.Boolean, default=False)
	encryption = db.Column(db.Boolean, default=False)

	def encrypt_content(self, key):
		cipher_suite = Fernet(key)
		self.content = cipher_suite.encrypt(self.content.encode()).decode()

	def decrypt_content(self, key):
		cipher_suite = Fernet(key)
		self.content = cipher_suite.decrypt(self.content.encode()).decode()


class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	picture = db.Column(db.String(120))
	participants = db.Column(db.PickleType)
	admins = db.Column(db.PickleType)

	def add_participant(self, user):
		if user not in self.participants:
			self.participants.append(user)

	def remove_participant(self, user):
		if user in self.participants:
			self.participants.remove(user)

	def assign_admin(self, user):
		if user in self.participants and user not in self.admins:
			self.admins.append(user)

	def revoke_admin(self, user):
		if user in self.admins:
			self.admins.remove(user)


class Status(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	image = db.Column(db.String(120))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	visibility = db.Column(db.String(120))

	def set_visibility(self, visibility):
		self.visibility = visibility


class Feedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	feedback = db.Column(db.String(500))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

