from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

@dataclass
class User(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	email: str = db.Column(db.String, unique=True, nullable=False)
	password: str = db.Column(db.String, nullable=False)

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password

	def to_dict(self):
		return {'id': self.id, 'email': self.email}
