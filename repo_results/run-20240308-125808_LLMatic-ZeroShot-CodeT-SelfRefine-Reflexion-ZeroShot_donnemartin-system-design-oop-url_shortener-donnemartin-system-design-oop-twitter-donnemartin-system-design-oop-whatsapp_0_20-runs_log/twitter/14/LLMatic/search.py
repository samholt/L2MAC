class Search:
	def __init__(self, user_db, post_db):
		self.user_db = user_db
		self.post_db = post_db

	def search_users(self, keyword):
		return [user for user in self.user_db.values() if keyword in user.username]

	def search_posts(self, keyword):
		return [post for post in self.post_db.values() if keyword in post.text]

	def filter_posts(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.post_db.values() if filter_value in post.text.split()]
		elif filter_type == 'user_mention':
			return [post for post in self.post_db.values() if filter_value in post.text.split()]
		elif filter_type == 'trending_topic':
			return sorted(self.post_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)[:10]
		else:
			raise Exception('Invalid filter type')
