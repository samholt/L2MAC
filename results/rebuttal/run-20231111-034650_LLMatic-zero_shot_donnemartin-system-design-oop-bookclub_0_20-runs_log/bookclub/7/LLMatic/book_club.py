class BookClub:
	def __init__(self):
		self.clubs = {}

	def create_club(self, club_name, is_private):
		if club_name in self.clubs:
			return 'Club already exists'
		self.clubs[club_name] = {'is_private': is_private, 'members': []}
		return 'Club created successfully'

	def set_privacy(self, club_name, is_private):
		if club_name not in self.clubs:
			return 'Club does not exist'
		self.clubs[club_name]['is_private'] = is_private
		return 'Club privacy updated successfully'

	def join_club(self, club_name, user_name):
		if club_name not in self.clubs:
			return 'Club does not exist'
		if self.clubs[club_name]['is_private']:
			return 'Cannot join private club'
		self.clubs[club_name]['members'].append(user_name)
		return 'Joined club successfully'

	def manage_member(self, club_name, user_name, action):
		if club_name not in self.clubs:
			return 'Club does not exist'
		if action == 'add':
			self.clubs[club_name]['members'].append(user_name)
		elif action == 'remove':
			self.clubs[club_name]['members'].remove(user_name)
		return 'Member managed successfully'
