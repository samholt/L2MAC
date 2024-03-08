from user import User
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion


class Admin:
	def __init__(self):
		self.users = {}
		self.book_clubs = {}
		self.meetings = {}
		self.discussions = {}

	def create_user(self, username):
		self.users[username] = User(username)

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]

	def create_book_club(self):
		self.book_clubs = BookClub()

	def create_meeting(self):
		self.meetings = Meeting()

	def create_discussion(self):
		self.discussions = Discussion()

	def generate_analytics(self):
		return {
			'users': len(self.users),
			'book_clubs': len(self.book_clubs.clubs),
			'meetings': sum([len(meetings) for meetings in self.meetings.meetings.values()]),
			'discussions': len(self.discussions.forums)
		}
