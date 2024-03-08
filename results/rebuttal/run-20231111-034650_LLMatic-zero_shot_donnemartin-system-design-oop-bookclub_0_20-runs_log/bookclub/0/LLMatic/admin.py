from user import User
from book_club import BookClub
from mock_db import MockDB


class Admin(User):
	def __init__(self, name, email, password, reading_interests=[], books_read=[], books_to_read=[]):
		super().__init__(name, email, password, reading_interests, books_read, books_to_read)
		self.db = MockDB()

	def manage_user_account(self, user_email, action):
		if action == 'delete':
			self.db.delete(self.db.users, user_email)
		elif action == 'suspend':
			user = self.db.get(self.db.users, user_email)
			if user:
				user.is_suspended = True
				self.db.update(self.db.users, user_email, user)

	def manage_book_club(self, book_club_name, action):
		if action == 'delete':
			self.db.delete(self.db.book_clubs, book_club_name)
		elif action == 'suspend':
			book_club = self.db.get(self.db.book_clubs, book_club_name)
			if book_club:
				book_club.is_suspended = True
				self.db.update(self.db.book_clubs, book_club_name, book_club)

	def remove_inappropriate_content(self, content_id):
		self.db.delete(self.db.discussions, content_id)

	def view_user_engagement(self):
		# For simplicity, we'll just count the number of users and book clubs
		return len(self.db.users), len(self.db.book_clubs)

	def view_popular_books(self):
		# For simplicity, we'll just return the books with the most reviews
		return sorted(self.db.books.values(), key=lambda book: len(book.reviews), reverse=True)
