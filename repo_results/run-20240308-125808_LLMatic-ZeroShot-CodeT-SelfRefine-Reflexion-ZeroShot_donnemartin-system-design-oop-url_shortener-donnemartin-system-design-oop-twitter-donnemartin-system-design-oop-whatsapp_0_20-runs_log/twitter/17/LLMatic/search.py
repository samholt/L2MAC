class Search:
	def __init__(self, users, posts):
		self.users = users
		self.posts = posts

	def search_users(self, keyword):
		return [user for user in self.users if keyword.lower() in user.username.lower()]

	def search_posts(self, keyword):
		return [post for post in self.posts if keyword.lower() in post.content.lower()]

	def filter_posts(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.posts if f'#{filter_value.lower()}' in post.content.lower()]
		elif filter_type == 'user_mention':
			return [post for post in self.posts if f'@{filter_value.lower()}' in post.content.lower()]
		elif filter_type == 'trending_topic':
			# For simplicity, we consider a topic trending if it appears in more than half of the posts
			return [post for post in self.posts if filter_value.lower() in post.content.lower() and sum(filter_value.lower() in p.content.lower() for p in self.posts) > len(self.posts) / 2]
