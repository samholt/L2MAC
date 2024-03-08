class Membership:
	def __init__(self, book_club):
		self.book_club = book_club

	def join_club(self, club_id, user_id):
		if club_id not in self.book_club.book_clubs:
			return 'Book club does not exist'
		if user_id in self.book_club.book_clubs[club_id]['members']:
			return 'User already a member'
		self.book_club.book_clubs[club_id]['members'].append(user_id)
		return 'User joined the club successfully'

	def leave_club(self, club_id, user_id):
		if club_id not in self.book_club.book_clubs:
			return 'Book club does not exist'
		if user_id not in self.book_club.book_clubs[club_id]['members']:
			return 'User not a member of the club'
		self.book_club.book_clubs[club_id]['members'].remove(user_id)
		return 'User left the club successfully'
