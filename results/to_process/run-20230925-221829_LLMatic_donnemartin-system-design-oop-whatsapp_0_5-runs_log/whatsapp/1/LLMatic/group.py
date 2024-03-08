class Group:
	def __init__(self, name, picture, admin):
		self.name = name
		self.picture = picture
		self.admin = admin
		self.participants = {admin}

	def add_participant(self, user):
		self.participants.add(user)

	def remove_participant(self, user):
		if user in self.participants:
			self.participants.remove(user)

	def set_admin(self, user):
		if user in self.participants:
			self.admin = user

mock_db = {}

def create_group(name, picture, admin):
	if name in mock_db:
		return 'Group already exists'
	else:
		mock_db[name] = Group(name, picture, admin)
		return 'Group created successfully'

