class Group:
	def __init__(self, name, picture, admin):
		self.name = name
		self.picture = picture
		self.admins = [admin]
		self.participants = [admin]

	def add_participant(self, user):
		if user not in self.participants:
			self.participants.append(user)

	def remove_participant(self, user):
		if user in self.participants and user not in self.admins:
			self.participants.remove(user)

	def add_admin(self, user):
		if user in self.participants and user not in self.admins:
			self.admins.append(user)

	def remove_admin(self, user):
		if user in self.admins and len(self.admins) > 1:
			self.admins.remove(user)
