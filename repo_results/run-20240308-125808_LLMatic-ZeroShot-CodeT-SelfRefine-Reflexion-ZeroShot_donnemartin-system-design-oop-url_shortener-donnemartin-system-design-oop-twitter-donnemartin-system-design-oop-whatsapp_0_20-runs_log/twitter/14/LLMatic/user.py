import hashlib
import binascii
import os


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = self.hash_password(password)
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = set()
		self.followers = set()
		self.notifications = []

	def hash_password(self, password):
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		pwdhash = binascii.hexlify(pwdhash)
		return (salt + pwdhash).decode('ascii')

	def verify_password(self, provided_password):
		salt = self.password[:64]
		stored_password = self.password[64:]
		pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')
		return pwdhash == stored_password

	def reset_password(self, new_password):
		self.password = self.hash_password(new_password)

	def update_profile_picture(self, new_picture):
		self.profile_picture = new_picture

	def update_bio(self, new_bio):
		self.bio = new_bio

	def update_website_link(self, new_website_link):
		self.website_link = new_website_link

	def update_location(self, new_location):
		self.location = new_location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user.username not in self.following:
			self.following.add(user.username)
			user.followers.add(self.username)
			user.notifications.append(f'{self.username} started following you.')

	def unfollow(self, user):
		if user.username in self.following:
			self.following.remove(user.username)
			user.followers.remove(self.username)

	def view_timeline(self):
		from post import Post
		timeline = []
		for username in self.following:
			user = mock_db[username]
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def view_notifications(self):
		return self.notifications

	def recommend_users(self):
		recommendations = []
		for user in mock_db.values():
			if user.username != self.username and user.username not in self.following:
				mutual_followers = self.followers.intersection(user.followers)
				if len(mutual_followers) > 0:
					recommendations.append(user.username)
		return recommendations

mock_db = {}

def register(email, username, password, is_private):
	if username in mock_db:
		return False
	else:
		mock_db[username] = User(email, username, password, is_private)
		return True


def authenticate(username, password):
	if username in mock_db and mock_db[username].verify_password(password):
		return True
	else:
		return False

