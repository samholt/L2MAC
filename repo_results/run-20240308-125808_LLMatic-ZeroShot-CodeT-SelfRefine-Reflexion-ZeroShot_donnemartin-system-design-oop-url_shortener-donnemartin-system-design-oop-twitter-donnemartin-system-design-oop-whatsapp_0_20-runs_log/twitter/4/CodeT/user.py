from dataclasses import dataclass, field
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User:
	email: str
	username: str
	password: str
	bio: str = field(default='')
	website: str = field(default='')
	location: str = field(default='')
	private: bool = field(default=False)

	def __post_init__(self):
		self.password = generate_password_hash(self.password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def to_dict(self):
		return {'email': self.email, 'username': self.username, 'bio': self.bio, 'website': self.website, 'location': self.location, 'private': self.private}
