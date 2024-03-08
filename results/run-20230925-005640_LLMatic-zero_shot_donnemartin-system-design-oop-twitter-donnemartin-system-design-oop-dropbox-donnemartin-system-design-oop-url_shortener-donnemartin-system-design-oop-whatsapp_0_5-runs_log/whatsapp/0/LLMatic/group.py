class Group:
	def __init__(self, name, picture):
		self.name = name
		self.picture = picture
		self.participants = []
		self.admins = []

	def add_participant(self, user):
		if user not in self.participants:
			self.participants.append(user)

	def remove_participant(self, user):
		if user in self.participants:
			self.participants.remove(user)

	def promote_to_admin(self, user):
		if user in self.participants and user not in self.admins:
			self.admins.append(user)

	def demote_from_admin(self, user):
		if user in self.admins:
			self.admins.remove(user)
