from datetime import datetime


class User:
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password


class Comment:
	def __init__(self, id, user_id, text):
		self.id = id
		self.user_id = user_id
		self.text = text

	def delete(self):
		# delete the comment
		pass


class Message:
	def __init__(self, id, sender_id, receiver_id, text, timestamp=None):
		self.id = id
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.text = text
		self.timestamp = timestamp if timestamp else datetime.now()

	def send(self):
		# send the message
		pass

	def delete(self):
		# delete the message
		pass


class Notification:
	def __init__(self, id, user_id, type, timestamp=None):
		self.id = id
		self.user_id = user_id
		self.type = type
		self.timestamp = timestamp if timestamp else datetime.now()

	def create(self):
		# create the notification
		pass


class TrendingTopic:
	def __init__(self, id, hashtag, count, timestamp=None):
		self.id = id
		self.hashtag = hashtag
		self.count = count
		self.timestamp = timestamp if timestamp else datetime.now()

	def update_count(self, new_count):
		self.count = new_count
