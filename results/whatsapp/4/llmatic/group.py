class Group:
	def __init__(self, name, picture, admin):
		self.name = name
		self.picture = picture
		self.admin = admin
		self.participants = []

	def add_participant(self, participant):
		if participant not in self.participants:
			self.participants.append(participant)

	def remove_participant(self, participant):
		if participant in self.participants:
			self.participants.remove(participant)

	def manage_admin_roles(self, user, admin_status):
		if user in self.participants:
			user.admin = admin_status
