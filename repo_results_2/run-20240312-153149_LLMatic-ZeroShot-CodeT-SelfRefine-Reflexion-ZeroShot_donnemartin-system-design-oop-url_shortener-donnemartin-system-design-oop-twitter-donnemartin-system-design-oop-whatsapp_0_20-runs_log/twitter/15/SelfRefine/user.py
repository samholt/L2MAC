from dataclasses import dataclass
from database import db

@dataclass
class User(db.Model):
	email: str = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
	username: str = db.Column(db.String(80), unique=True, nullable=False)
	password: str = db.Column(db.String(80), nullable=False)
	profile_picture: str = db.Column(db.String(120), nullable=True)
	bio: str = db.Column(db.String(120), nullable=True)
	website_link: str = db.Column(db.String(120), nullable=True)
	location: str = db.Column(db.String(120), nullable=True)
	is_private: bool = db.Column(db.Boolean, default=False)

	def to_dict(self):
		return {'email': self.email, 'username': self.username, 'password': self.password, 'profile_picture': self.profile_picture, 'bio': self.bio, 'website_link': self.website_link, 'location': self.location, 'is_private': self.is_private}
