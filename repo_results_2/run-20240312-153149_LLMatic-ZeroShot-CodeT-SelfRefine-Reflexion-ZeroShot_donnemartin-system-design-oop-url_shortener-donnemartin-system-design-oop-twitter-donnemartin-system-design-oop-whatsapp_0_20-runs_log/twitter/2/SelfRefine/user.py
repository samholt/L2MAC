from dataclasses import dataclass
from db import db

@dataclass
class User(db.Model):
	email: str = db.Column(db.String, primary_key=True)
	username: str = db.Column(db.String)
	password: str = db.Column(db.String)
	profile_picture: str = db.Column(db.String)
	bio: str = db.Column(db.String)
	website_link: str = db.Column(db.String)
	location: str = db.Column(db.String)

	def to_dict(self):
		return {
			'email': self.email,
			'username': self.username,
			'password': self.password,
			'profile_picture': self.profile_picture,
			'bio': self.bio,
			'website_link': self.website_link,
			'location': self.location
		}
