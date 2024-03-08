class BookClub:
	def __init__(self):
		self.clubs = {}
		self.votes = []

	def create_club(self, name, description, privacy):
		if name in self.clubs:
			return 'Club already exists'
		self.clubs[name] = {'description': description, 'privacy': privacy, 'members': []}
		return 'Club created successfully'

	def join_club(self, name, user):
		if name not in self.clubs:
			return 'Club does not exist'
		if user in self.clubs[name]['members']:
			return 'User already a member'
		self.clubs[name]['members'].append(user)
		return 'User added successfully'

	def manage_request(self, name, user, action):
		if name not in self.clubs:
			return 'Club does not exist'
		if user not in self.clubs[name]['members']:
			return 'User not a member'
		if action == 'remove':
			self.clubs[name]['members'].remove(user)
			return 'User removed successfully'
		return 'Invalid action'
