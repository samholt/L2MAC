class MockDatabase:
	def __init__(self):
		self.users = {}
		self.book_clubs = {}
		self.meetings = {}
		self.discussions = {}
		self.admins = {}

	def add_user(self, user):
		self.users[user.username] = user

	def get_user(self, username):
		return self.users.get(username)

	def add_book_club(self, book_club):
		self.book_clubs[book_club.name] = book_club

	def get_book_club(self, book_club_name):
		return self.book_clubs.get(book_club_name)

	def add_meeting(self, meeting):
		self.meetings[meeting.date] = meeting

	def get_meeting(self, meeting_date):
		return self.meetings.get(meeting_date)

	def add_discussion(self, discussion):
		self.discussions[discussion.topic] = discussion

	def get_discussion(self, discussion_topic):
		return self.discussions.get(discussion_topic)

	def add_admin(self, admin):
		self.admins[admin] = admin

	def get_admin(self, admin):
		return self.admins.get(admin)
