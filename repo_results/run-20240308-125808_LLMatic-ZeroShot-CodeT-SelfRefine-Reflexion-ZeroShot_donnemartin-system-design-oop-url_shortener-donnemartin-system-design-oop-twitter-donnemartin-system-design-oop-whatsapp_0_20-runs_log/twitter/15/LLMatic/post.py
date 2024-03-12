class Post:
	def __init__(self, user, text, image, timestamp):
		self.user = user
		self.text = text
		self.image = image
		self.timestamp = timestamp
		self.likes = []
		self.retweets = []
		self.replies = []

	def create_post(self, db):
		post_id = len(db) + 1
		db[post_id] = self

	def delete_post(self, post_id, db):
		if post_id in db:
			del db[post_id]

	def like_post(self, user):
		self.likes.append(user)

	def retweet_post(self, user):
		self.retweets.append(user)

	def reply_post(self, reply):
		self.replies.append(reply)

	@staticmethod
	def search(keyword, db):
		return [post for post in db.values() if keyword in post.text]

	@staticmethod
	def filter_posts(filter, db):
		return [post for post in db.values() if filter in post.text]

	@staticmethod
	def get_trending_topics(db):
		from collections import Counter
		topics = []
		for post in db.values():
			words = post.text.split()
			topics.extend(word for word in words if word.startswith('#'))
		return [topic for topic, count in Counter(topics).most_common(5)]
