class User:
	def __init__(self, username, email, password_hash, first_name='', last_name='', bio='', profile_picture='', role='member'):
		self.username = username
		self.email = email
		self.password_hash = password_hash
		self.first_name = first_name
		self.last_name = last_name
		self.bio = bio
		self.profile_picture = profile_picture
		self.role = role

class BookClub:
	def __init__(self, name, description, privacy='public'):
		self.name = name
		self.description = description
		self.privacy = privacy
		self.members = []
		self.meetings = []
		self.discussions = []

	def add_member(self, user):
		self.members.append(user)

	def schedule_meeting(self, meeting):
		self.meetings.append(meeting)

	def start_discussion(self, discussion):
		self.discussions.append(discussion)

	def set_privacy(self, privacy):
		self.privacy = privacy

class Meeting:
	def __init__(self, date, time):
		self.date = date
		self.time = time

	def set_reminder(self, reminder):
		self.reminder = reminder

class Discussion:
	def __init__(self, topic):
		self.topic = topic
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)

class Comment:
	def __init__(self, user, text):
		self.user = user
		self.text = text
		self.votes = 0

	def upvote(self):
		self.votes += 1

	def downvote(self):
		self.votes -= 1

class Vote:
	def __init__(self, user, comment, vote_type):
		self.user = user
		self.comment = comment
		self.vote_type = vote_type
