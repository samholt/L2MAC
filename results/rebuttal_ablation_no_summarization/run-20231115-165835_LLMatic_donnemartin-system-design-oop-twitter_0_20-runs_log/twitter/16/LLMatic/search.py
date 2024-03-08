class Search:
	def __init__(self, user_db, post_db):
		self.user_db = user_db
		self.post_db = post_db

	def search(self, keyword):
		results = {'users': [], 'posts': []}
		for email, user in self.user_db.items():
			if keyword in user.username or keyword in user.bio:
				results['users'].append(user)
		for timestamp, post in self.post_db.database.items():
			if keyword in post['text']:
				results['posts'].append(post)
		return results

	def filter(self, keyword):
		results = []
		for timestamp, post in self.post_db.database.items():
			if keyword in post['text']:
				results.append(post)
		return results
