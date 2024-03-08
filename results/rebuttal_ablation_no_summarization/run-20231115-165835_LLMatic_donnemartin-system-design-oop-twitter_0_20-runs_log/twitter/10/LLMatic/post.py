class Post:
	# Mock database
	posts = {}

	def __init__(self, user, text, images=None, location='global'):
		self.user = user
		self.text = text
		self.images = images
		self.location = location
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create_post(self):
		self.posts[self.user] = {'text': self.text, 'images': self.images, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies, 'location': self.location}
		return self.posts

	def delete_post(self):
		if self.posts.get(self.user):
			del self.posts[self.user]
			return 'Post deleted'
		else:
			return 'Post not found'

	def like_post(self):
		self.likes += 1
		return 'Post liked'

	def retweet_post(self):
		self.retweets += 1
		return 'Post retweeted'

	def reply_post(self, reply):
		self.replies.append(reply)
		return 'Reply added'

	def search_posts_by_keyword(self, keyword):
		# Search for posts containing the keyword
		return [post for post in self.posts.values() if keyword in post['text']]

	def filter_posts_by_hashtag(self, hashtag):
		# Filter posts based on the hashtag
		return [post for post in self.posts.values() if hashtag in post['text']]

	def filter_posts_by_user_mentions(self, user):
		# Filter posts based on user mentions
		return [post for post in self.posts.values() if f'@{user}' in post['text']]

	def filter_posts_by_trending_topics(self, topic):
		# Filter posts based on trending topics
		return [post for post in self.posts.values() if topic in post['text']]

	def get_trending_topics(self):
		# Identify and display trending hashtags or topics based on volume and velocity of mentions
		from collections import Counter
		topics = Counter()
		for post in self.posts.values():
			words = post['text'].split()
			for word in words:
				if word.startswith('#'):
					topics[word] += 1
		return topics.most_common()

	def sort_trending_topics(self, location='global'):
		# Sort trending topics based on location or globally
		from collections import Counter
		topics = Counter()
		for post in self.posts.values():
			if post['location'] == location:
				words = post['text'].split()
				for word in words:
					if word.startswith('#'):
						topics[word] += 1
		return topics.most_common()
