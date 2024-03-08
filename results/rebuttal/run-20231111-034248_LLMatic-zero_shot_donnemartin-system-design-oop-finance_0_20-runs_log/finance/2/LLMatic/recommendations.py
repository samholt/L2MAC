class Recommendations:
	def __init__(self):
		self.recommendations = {}

	def add_recommendation(self, user_id, recommendation):
		if user_id not in self.recommendations:
			self.recommendations[user_id] = []
		self.recommendations[user_id].append(recommendation)

	def get_recommendations(self, user_id):
		return self.recommendations.get(user_id, [])

	def clear_recommendations(self, user_id):
		if user_id in self.recommendations:
			self.recommendations[user_id] = []

	def generate_savings_tips(self, user_id, spending_habits, budget):
		# Mock implementation of savings tips generation based on user's spending habits and budget
		# In a real-world application, this would involve more complex logic and possibly machine learning algorithms
		tips = []
		if spending_habits.get('food', 0) > 0.3 * budget:
			tips.append('Consider cooking at home to save on food expenses.')
		if spending_habits.get('entertainment', 0) > 0.1 * budget:
			tips.append('Consider reducing entertainment expenses.')
		if spending_habits.get('transportation', 0) > 0.15 * budget:
			tips.append('Consider using public transportation to save on transportation costs.')
		self.add_recommendation(user_id, {'savings_tips': tips})
