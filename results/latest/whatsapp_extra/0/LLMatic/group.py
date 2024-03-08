from user import User


class Group:
	def __init__(self, name: str, picture: str, admins: list):
		self.name = name
		self.picture = picture
		self.participants = admins
		self.admins = admins

	def add_participant(self, user: User):
		if user not in self.participants:
			self.participants.append(user)

	def remove_participant(self, user: User):
		if user in self.participants:
			self.participants.remove(user)

	def promote_to_admin(self, user: User):
		if user in self.participants and user not in self.admins:
			self.admins.append(user)

	def demote_from_admin(self, user: User):
		if user in self.admins:
			self.admins.remove(user)
