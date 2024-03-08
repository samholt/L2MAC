class User:
	def __init__(self, username, email, password, reading_interests, read_books, wish_to_read_books):
		self.username = username
		self.email = email
		self.password = password
		self.reading_interests = reading_interests
		self.read_books = read_books
		self.wish_to_read_books = wish_to_read_books
		self.following = []
		self.notifications = []

	def to_dict(self):
		return {
			'username': self.username,
			'email': self.email,
			'password': self.password,
			'reading_interests': self.reading_interests,
			'read_books': [book.title for book in self.read_books],
			'wish_to_read_books': [book.title for book in self.wish_to_read_books],
			'following': [user.username for user in self.following],
			'notifications': [notification.to_dict() for notification in self.notifications]
		}

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)

	def is_following(self, user):
		return user in self.following

	def recommend_books(self, books):
		# Recommend books based on user's reading interests and popular books
		recommendations = [book for book in books.values() if book.genre in self.reading_interests and book not in self.read_books]
		return recommendations

	def __str__(self):
		return self.username

class Book:
	def __init__(self, title, author, genre):
		self.title = title
		self.author = author
		self.genre = genre

	def __str__(self):
		return self.title

class Admin:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def manage_users(self, users):
		# Admin can view all users
		return [user.to_dict() for user in users.values()]

	def manage_books(self, books):
		# Admin can view all books
		return [book.__dict__ for book in books.values()]

	def remove_user(self, users, username):
		# Admin can remove a user
		if username in users:
			del users[username]
			return 'User removed successfully'
		else:
			return 'User not found'

	def remove_book(self, books, title):
		# Admin can remove a book
		if title in books:
			del books[title]
			return 'Book removed successfully'
		else:
			return 'Book not found'

	def view_analytics(self, users):
		# Admin can view analytics on user engagement and popular books
		user_engagement = {user.username: len(user.read_books) for user in users.values()}
		popular_books = {}
		for user in users.values():
			for book in user.read_books:
				if book.title in popular_books:
					popular_books[book.title] += 1
				else:
					popular_books[book.title] = 1
		return {'user_engagement': user_engagement, 'popular_books': popular_books}

class Notification:
	def __init__(self, content, user, date):
		self.content = content
		self.user = user
		self.date = date

	def to_dict(self):
		return {
			'content': self.content,
			'user': self.user,
			'date': self.date
		}

class Resource:
	def __init__(self, title, content, author):
		self.title = title
		self.content = content
		self.author = author

	def to_dict(self):
		return {
			'title': self.title,
			'content': self.content,
			'author': self.author
		}
