from user import User


class Group:
	def __init__(self, name, picture=None):
		self.name = name
		self.picture = picture
		self.participants = []
		self.admins = []

	def add_participant(self, user: User):
		self.participants.append(user)

	def remove_participant(self, user: User):
		self.participants.remove(user)

	def promote_to_admin(self, user: User):
		if user in self.participants:
			self.admins.append(user)

	def demote_from_admin(self, user: User):
		if user in self.admins:
			self.admins.remove(user)

	def edit_group_name(self, name):
		self.name = name

	def edit_group_picture(self, picture):
		self.picture = picture
