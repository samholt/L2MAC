class User:
	def __init__(self, id, username, email, password):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.profile = None
		self.bookclubs = []
		self.following = []
		self.followers = []
		self.reading_list = []
		self.recommendations = []

	def set_profile(self, profile):
		self.profile = profile

	def join_bookclub(self, bookclub):
		self.bookclubs.append(bookclub)

	def follow(self, user):
		self.following.append(user)
		user.followers.append(self)

	def add_to_reading_list(self, book):
		self.reading_list.append(book)

	def add_recommendation(self, book):
		self.recommendations.append(book)


class Profile:
	def __init__(self, id, bio, location):
		self.id = id
		self.bio = bio
		self.location = location


class BookClub:
	def __init__(self, id, name, description, privacy):
		self.id = id
		self.name = name
		self.description = description
		self.privacy = privacy
		self.members = []
		self.meetings = []
		self.discussions = []
		self.votes = []

	def add_member(self, user):
		self.members.append(user)

	def schedule_meeting(self, meeting):
		self.meetings.append(meeting)

	def start_discussion(self, discussion):
		self.discussions.append(discussion)

	def add_vote(self, vote):
		self.votes.append(vote)


class Meeting:
	def __init__(self, id, date, time, location, bookclub):
		self.id = id
		self.date = date
		self.time = time
		self.location = location
		self.bookclub = bookclub


class Discussion:
	def __init__(self, id, title, content, bookclub):
		self.id = id
		self.title = title
		self.content = content
		self.bookclub = bookclub
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)


class Comment:
	def __init__(self, id, content, user_id, discussion):
		self.id = id
		self.content = content
		self.user_id = user_id
		self.discussion = discussion


class Vote:
	def __init__(self, id, book_name, user_id, bookclub):
		self.id = id
		self.book_name = book_name
		self.user_id = user_id
		self.bookclub = bookclub

