class Search:
	def __init__(self, users_db, posts_db):
		self.users_db = users_db
		self.posts_db = posts_db

	def search_by_keyword(self, keyword):
		matched_users = [user for user in self.users_db.values() if keyword in user.username or keyword in user.email]
		matched_posts = [post for post in self.posts_db.values() if keyword in post.content]
		return matched_users, matched_posts

	def filter_posts(self, filter_criteria):
		if filter_criteria == 'hashtags':
			filtered_posts = [post for post in self.posts_db.values() if '#' in post.content]
		elif filter_criteria == 'user_mentions':
			filtered_posts = [post for post in self.posts_db.values() if '@' in post.content]
		elif filter_criteria == 'trending_topics':
			filtered_posts = sorted(self.posts_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)[:10]
		else:
			filtered_posts = []
		return filtered_posts
