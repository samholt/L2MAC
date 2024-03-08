class GroupChat:
	def __init__(self, name, picture, participants, admin_roles):
		self.name = name
		self.picture = picture
		self.participants = participants
		self.admin_roles = admin_roles

	def add_participant(self, participant):
		self.participants.append(participant)

	def remove_participant(self, participant):
		self.participants.remove(participant)

	def set_admin_role(self, user, role):
		self.admin_roles[user] = role

	def remove_admin_role(self, user):
		del self.admin_roles[user]
