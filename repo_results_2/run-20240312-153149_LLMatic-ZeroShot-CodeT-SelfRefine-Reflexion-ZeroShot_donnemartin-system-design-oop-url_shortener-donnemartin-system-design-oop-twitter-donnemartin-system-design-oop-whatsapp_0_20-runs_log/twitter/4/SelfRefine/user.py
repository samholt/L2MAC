from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

@dataclass
class User(db.Model):
	email: str = db.Column(db.String, primary_key=True)
	username: str = db.Column(db.String)
	_password: str = db.Column(db.String)
	bio: str = db.Column(db.String)
	website: str = db.Column(db.String)
	location: str = db.Column(db.String)
	private: bool = db.Column(db.Boolean)

	def set_password(self, password):
		self._password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self._password, password)

	def to_dict(self):
		return {
			'email': self.email,
			'username': self.username,
			'bio': self.bio,
			'website': self.website,
			'location': self.location,
			'private': self.private
		}
