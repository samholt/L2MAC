class GroupChat:
	def __init__(self, group_name, admin):
		self.group_name = group_name
		self.admin = admin
		self.participants = {admin: 'admin'}

	def add_participant(self, participant):
		if self.participants.get(participant) is None:
			self.participants[participant] = 'participant'

	def remove_participant(self, participant):
		if self.participants.get(participant) is not None:
			del self.participants[participant]

	def set_admin(self, participant):
		if self.participants.get(participant) is not None:
			self.participants[participant] = 'admin'

	def get_participants(self):
		return self.participants
