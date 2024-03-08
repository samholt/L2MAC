from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db

# Table for many-to-many relationship between users and their blocked contacts
blocked_contacts = db.Table('blocked_contacts',
    db.Column('blocking_user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('blocked_user_id', db.Integer, db.ForeignKey('user.id'))
)

# Table for many-to-many relationship between groups and their admins
group_admins = db.Table('group_admins',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('admin_id', db.Integer, db.ForeignKey('user.id'))
)

# Table for many-to-many relationship between groups and their participants
group_participants = db.Table('group_participants',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('participant_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
	# User model
	id = Column(Integer, primary_key=True)
	email = Column(String(120), unique=True, nullable=False)
	password_hash = Column(String(128))
	profile_picture = Column(String(120))
	status_message = Column(String(120))
	privacy_settings = Column(String(120))
	last_seen = Column(DateTime, default=datetime.utcnow)
	# Relationship with blocked contacts
	blocked_contacts = relationship('User', 
									secondary=blocked_contacts, 
									primaryjoin=id==blocked_contacts.c.blocking_user_id,
									secondaryjoin=id==blocked_contacts.c.blocked_user_id,
									backref=db.backref('blocking_users', lazy='dynamic'), 
									lazy='dynamic')

	def __init__(self, email, password):
		# Initialize user with email and hashed password
		self.email = email
		self.password_hash = generate_password_hash(password)

	def set_password(self, password):
		# Set hashed password
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		# Check if hashed password matches
		return check_password_hash(self.password_hash, password)

	def block_contact(self, contact):
		# Add contact to blocked contacts
		if contact not in self.blocked_contacts:
			self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		# Remove contact from blocked contacts
		if contact in self.blocked_contacts:
			self.blocked_contacts.remove(contact)

class Message(db.Model):
	# Message model
	id = Column(Integer, primary_key=True)
	sender_id = Column(Integer, ForeignKey('user.id'))
	recipient_id = Column(Integer, ForeignKey('user.id'))
	content = Column(String(120))
	timestamp = Column(DateTime, index=True, default=datetime.utcnow)
	read_receipt = Column(Boolean, default=False)
	encryption_key = Column(String(120))

	def __init__(self, sender, recipient, content, read_receipt, encryption_key):
		# Initialize message with sender, recipient, content, read receipt status, and encryption key
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.read_receipt = read_receipt
		self.encryption_key = encryption_key

	def encrypt_content(self):
		# Encrypt message content
		cipher_suite = Fernet(self.encryption_key)
		self.content = cipher_suite.encrypt(self.content.encode()).decode()

	def decrypt_content(self):
		# Decrypt message content
		cipher_suite = Fernet(self.encryption_key)
		self.content = cipher_suite.decrypt(self.content.encode()).decode()

class Group(db.Model):
	# Group model
	id = Column(Integer, primary_key=True)
	name = Column(String(120))
	picture = Column(String(120))
	# Relationships with admins and participants
	admins = relationship('User', secondary=group_admins, backref='admin_groups')
	participants = relationship('User', secondary=group_participants, backref='participant_groups')

	def __init__(self, name):
		# Initialize group with name
		self.name = name

	def add_participant(self, participant):
		# Add participant to group
		self.participants.append(participant)

	def remove_participant(self, participant):
		# Remove participant from group
		self.participants.remove(participant)

	def set_admin(self, participant):
		# Set participant as admin
		self.admins.append(participant)

	def remove_admin(self, participant):
		# Remove admin status from participant
		self.admins.remove(participant)

class Status(db.Model):
	# Status model
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	content = Column(String(120))
	timestamp = Column(DateTime, index=True, default=datetime.utcnow)
	visibility = Column(String(120))

	def __init__(self, user, content, visibility):
		# Initialize status with user, content, and visibility
		self.user = user
		self.content = content
		self.visibility = visibility

	def set_visibility(self, visibility):
		# Set status visibility
		self.visibility = visibility

