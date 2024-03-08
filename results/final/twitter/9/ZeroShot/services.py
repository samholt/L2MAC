from models import db, User, Post, Comment, Like, Follow, Message, Notification, TrendingTopic


class UserService:
	@staticmethod
	def create_user(email, password, username):
		# User creation logic here
		pass

	@staticmethod
	def get_user_by_email(email):
		# User retrieval logic here
		pass

	@staticmethod
	def update_user(user, data):
		# User update logic here
		pass


class PostService:
	@staticmethod
	def create_post(user, content):
		# Post creation logic here
		pass

	@staticmethod
	def delete_post(post):
		# Post deletion logic here
		pass


class CommentService:
	@staticmethod
	def create_comment(user, post, content):
		# Comment creation logic here
		pass


class LikeService:
	@staticmethod
	def create_like(user, post):
		# Like creation logic here
		pass

	@staticmethod
	def delete_like(like):
		# Like deletion logic here
		pass


class FollowService:
	@staticmethod
	def create_follow(follower, followee):
		# Follow creation logic here
		pass

	@staticmethod
	def delete_follow(follow):
		# Follow deletion logic here
		pass


class MessageService:
	@staticmethod
	def create_message(sender, receiver, content):
		# Message creation logic here
		pass


class NotificationService:
	@staticmethod
	def create_notification(user, content):
		# Notification creation logic here
		pass

	@staticmethod
	def get_notifications(user):
		# Notification retrieval logic here
		pass


class TrendingTopicService:
	@staticmethod
	def get_trending_topics():
		# Trending topics retrieval logic here
		pass
