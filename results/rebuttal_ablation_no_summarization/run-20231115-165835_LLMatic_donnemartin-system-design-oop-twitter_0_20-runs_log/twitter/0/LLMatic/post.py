import re
from collections import Counter

class Post:
	def __init__(self, user, text, image, timestamp):
		self.user = user
		self.text = text
		self.image = image
		self.timestamp = timestamp
		self.likes = 0
		self.retweets = []
		self.replies = []

	def like_post(self):
		self.likes += 1

	def retweet(self, user):
		self.retweets.append(user)

	def reply(self, user, text):
		self.replies.append({'user': user, 'text': text})

mock_db = {}

def create_post(post):
	mock_db[post.timestamp] = post

def delete_post(timestamp):
	if timestamp in mock_db:
		del mock_db[timestamp]

def search(keyword):
	return [post for post in mock_db.values() if keyword in post.text]

def filter_posts(filter):
	return [post for post in mock_db.values() if filter in post.text]

def get_trending_topics():
	all_hashtags = [re.findall(r'#\w+', post.text) for post in mock_db.values()]
	all_hashtags = [hashtag for sublist in all_hashtags for hashtag in sublist]
	return [item for item, count in Counter(all_hashtags).most_common()]

