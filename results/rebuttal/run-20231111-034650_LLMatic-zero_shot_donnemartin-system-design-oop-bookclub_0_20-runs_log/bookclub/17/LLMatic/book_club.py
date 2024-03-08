class BookClub:
	def __init__(self):
		self.book_clubs = {}

	def create_book_club(self, club_id, club_name):
		if club_id in self.book_clubs:
			return 'Book club already exists'
		self.book_clubs[club_id] = {'club_name': club_name, 'members': []}
		return 'Book club created successfully'

	def get_book_club(self, club_id):
		if club_id not in self.book_clubs:
			return 'Book club does not exist'
		return self.book_clubs[club_id]

	def update_book_club(self, club_id, club_name):
		if club_id not in self.book_clubs:
			return 'Book club does not exist'
		self.book_clubs[club_id]['club_name'] = club_name
		return 'Book club updated successfully'

	def delete_book_club(self, club_id):
		if club_id not in self.book_clubs:
			return 'Book club does not exist'
		self.book_clubs.pop(club_id)
		return 'Book club deleted successfully'
