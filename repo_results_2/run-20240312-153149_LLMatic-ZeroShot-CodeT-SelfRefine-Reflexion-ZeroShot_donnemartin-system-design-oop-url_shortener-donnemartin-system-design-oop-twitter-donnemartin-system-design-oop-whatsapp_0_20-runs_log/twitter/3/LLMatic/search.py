class Search:
	def __init__(self, users_db, posts_db):
		self.users_db = users_db
		self.posts_db = posts_db

	def search_users(self, keyword):
		return [user for user in self.users_db.values() if keyword in user.username]

	def search_posts(self, keyword):
		return [post for post in self.posts_db.values() if keyword in post.content]

	def filter_posts(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.posts_db.values() if filter_value in post.content.split()]
		elif filter_type == 'user_mention':
			return [post for post in self.posts_db.values() if filter_value in post.content.split()]
		elif filter_type == 'trending_topic':
			trending_posts = sorted(self.posts_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)
			return [post for post in trending_posts if filter_value in post.content.split()]
		else:
			return 'Invalid filter type'
