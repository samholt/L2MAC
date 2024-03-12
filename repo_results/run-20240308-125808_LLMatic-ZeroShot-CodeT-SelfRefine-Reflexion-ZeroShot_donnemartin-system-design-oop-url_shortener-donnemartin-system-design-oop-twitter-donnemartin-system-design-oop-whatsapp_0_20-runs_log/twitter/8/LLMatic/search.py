class Search:
	def __init__(self, db):
		self.db = db

	def search_posts(self, keyword):
		results = []
		for post in self.db.values():
			if keyword in post['text']:
				results.append(post)
		return results

	def search_users(self, keyword, users_db):
		results = []
		for user in users_db.values():
			if keyword in user.username:
				results.append(user)
		return results

	def filter_posts(self, filter_type, filter_value):
		results = []
		if filter_type == 'hashtag':
			for post in self.db.values():
				if '#' + filter_value in post['text']:
					results.append(post)
		elif filter_type == 'mention':
			for post in self.db.values():
				if '@' + filter_value in post['text']:
					results.append(post)
		elif filter_type == 'trending':
			# For simplicity, we consider a post as trending if it has more than 10 likes
			for post in self.db.values():
				if post['likes'] > 10:
					results.append(post)
		return results
