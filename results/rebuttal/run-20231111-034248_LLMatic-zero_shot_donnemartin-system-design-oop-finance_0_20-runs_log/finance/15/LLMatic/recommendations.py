class Recommendations:
	def __init__(self, user):
		self.user = user

	def savings_tips(self):
		# Mocked data for demonstration
		tips = [
			'Consider cooking at home instead of eating out.',
			'Consider using public transportation instead of owning a car.',
			'Consider investing in a retirement fund.'
		]
		return tips

	def product_recommendations(self):
		# Mocked data for demonstration
		products = [
			'High interest savings account',
			'Low interest credit card',
			'Investment fund'
		]
		return products
