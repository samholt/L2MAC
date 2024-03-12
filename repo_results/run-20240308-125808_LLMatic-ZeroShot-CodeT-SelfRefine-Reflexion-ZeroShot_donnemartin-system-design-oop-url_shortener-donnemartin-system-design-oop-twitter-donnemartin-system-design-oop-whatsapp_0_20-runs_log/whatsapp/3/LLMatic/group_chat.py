class GroupChat:
	def __init__(self, group_id, admin):
		self.group_id = group_id
		self.admin = admin
		self.participants = {admin: 'admin'}

	def add_participant(self, participant):
		self.participants[participant] = 'participant'

	def remove_participant(self, participant):
		if participant in self.participants and self.participants[participant] != 'admin':
			del self.participants[participant]

	def set_admin(self, participant):
		if participant in self.participants:
			self.participants[participant] = 'admin'

	def remove_admin(self, participant):
		if participant in self.participants and self.participants[participant] == 'admin' and participant != self.admin:
			self.participants[participant] = 'participant'
