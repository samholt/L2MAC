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
		self.posts = []
		self.following = []
		self.notifications = []

	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self, db):
		if self.email in db:
			return 'User already exists'
		db[self.email] = self
		return 'User registered successfully'

	def authenticate(self, password, db):
		if self.email not in db:
			return 'User does not exist'
		if db[self.email].password != self.hash_password(password):
			return 'Invalid password'
		return jwt.encode({'user': self.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')

	def reset_password(self, new_password, db):
		if self.email not in db:
			return 'User does not exist'
		db[self.email].password = self.hash_password(new_password)
		return 'Password reset successfully'

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture is not None else self.profile_picture
		self.bio = bio if bio is not None else self.bio
		self.website_link = website_link if website_link is not None else self.website_link
		self.location = location if location is not None else self.location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting toggled successfully'

	def follow(self, user_to_follow):
		if user_to_follow.email not in self.following:
			self.following.append(user_to_follow.email)
			return 'Followed successfully'
		return 'Already following'

	def unfollow(self, user_to_unfollow):
		if user_to_unfollow.email in self.following:
			self.following.remove(user_to_unfollow.email)
			return 'Unfollowed successfully'
		return 'Not following'

	def view_timeline(self, db):
		timeline = []
		for user_email in self.following:
			if user_email in db:
				timeline.extend(db[user_email].posts)
		return timeline

	def receive_notification(self, notification):
		self.notifications.append(notification)

	def get_recommendations(self, db):
		recommendations = []
		for user in db.values():
			if user.email != self.email and user.email not in self.following:
				recommendations.append(user.email)
		return recommendations
