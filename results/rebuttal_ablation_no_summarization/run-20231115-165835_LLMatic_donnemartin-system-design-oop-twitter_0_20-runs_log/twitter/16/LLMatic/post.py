import datetime


class Post:
	def __init__(self):
		self.database = {}

	def create(self, user, text, image):
		timestamp = datetime.datetime.now()
		self.database[timestamp] = {'user': user, 'text': text, 'image': image, 'timestamp': timestamp, 'likes': 0, 'retweets': 0, 'replies': []}
		return self.database[timestamp]

	def delete(self, timestamp):
		if timestamp in self.database:
			del self.database[timestamp]
			return True
		return False

	def like(self, timestamp):
		if timestamp in self.database:
			self.database[timestamp]['likes'] += 1
			return True
		return False

	def retweet(self, timestamp):
		if timestamp in self.database:
			self.database[timestamp]['retweets'] += 1
			return True
		return False

	def reply(self, timestamp, reply):
		if timestamp in self.database:
			self.database[timestamp]['replies'].append(reply)
			return True
		return False
