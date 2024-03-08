class Investment:
	def __init__(self, user, amount, type):
		self.user = user
		self.amount = amount
		self.type = type

	@staticmethod
	def create_investment(user, amount, type):
		investment = Investment(user, amount, type)
		return investment

	@staticmethod
	def get_user_investments(user):
		# This is a mock function. In a real application, this would interact with a database.
		return [Investment(user, 1000, 'Stocks'), Investment(user, 2000, 'Bonds')]

	def track_performance(self):
		# This is a mock function. In a real application, this would interact with a database or an external API.
		return {'investment': self.serialize(), 'performance': 'Good'}

	def __repr__(self):
		return f'Investment(user={self.user}, amount={self.amount}, type={self.type})'

	def serialize(self):
		return {
			'user': self.user.serialize(),
			'amount': self.amount,
			'type': self.type
		}
