class Recommendations:
	def __init__(self):
		self.recommendations_db = {}

	def add_recommendation(self, username, recommendation):
		if username not in self.recommendations_db:
			self.recommendations_db[username] = []
		self.recommendations_db[username].append(recommendation)
		return 'Recommendation added successfully'

	def get_recommendations(self, username):
		if username in self.recommendations_db:
			return self.recommendations_db[username]
		else:
			return 'No recommendations available'

