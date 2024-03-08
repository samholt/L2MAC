class GroupChat:
	def __init__(self, name, picture=None, participants=None, admins=None):
		self.name = name
		self.picture = picture
		self.participants = participants if participants else []
		self.admins = admins if admins else []

	def create_group_chat(self, name, picture, participants, admins):
		self.name = name
		self.picture = picture
		self.participants = participants
		self.admins = admins

	def add_participant(self, participant):
		self.participants.append(participant)

	def remove_participant(self, participant):
		self.participants.remove(participant)

	def manage_admin_roles(self, admin):
		if admin in self.admins:
			self.admins.remove(admin)
		else:
			self.admins.append(admin)
