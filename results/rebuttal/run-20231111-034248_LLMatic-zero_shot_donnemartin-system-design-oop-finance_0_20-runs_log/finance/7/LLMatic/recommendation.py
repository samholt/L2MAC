class Recommendation:
	def __init__(self):
		self.recommendations_db = {}

	def add_savings_tip(self, user_id, tip):
		if user_id not in self.recommendations_db:
			self.recommendations_db[user_id] = {'savings_tips': [], 'product_recommendations': []}
		self.recommendations_db[user_id]['savings_tips'].append(tip)

	def add_product_recommendation(self, user_id, product):
		if user_id not in self.recommendations_db:
			self.recommendations_db[user_id] = {'savings_tips': [], 'product_recommendations': []}
		self.recommendations_db[user_id]['product_recommendations'].append(product)

	def get_savings_tips(self, user_id):
		if user_id in self.recommendations_db:
			return self.recommendations_db[user_id]['savings_tips']
		else:
			return 'No savings tips available'

	def get_product_recommendations(self, user_id):
		if user_id in self.recommendations_db:
			return self.recommendations_db[user_id]['product_recommendations']
		else:
			return 'No product recommendations available'
