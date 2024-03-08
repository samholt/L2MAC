class Admin:
	def __init__(self, database, user, profile, book_club, membership, meeting, reminder, discussion, comment, book, vote, recommendation):
		self.database = database
		self.user = user
		self.profile = profile
		self.book_club = book_club
		self.membership = membership
		self.meeting = meeting
		self.reminder = reminder
		self.discussion = discussion
		self.comment = comment
		self.book = book
		self.vote = vote
		self.recommendation = recommendation

	def manage_user(self, id, action, user_data=None):
		if action == 'create':
			self.user.create_user(id, user_data)
		elif action == 'get':
			return self.user.get_user(id)
		elif action == 'update':
			self.user.update_user(id, user_data)
		elif action == 'delete':
			self.user.delete_user(id)

	def manage_book_club(self, club_id, action, club_name=None):
		if action == 'create':
			self.book_club.create_book_club(club_id, club_name)
		elif action == 'get':
			return self.book_club.get_book_club(club_id)
		elif action == 'update':
			self.book_club.update_book_club(club_id, club_name)
		elif action == 'delete':
			self.book_club.delete_book_club(club_id)

	def remove_inappropriate_content(self, content_type, id):
		if content_type == 'discussion':
			self.discussion.delete_discussion(id)
		elif content_type == 'comment':
			self.comment.delete_comment(id)

	def generate_analytics(self):
		user_engagement = len(self.database.users)
		popular_books = self.recommendation.get_popular_books()
		return {'user_engagement': user_engagement, 'popular_books': popular_books}
