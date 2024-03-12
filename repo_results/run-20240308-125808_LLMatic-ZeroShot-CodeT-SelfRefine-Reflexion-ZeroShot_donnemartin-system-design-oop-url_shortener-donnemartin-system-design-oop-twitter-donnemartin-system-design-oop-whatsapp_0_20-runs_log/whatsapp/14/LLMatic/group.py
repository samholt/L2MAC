class Group:
	def __init__(self, group_name, admin):
		self.group_name = group_name
		self.admin = admin
		self.participants = {admin: 'admin'}
		self.group_chat = []

	def add_participant(self, participant):
		if participant not in self.participants:
			self.participants[participant] = 'participant'

	def remove_participant(self, participant):
		if participant in self.participants and self.participants[participant] != 'admin':
			del self.participants[participant]

	def assign_admin(self, participant):
		if participant in self.participants:
			self.participants[participant] = 'admin'

	def add_message(self, message):
		self.group_chat.append(message)
