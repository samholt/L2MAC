import hashlib
import jwt
import datetime


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
		self.followers = []
		self.notifications = []
		self.posts = []

	def hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self, db):
		if self.email in db:
			return 'User already exists'
		else:
			db[self.email] = self
			return 'User registered successfully'

	def authenticate(self, password, db):
		if self.email in db and db[self.email].password == self.hash_password(password):
			return jwt.encode({'user': self.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')
		else:
			return 'Invalid credentials'

	def reset_password(self, new_password, db):
		if self.email in db:
			db[self.email].password = self.hash_password(new_password)
			return 'Password reset successful'
		else:
			return 'User does not exist'

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

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			return 'Followed successfully'
		else:
			return 'Already following'

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
			return 'Unfollowed successfully'
		else:
			return 'Not following'

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		timeline.sort(key=lambda post: post.timestamp, reverse=True)
		return timeline

	def receive_notification(self, notification):
		self.notifications.append(notification)
		return 'Notification received'

	def recommend_users(self, db):
		recommended_users = []
		for user in db.values():
			if user != self and user not in self.following:
				mutual_followers = len(set(self.followers) & set(user.followers))
				if mutual_followers > 0 or any(follower in self.following for follower in user.followers):
					recommended_users.append(user)
		return recommended_users
