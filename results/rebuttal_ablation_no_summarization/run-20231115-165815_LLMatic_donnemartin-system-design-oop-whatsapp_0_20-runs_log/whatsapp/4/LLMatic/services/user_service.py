class UserService:
	def __init__(self):
		self.users = {}

	def register(self, email, password):
		if email in self.users:
			return False
		self.users[email] = {'password': password, 'profile': {}, 'contacts': [], 'blocked': []}
		return True

	def authenticate(self, email, password):
		if email in self.users and self.users[email]['password'] == password:
			return True
		return False

	def set_profile(self, email, picture, status):
		if email in self.users:
			self.users[email]['profile'] = {'picture': picture, 'status': status}
			return True
		return False

	def set_privacy(self, email, privacy):
		if email in self.users:
			self.users[email]['privacy'] = privacy
			return True
		return False

	def block_contact(self, email, contact):
		if email in self.users and contact not in self.users[email]['blocked'] and contact in self.users:
			self.users[email]['blocked'].append(contact)
			return True
		return False

	def unblock_contact(self, email, contact):
		if email in self.users and contact in self.users[email]['blocked']:
			self.users[email]['blocked'].remove(contact)
			return True
		return False

	def get_user(self, email):
		if email in self.users:
			return self.users[email]
		return None
