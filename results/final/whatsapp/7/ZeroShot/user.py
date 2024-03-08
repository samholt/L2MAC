import uuid

class User:
	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = {'last_seen': 'everyone', 'profile_picture': 'everyone', 'status_message': 'everyone'}
		self.blocked_contacts = []
		self.groups = []

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'privacy_settings': self.privacy_settings,
			'blocked_contacts': [user.id for user in self.blocked_contacts],
			'groups': [group.id for group in self.groups]
		}
