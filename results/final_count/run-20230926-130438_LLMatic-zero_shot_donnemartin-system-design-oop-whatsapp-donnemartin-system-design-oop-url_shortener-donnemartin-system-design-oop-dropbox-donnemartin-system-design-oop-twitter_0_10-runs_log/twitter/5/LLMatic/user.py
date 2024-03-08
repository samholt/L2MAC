import jwt
import datetime
from post import Post

SECRET_KEY = 'SECRET'


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
		self.followers = []
		self.notifications = []
		self.posts = []
		self.likes = []

	def register(self):
		return 'User registered successfully'

	def authenticate(self, password):
		if self.password == password:
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return 'Invalid password'

	def reset_password(self, new_password):
		self.password = new_password
		return 'Password reset successfully'

	def update_profile_picture(self, new_picture):
		self.profile_picture = new_picture
		return 'Profile picture updated successfully'

	def update_bio(self, new_bio):
		self.bio = new_bio
		return 'Bio updated successfully'

	def update_website_link(self, new_link):
		self.website_link = new_link
		return 'Website link updated successfully'

	def update_location(self, new_location):
		self.location = new_location
		return 'Location updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting toggled successfully'

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
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
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return sorted(timeline, key=lambda post: post.timestamp, reverse=True)

	def receive_notification(self, notification):
		self.notifications.append(notification)
		return 'Notification received successfully'

	def like_post(self, post):
		if post not in self.likes:
			self.likes.append(post)
			return 'Post liked successfully'
		else:
			return 'Already liked'

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user != self and user not in self.following:
				# Users who have similar interests
				if any(post in user.likes for post in self.likes):
					recommendations.append(user)
				# Users who are active
				elif len(user.posts) > len(self.posts):
					recommendations.append(user)
				# Users who have mutual followers
				elif any(follower in self.followers for follower in user.followers):
					recommendations.append(user)
		return recommendations

