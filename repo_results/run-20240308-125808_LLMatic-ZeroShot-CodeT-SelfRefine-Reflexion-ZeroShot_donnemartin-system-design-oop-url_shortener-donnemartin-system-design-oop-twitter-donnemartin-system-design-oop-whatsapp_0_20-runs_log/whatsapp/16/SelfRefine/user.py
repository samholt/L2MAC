from dataclasses import dataclass
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

@dataclass
class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	password_hash = db.Column(db.String, nullable=False)

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def to_dict(self):
		return {'id': self.id, 'email': self.email}
