class Search:
	def __init__(self, users_db, posts_db):
		self.users_db = users_db
		self.posts_db = posts_db

	def search_users(self, keyword):
		return [user.username for user in self.users_db.users.values() if keyword in user.username]

	def search_posts(self, keyword):
		return [post for post in self.posts_db.values() if keyword in post.text]

	def filter_posts(self, filter_type, filter_value):
		if filter_type == 'hashtag':
			return [post for post in self.posts_db.values() if '#' + filter_value in post.text]
		elif filter_type == 'user_mention':
			return [post for post in self.posts_db.values() if '@' + filter_value in post.text]
		elif filter_type == 'trending_topic':
			# For simplicity, we consider a topic trending if it appears in more than 5 posts
			trending_topics = [word for word in set(' '.join(post.text for post in self.posts_db.values()).split()) if sum(word in post.text.split() for post in self.posts_db.values()) > 5]
			return [post for post in self.posts_db.values() if filter_value in trending_topics]
		else:
			return []

