from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
	email = db.Column(db.String(120), unique=True, nullable=False)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	bio = db.Column(db.String(500), nullable=True)
	website = db.Column(db.String(120), nullable=True)
	location = db.Column(db.String(120), nullable=True)
	private = db.Column(db.Boolean, default=False)

	def __init__(self, **kwargs):
		self.password = generate_password_hash(kwargs.get('password'))
		super().__init__(**kwargs)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def to_dict(self):
		return {key: value for key, value in self.__dict__.items() if key != 'password'}
