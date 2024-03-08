class Recommendation:
	def __init__(self):
		self.recommendations_db = {}

	def generate_savings_tips(self, user_id, spending_data):
		# Mock implementation of generating savings tips based on user's spending data
		tips = 'Save more on ' + min(spending_data, key=spending_data.get)
		self.recommendations_db[user_id] = tips
		return tips

	def recommend_financial_products(self, user_id, financial_profile):
		# Mock implementation of recommending financial products based on user's financial profile
		products = 'Invest in ' + max(financial_profile, key=financial_profile.get)
		self.recommendations_db[user_id] = products
		return products
