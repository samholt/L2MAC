from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	status_message = db.Column(db.String(120), nullable=True)
	last_seen = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	privacy_settings = db.Column(db.String(20), nullable=False, default='public')
	
	def set_password(self, password):
		self.password = pbkdf2_sha256.hash(password)
	
	def check_password(self, password):
		return pbkdf2_sha256.verify(password, self.password)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	read_receipt = db.Column(db.Boolean, default=False)
	
	def __repr__(self):
		return f'Message('{self.content}', '{self.date_posted}')'

class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f'Group('{self.name}', '{self.image_file}')'

class GroupMember(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
	member_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f'GroupMember('{self.group_id}', '{self.member_id}')'

class Status(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	image_file = db.Column(db.String(20), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f'Status('{self.image_file}', '{self.date_posted}')'
