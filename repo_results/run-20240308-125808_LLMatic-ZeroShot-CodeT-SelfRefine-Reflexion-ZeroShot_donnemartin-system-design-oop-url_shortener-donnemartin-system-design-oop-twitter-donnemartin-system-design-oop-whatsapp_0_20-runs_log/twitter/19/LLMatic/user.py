import hashlib
import jwt
import time


class User:
	def __init__(self, email, username, password, is_private):
		self.email = email
		self.username = username
		self.password = self.hash_password(password)
		self.is_private = is_private
		self.profile_picture = None
		self.bio = None
		self.website_link = None
		self.location = None
		self.following = []
		self.notifications = []

	def hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self, users_db):
		if self.email in users_db:
			return 'User already exists'
		else:
			users_db[self.email] = self
			return 'User registered successfully'

	def authenticate(self, password, users_db):
		if self.email in users_db and self.password == self.hash_password(password):
			token = jwt.encode({'email': self.email, 'exp': time.time() + 600}, 'secret', algorithm='HS256')
			return token
		else:
			return 'Authentication failed'

	def reset_password(self, new_password, users_db):
		if self.email in users_db:
			self.password = self.hash_password(new_password)
			users_db[self.email] = self
			return 'Password reset successful'
		else:
			return 'User not found'

	def update_profile_picture(self, new_picture):
		self.profile_picture = new_picture
		return 'Profile picture updated successfully'

	def update_bio(self, new_bio):
		self.bio = new_bio
		return 'Bio updated successfully'

	def update_website_link(self, new_website_link):
		self.website_link = new_website_link
		return 'Website link updated successfully'

	def update_location(self, new_location):
		self.location = new_location
		return 'Location updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting updated successfully'

	def follow(self, user_to_follow):
		if user_to_follow not in self.following:
			self.following.append(user_to_follow)
			return 'Followed successfully'
		else:
			return 'Already following'

	def unfollow(self, user_to_unfollow):
		if user_to_unfollow in self.following:
			self.following.remove(user_to_unfollow)
			return 'Unfollowed successfully'
		else:
			return 'Not following'

	def view_timeline(self, posts_db):
		timeline_posts = []
		for post in posts_db.values():
			if post.author in self.following:
				timeline_posts.append(post)
		return timeline_posts

	def receive_notification(self, notification):
		self.notifications.append(notification)
		return 'Notification received successfully'

	def recommend_users(self, users_db):
		recommended_users = []
		for user in users_db.values():
			if user.username not in self.following and user.username != self.username:
				recommended_users.append(user.username)
		return recommended_users
