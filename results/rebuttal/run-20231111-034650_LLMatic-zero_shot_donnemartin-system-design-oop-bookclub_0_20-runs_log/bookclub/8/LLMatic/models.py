class User:
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
		self.read_books = []
		self.wish_list = []
		self.followed_users = []
		self.notifications = []


class BookClub:
	def __init__(self, name, description, is_private, admin):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = []
		self.admin = admin
		self.meetings = []
		self.discussions = []


class Meeting:
	def __init__(self, date, time, book, book_club):
		self.date = date
		self.time = time
		self.book = book
		self.book_club = book_club


class Discussion:
	def __init__(self, topic, book_club):
		self.topic = topic
		self.book_club = book_club


class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author


class Vote:
	def __init__(self, user, book):
		self.user = user
		self.book = book


class Notification:
	def __init__(self, user, message):
		self.user = user
		self.message = message


class Resource:
	def __init__(self, url, description):
		self.url = url
		self.description = description
