class BookClub:
	def __init__(self):
		self.clubs = {}

	def create_club(self, club_name, privacy_setting):
		if club_name in self.clubs:
			return 'Club already exists'
		self.clubs[club_name] = {'members': [], 'privacy': privacy_setting, 'roles': {}}
		return 'Club created successfully'

	def join_club(self, club_name, user_name):
		if club_name not in self.clubs:
			return 'Club does not exist'
		if user_name in self.clubs[club_name]['members']:
			return 'User already a member'
		self.clubs[club_name]['members'].append(user_name)
		return 'User added successfully'

	def set_privacy(self, club_name, privacy_setting):
		if club_name not in self.clubs:
			return 'Club does not exist'
		self.clubs[club_name]['privacy'] = privacy_setting
		return 'Privacy setting updated'

	def manage_roles(self, club_name, user_name, role):
		if club_name not in self.clubs:
			return 'Club does not exist'
		if user_name not in self.clubs[club_name]['members']:
			return 'User not a member'
		self.clubs[club_name]['roles'][user_name] = role
		return 'Role updated'
