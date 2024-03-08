class Admin:
	def __init__(self):
		self.users = {}
		self.book_clubs = {}
		self.discussions = {}

	def manage_user(self, user_name, action):
		if action == 'remove':
			if user_name in self.users:
				del self.users[user_name]
				return 'User removed successfully'
			else:
				return 'User not found'
		elif action == 'suspend':
			if user_name in self.users:
				self.users[user_name].active = False
				return 'User suspended successfully'
			else:
				return 'User not found'

	def manage_book_club(self, book_club_name, action):
		if action == 'remove':
			if book_club_name in self.book_clubs:
				del self.book_clubs[book_club_name]
				return 'Book club removed successfully'
			else:
				return 'Book club not found'

	def remove_content(self, discussion_topic):
		if discussion_topic in self.discussions:
			del self.discussions[discussion_topic]
			return 'Discussion removed successfully'
		else:
			return 'Discussion not found'

	def generate_analytics(self):
		user_engagement = {user.name: len(user.followers) for user in self.users.values()}
		popular_books = {book_club_name: len(book_club.votes) for book_club_name, book_club in self.book_clubs.items()}
		return {'user_engagement': user_engagement, 'popular_books': popular_books}
