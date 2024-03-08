class Group:
	def __init__(self, name, picture, creator):
		self.name = name
		self.picture = picture
		self.participants = {creator}
		self.admins = {creator}

	def create_group(self, name, picture, creator):
		self.name = name
		self.picture = picture
		self.participants.add(creator)
		self.admins.add(creator)

	def manage_group(self, user, action, participant):
		if user not in self.admins:
			return "Only admins can manage the group."
		if action == "add":
			self.participants.add(participant)
		elif action == "remove":
			if participant in self.participants:
				self.participants.remove(participant)
		return "Group managed successfully."

	def administer_group(self, user, action, admin):
		if user not in self.admins:
			return "Only admins can administer the group."
		if action == "add":
			self.admins.add(admin)
		elif action == "remove":
			if admin in self.admins and admin != user:
				self.admins.remove(admin)
			else:
				return "Admins cannot remove themselves."
		return "Group administered successfully."
