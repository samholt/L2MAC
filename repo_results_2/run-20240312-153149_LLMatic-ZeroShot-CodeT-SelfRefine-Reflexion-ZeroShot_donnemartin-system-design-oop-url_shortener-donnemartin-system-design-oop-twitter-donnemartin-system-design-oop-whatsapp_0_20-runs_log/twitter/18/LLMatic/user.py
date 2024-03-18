import jwt
import datetime

SECRET_KEY = 'SECRET'


class User:
	def __init__(self, email, username, password, is_private):
		self.email = email
		self.username = username
		self.password = password
		self.is_private = is_private
		self.profile_picture = None
		self.bio = None
		self.website_link = None
		self.location = None
		self.following = set()
		self.followers = set()
		self.timeline = []
		self.notifications = []

	def register(self):
		# In a real-world application, you would store these details in a database
		return {'email': self.email, 'username': self.username, 'password': self.password, 'is_private': self.is_private}

	def authenticate(self, email, password):
		# In a real-world application, you would fetch these details from a database and compare
		if self.email == email and self.password == password:
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return 'Invalid credentials'

	def reset_password(self, new_password):
		self.password = new_password
		return 'Password reset successful'

	def set_profile_picture(self, picture):
		self.profile_picture = picture
		return 'Profile picture updated'

	def set_bio(self, bio):
		self.bio = bio
		return 'Bio updated'

	def set_website_link(self, link):
		self.website_link = link
		return 'Website link updated'

	def set_location(self, location):
		self.location = location
		return 'Location updated'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting updated'

	def follow(self, user):
		if user not in self.following:
			self.following.add(user)
			user.followers.add(self)
			user.notifications.append(f'{self.username} started following you.')
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
		for user in self.following:
			self.timeline.extend(user.posts)
		self.timeline.sort(key=lambda x: x['timestamp'], reverse=True)
		return self.timeline

