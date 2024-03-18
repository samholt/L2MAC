class Search:
	def __init__(self, users, posts):
		self.users = users
		self.posts = posts

	def search(self, keyword):
		user_results = [user for user in self.users if keyword in user.username]
		post_results = [post for post in self.posts if keyword in post.content]
		return user_results, post_results

	def filter(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.posts if f'#{filter_value}' in post.content]
		elif filter_type == 'user_mention':
			return [post for post in self.posts if f'@{filter_value}' in post.content]
		elif filter_type == 'trending_topic':
			return [post for post in self.posts if filter_value in post.content]
		else:
			return []
