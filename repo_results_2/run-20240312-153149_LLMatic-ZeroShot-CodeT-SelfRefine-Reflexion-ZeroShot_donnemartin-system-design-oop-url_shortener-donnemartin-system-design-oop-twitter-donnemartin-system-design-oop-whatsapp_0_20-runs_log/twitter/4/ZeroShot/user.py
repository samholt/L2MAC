from dataclasses import dataclass, field
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = field(default=None)
	bio: str = field(default=None)
	website_link: str = field(default=None)
	location: str = field(default=None)
	private: bool = field(default=False)

	def __post_init__(self):
		self.password = generate_password_hash(self.password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def update_profile(self, profile_picture=None, bio=None, website_link=None, location=None, private=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location
		if private is not None:
			self.private = private

	def to_dict(self):
		return {f.name: getattr(self, f.name) for f in fields(self)}
