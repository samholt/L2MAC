from models.user import User
from models.book_club import BookClub
from models.meeting import Meeting
from models.discussion import Discussion
from models.book import Book
from models.notification import Notification

users = {}
book_clubs = {}
meetings = {}
discussions = {}
books = {}
notifications = {}

class AdminDashboard:
	def __init__(self):
		pass

	def manage_users(self, action, user_id=None, name=None, email=None, password=None):
		if action == 'view':
			return users
		elif action == 'delete':
			if user_id in users:
				del users[user_id]
				return 'User deleted successfully'
		elif action == 'create':
			user = User.create(name, email, password)
			users[user.id] = user
			return 'User created successfully'

	def manage_book_clubs(self, action, club_id=None, name=None, description=None, privacy=None):
		if action == 'view':
			return book_clubs
		elif action == 'delete':
			if club_id in book_clubs:
				del book_clubs[club_id]
				return 'Book club deleted successfully'
		elif action == 'create':
			club = BookClub(None, name, description, privacy, [], None)
			book_clubs[club.id] = club
			return 'Book club created successfully'

	def view_analytics(self):
		user_engagement = len(users)
		book_club_engagement = len(book_clubs)
		popular_books = sorted(books.values(), key=lambda x: len(x.readers), reverse=True)
		return {'user_engagement': user_engagement, 'book_club_engagement': book_club_engagement, 'popular_books': popular_books}
