class BookClub:
	clubs = {}

	def __init__(self, name, privacy='public'):
		if not name or not privacy:
			raise ValueError('Missing required parameters')
		self.name = name
		self.privacy = privacy
		self.members = {}

	def create_club(self, admin):
		if not admin:
			raise ValueError('Missing required parameters')
		self.members[admin] = 'admin'
		self.__class__.clubs[self.name] = self

	def join_club(self, user):
		if not user:
			raise ValueError('Missing required parameters')
		if self.privacy == 'public' or user in self.members:
			self.members[user] = 'member'

	def set_privacy(self, privacy):
		if not privacy:
			raise ValueError('Missing required parameters')
		self.privacy = privacy

	def manage_roles(self, admin, user, role):
		if not admin or not user or not role:
			raise ValueError('Missing required parameters')
		if self.members.get(admin) == 'admin':
			self.members[user] = role
