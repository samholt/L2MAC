class Search:
	def __init__(self, user_obj, post_obj):
		self.user_obj = user_obj
		self.post_obj = post_obj

	def search(self, keyword):
		matching_users = [user for user in self.user_obj.users if keyword in user]
		matching_posts = []
		for user in self.post_obj.posts_db:
			for post in self.post_obj.posts_db[user]:
				if keyword in post['content']:
					matching_posts.append(post)
		return matching_users, matching_posts

	def filter_posts(self, filter):
		filtered_posts = []
		for user in self.post_obj.posts_db:
			for post in self.post_obj.posts_db[user]:
				if filter in post['content']:
					filtered_posts.append(post)
		return filtered_posts
