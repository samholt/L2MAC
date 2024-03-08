class Search:
	def __init__(self, users, posts):
		self.users = users
		self.posts = posts

	def search_users(self, keyword):
		return [user for user in self.users if keyword in user.username]

	def search_posts(self, keyword):
		return [post for post in self.posts if keyword in post.text]

	def filter_posts(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.posts if '#' + filter_value in post.text]
		elif filter_type == 'mention':
			return [post for post in self.posts if '@' + filter_value in post.text]
		elif filter_type == 'trending':
			return [post for post in self.posts if post.likes + post.retweets > 100]
		else:
			return []
