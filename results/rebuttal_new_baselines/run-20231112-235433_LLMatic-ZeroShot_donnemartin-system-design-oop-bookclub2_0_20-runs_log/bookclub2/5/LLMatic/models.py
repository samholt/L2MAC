class User:
	def __init__(self, id, username, email, password):
		self.id = id
		self.username = username
		self.email = email
		self.password = password


class Profile:
	def __init__(self, id, user_id, bio, location):
		self.id = id
		self.user_id = user_id
		self.bio = bio
		self.location = location


class BookClub:
	def __init__(self, id, name, description, privacy_settings):
		self.id = id
		self.name = name
		self.description = description
		self.privacy_settings = privacy_settings


class Meeting:
	def __init__(self, id, bookclub_id, date, time, location):
		self.id = id
		self.bookclub_id = bookclub_id
		self.date = date
		self.time = time
		self.location = location

class Discussion:
	def __init__(self, id, bookclub_id, title, content):
		self.id = id
		self.bookclub_id = bookclub_id
		self.title = title
		self.content = content

class Comment:
	def __init__(self, id, discussion_id, user_id, content):
		self.id = id
		self.discussion_id = discussion_id
		self.user_id = user_id
		self.content = content

class Vote:
	def __init__(self, id, book_id, user_id):
		self.id = id
		self.book_id = book_id
		self.user_id = user_id

class Follow:
	def __init__(self, id, follower_id, followee_id):
		self.id = id
		self.follower_id = follower_id
		self.followee_id = followee_id

class ReadingList:
	def __init__(self, id, user_id, book_id):
		self.id = id
		self.user_id = user_id
		self.book_id = book_id

class Recommendation:
	def __init__(self, id, user_id, book_id):
		self.id = id
		self.user_id = user_id
		self.book_id = book_id

class Dashboard:
	def __init__(self, id, admin_id, content):
		self.id = id
		self.admin_id = admin_id
		self.content = content

class Moderation:
	def __init__(self, id, admin_id, action):
		self.id = id
		self.admin_id = admin_id
		self.action = action

class Analytics:
	def __init__(self, id, user_engagement, popular_books):
		self.id = id
		self.user_engagement = user_engagement
		self.popular_books = popular_books
