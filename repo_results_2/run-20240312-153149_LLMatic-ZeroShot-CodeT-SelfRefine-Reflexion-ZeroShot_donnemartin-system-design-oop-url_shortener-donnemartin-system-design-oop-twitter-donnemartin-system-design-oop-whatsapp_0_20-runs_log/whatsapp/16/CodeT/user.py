import uuid

class User:
	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = {'last_seen': 'everyone', 'profile_picture': 'everyone', 'status_message': 'everyone'}
		self.blocked_users = set()
		self.groups = set()

	def block_user(self, user_id):
		self.blocked_users.add(user_id)

	def unblock_user(self, user_id):
		self.blocked_users.remove(user_id)

	def create_group(self, group_id):
		self.groups.add(group_id)

	def leave_group(self, group_id):
		self.groups.remove(group_id)
