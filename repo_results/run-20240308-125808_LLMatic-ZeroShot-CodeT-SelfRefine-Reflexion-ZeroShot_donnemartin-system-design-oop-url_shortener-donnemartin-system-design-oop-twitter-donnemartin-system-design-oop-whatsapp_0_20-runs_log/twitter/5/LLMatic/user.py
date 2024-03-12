from notification import Notification
from post import Post
from collections import Counter


class User:
	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password
		self.notifications = []
		self.blocked_users = []
		self.posts = []
		self.inbox = []
		self.likes = []

	def like(self, post):
		post.like(self)
		self.notifications.append(Notification(self, 'like'))
		self.likes.append(post)

	def retweet(self, post):
		post.retweet(self)
		self.notifications.append(Notification(self, 'retweet'))

	def reply(self, post, text, images):
		post.reply(text, images, self)
		self.notifications.append(Notification(self, 'reply'))

	def mention(self, user):
		user.notifications.append(Notification(user, 'mention'))

	def create_post(self, text, images):
		post = Post(text, images, self)
		self.posts.append(post)
		return post

	def delete_post(self, post):
		if post in self.posts:
			self.posts.remove(post)

	def recommend_users(self, users):
		interests = [word for post in self.posts for word in post.text.split() if word.startswith('#')]
		activity = {user: len(user.posts) for user in users}
		mutual_followers = {user: len(set(self.likes).intersection(set(user.likes))) for user in users}
		recommendations = sorted(users, key=lambda user: (Counter(interests)[user.username], activity[user], mutual_followers[user]), reverse=True)
		return recommendations[:10]
