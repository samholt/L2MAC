class Group:
	def __init__(self, name, admin):
		self.name = name
		self.admin = admin
		self.participants = [admin]
		self.admin_permissions = {admin: ['add', 'remove', 'set_admin', 'remove_admin']}

	def add_participant(self, participant):
		if participant not in self.participants:
			self.participants.append(participant)

	def remove_participant(self, participant):
		if participant in self.participants:
			self.participants.remove(participant)

	def set_admin(self, participant):
		if participant in self.participants and participant not in self.admin_permissions:
			self.admin_permissions[participant] = ['add', 'remove', 'set_admin', 'remove_admin']

	def remove_admin(self, participant):
		if participant in self.admin_permissions and len(self.admin_permissions) > 1:
			del self.admin_permissions[participant]
