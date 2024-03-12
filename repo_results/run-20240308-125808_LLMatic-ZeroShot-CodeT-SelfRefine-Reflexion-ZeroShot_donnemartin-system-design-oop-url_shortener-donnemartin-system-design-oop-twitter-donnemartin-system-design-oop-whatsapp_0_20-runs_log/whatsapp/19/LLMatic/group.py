class Group:
	def __init__(self, name, picture):
		self.name = name
		self.picture = picture
		self.participants = []
		self.admins = []

	def create_group_chat(self, name, picture):
		self.name = name
		self.picture = picture

	def add_participant(self, participant):
		self.participants.append(participant)

	def remove_participant(self, participant):
		self.participants.remove(participant)

	def manage_admin_roles_and_permissions(self, admin, permissions):
		for i in range(len(self.admins)):
			if self.admins[i] == admin:
				self.admins[i] = (admin, permissions)
