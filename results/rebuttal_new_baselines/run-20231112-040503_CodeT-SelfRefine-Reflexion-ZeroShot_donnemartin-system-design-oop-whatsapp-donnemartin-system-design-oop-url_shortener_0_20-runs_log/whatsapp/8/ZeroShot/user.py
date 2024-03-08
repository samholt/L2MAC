from dataclasses import dataclass, field
import uuid

@dataclass
class User:
	id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = field(default_factory=dict)
	blocked_contacts: list = field(default_factory=list)
	
	def to_dict(self):
		return {'id': self.id, 'email': self.email, 'profile_picture': self.profile_picture, 'status_message': self.status_message, 'privacy_settings': self.privacy_settings, 'blocked_contacts': self.blocked_contacts}
