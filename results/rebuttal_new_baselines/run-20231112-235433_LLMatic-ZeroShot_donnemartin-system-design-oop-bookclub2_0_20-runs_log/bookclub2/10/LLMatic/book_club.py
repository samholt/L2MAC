class BookClub:
	def __init__(self, id=None, name=None, creator=None, members=None, privacy='public'):
		self.id = id
		self.name = name
		self.creator = creator
		self.members = members if members else []
		self.privacy = privacy

	def create_club(self, id, name, creator):
		self.id = id
		self.name = name
		self.creator = creator
		self.members = [creator]
		self.privacy = 'public'

	def add_member(self, user):
		self.members.append(user)

	def remove_member(self, user):
		if user in self.members:
			self.members.remove(user)

	def change_privacy(self, privacy):
		self.privacy = privacy
