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
	is_private: bool = db.Column(db.Boolean)

	def to_dict(self):
		return self.__dict__
