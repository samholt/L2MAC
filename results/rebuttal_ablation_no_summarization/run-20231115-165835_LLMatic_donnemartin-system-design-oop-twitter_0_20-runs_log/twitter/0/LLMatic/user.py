import re
from collections import Counter
from post import Post

class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.posts = []
		self.notifications = []

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)

	def get_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return timeline

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location

	def notify(self, notification):
		self.notifications.append(notification)

	def recommend_users(self):
		# Find all users who have common hashtags with the given user
		common_hashtags_users = [user for user in users_db.values() if any(hashtag in post.text for post in user.posts for hashtag in re.findall(r'#\w+', post.text))]
		# Rank these users based on the number of posts they have and the number of mutual followers with the given user
		recommendations = sorted(common_hashtags_users, key=lambda user: (len(user.posts), len(set(self.following).intersection(user.following))), reverse=True)
		# Return the top 5 users as recommendations
		return recommendations[:5]

# Mock database
users_db = {}

def register(email, username, password, is_private):
	for user in users_db.values():
		if user.email == email or user.username == username:
			return 'User already exists'
	users_db[username] = User(email, username, password, is_private)
	return 'User registered successfully'

def authenticate(username, password):
	if username in users_db and users_db[username].password == password:
		return 'User authenticated'
	else:
		return 'Invalid credentials'

def reset_password(username, new_password):
	if username in users_db:
		users_db[username].password = new_password
		return 'Password reset successful'
	else:
		return 'User does not exist'

