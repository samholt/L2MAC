from models.chat import Chat

class GroupChat(Chat):
	def __init__(self, users):
		super().__init__(users)

	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		if user in self.users:
			self.users.remove(user)
		else:
			return 'User not found in group chat'
