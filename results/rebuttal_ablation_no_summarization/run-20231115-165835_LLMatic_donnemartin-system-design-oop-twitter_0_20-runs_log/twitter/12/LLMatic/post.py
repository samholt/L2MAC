import datetime
import re
import collections

# Mock database
posts_db = {}
comments_db = {}


class Post:
	def __init__(self, username, text, images=None):
		self.username = username
		self.text = text
		self.images = images
		self.created_at = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0

	@staticmethod
	def create_post(username, text, images):
		if username not in posts_db:
			posts_db[username] = []
		post = Post(username, text, images)
		posts_db[username].append(post)
		return True

	@staticmethod
	def like_post(username, post_id):
		if username in posts_db and len(posts_db[username]) > post_id:
			posts_db[username][post_id].likes += 1
			return True
		return False

	@staticmethod
	def retweet_post(username, post_id):
		if username in posts_db and len(posts_db[username]) > post_id:
			posts_db[username][post_id].retweets += 1
			return True
		return False

	@staticmethod
	def search_posts(keyword):
		results = []
		for username in posts_db:
			for post in posts_db[username]:
				if keyword.lower() in post.text.lower():
					results.append(post)
		return results

	@staticmethod
	def filter_posts(filter_type, filter_value):
		results = []
		for username in posts_db:
			for post in posts_db[username]:
				if filter_type == 'hashtag' and '#' + filter_value in post.text:
					results.append(post)
				elif filter_type == 'mention' and '@' + filter_value in post.text:
					results.append(post)
				elif filter_type == 'trending' and any(word in post.text for word in filter_value):
					results.append(post)
		return results

	@staticmethod
	def get_trending_topics():
		hashtags = []
		for username in posts_db:
			for post in posts_db[username]:
				hashtags.extend(re.findall(r'#\w+', post.text))
		counter = collections.Counter(hashtags)
		return counter.most_common(10)


class Comment:
	def __init__(self, username, text, post_id):
		self.username = username
		self.text = text
		self.post_id = post_id
		self.created_at = datetime.datetime.now()

	@staticmethod
	def create_comment(username, text, post_id):
		if username not in comments_db:
			comments_db[username] = []
		comments_db[username].append(Comment(username, text, post_id))
		return True


# Expose the databases for testing
Post.posts_db = posts_db
Comment.comments_db = comments_db
