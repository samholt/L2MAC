class Recommendations:
	def __init__(self):
		self.recommendations_db = {}

	def add_recommendation(self, user_id, recommendation):
		if user_id not in self.recommendations_db:
			self.recommendations_db[user_id] = []
		self.recommendations_db[user_id].append(recommendation)

	def get_recommendations(self, user_id):
		return self.recommendations_db.get(user_id, [])

	def add_savings_tip(self, user_id, savings_tip):
		if user_id not in self.recommendations_db:
			self.recommendations_db[user_id] = []
		self.recommendations_db[user_id].append(savings_tip)

	def get_savings_tips(self, user_id):
		return self.recommendations_db.get(user_id, [])
