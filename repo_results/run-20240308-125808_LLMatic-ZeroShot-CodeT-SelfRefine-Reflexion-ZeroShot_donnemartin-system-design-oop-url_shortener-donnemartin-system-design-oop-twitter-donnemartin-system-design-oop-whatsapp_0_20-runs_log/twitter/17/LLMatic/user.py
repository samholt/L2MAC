import jwt
import datetime
from post import Post

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
		self.notifications = []
		self.posts = []

	def register(self):
		# In a real-world application, you would store these details in a database
		return self

	def authenticate(self, password):
		if self.password == password:
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return None

	def reset_password(self, new_password):
		self.password = new_password
		return self

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_bio(self, bio):
		self.bio = bio

	def set_website_link(self, link):
		self.website_link = link

	def set_location(self, location):
		self.location = location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user.is_private:
			return 'Request sent'
		self.following.add(user)
		user.followers.add(self)
		user.notifications.append(f'{self.username} started following you')
		return 'Followed'

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
		return 'Unfollowed'

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		timeline.sort(key=lambda x: x.timestamp, reverse=True)
		return timeline

	def view_notifications(self):
		return self.notifications

	def receive_like_notification(self, post):
		self.notifications.append(f'{post.user.username} liked your post: {post.content}')

	def receive_retweet_notification(self, post):
		self.notifications.append(f'{post.user.username} retweeted your post: {post.content}')

	def receive_reply_notification(self, post, reply):
		self.notifications.append(f'{reply.user.username} replied to your post: {post.content}')

	def receive_mention_notification(self, post):
		self.notifications.append(f'{post.user.username} mentioned you in a post: {post.content}')

	def recommend_users(self, users):
		# This is a simple recommendation algorithm based on mutual followers and number of posts
		# In a real-world application, this would be much more complex and would take into account various factors
		recommendations = []
		for user in users:
			if user != self and len(self.followers & user.followers) > 0 and len(user.posts) > len(self.posts):
				recommendations.append(user)
		return recommendations
