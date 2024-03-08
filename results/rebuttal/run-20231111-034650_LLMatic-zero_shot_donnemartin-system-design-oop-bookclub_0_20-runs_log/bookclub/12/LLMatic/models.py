class User:
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
		self.books_read = []
		self.interests = []
		self.followed_users = []
		self.notifications = []


class BookClub:
	def __init__(self, name, description, is_private):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = []
		self.current_book = None
		self.meetings = []
		self.discussion_forums = []

	def add_member(self, user):
		self.members.append(user)


class Meeting:
	def __init__(self, date, time, attendees, book_club):
		self.date = date
		self.time = time
		self.attendees = attendees
		self.book_club = book_club

	def to_ical(self):
		return f'BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\nDTSTART:{self.date.replace("-", "")}T{self.time.replace(":", "")}00\nSUMMARY:Meeting of {self.book_club.name}\nEND:VEVENT\nEND:VCALENDAR'


class DiscussionForum:
	def __init__(self, topic, book_club):
		self.topic = topic
		self.book_club = book_club
		self.posts = []


class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.votes = 0


class Notification:
	def __init__(self, message, user):
		self.message = message
		self.user = user
		self.read = False

class Resource:
	def __init__(self, title, content, user):
		self.title = title
		self.content = content
		self.user = user
