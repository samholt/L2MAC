import hashlib
import jwt
import datetime


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
		self.following = []
		self.followers = []
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
			return jwt.encode({'user': self.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')
		else:
			return 'Invalid credentials'

	def reset_password(self, new_password, users_db):
		if self.email in users_db:
			self.password = self.hash_password(new_password)
			return 'Password reset successful'
		else:
			return 'User does not exist'

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting updated'

	def follow_user(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			return 'Followed user successfully'
		else:
			return 'Already following user'

	def unfollow_user(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
			return 'Unfollowed user successfully'
		else:
			return 'Not following user'

	def notify(self, notification):
		self.notifications.append(notification)
		return 'Notification added successfully'

	def recommend_users(self, users_db):
		recommended_users = []
		for user in users_db.values():
			if user != self and user not in self.following:
				mutual_followers = len(set(self.followers) & set(user.followers))
				if mutual_followers > 0:
					recommended_users.append(user)
		return recommended_users

