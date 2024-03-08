from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(280))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(280))
	sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Notification(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(280))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
