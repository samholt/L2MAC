class Security:
	def __init__(self):
		self.user_data = {}
		self.transaction_data = {}

	def protect_user_data(self, user_id, user_info):
		self.user_data[user_id] = user_info
		return 'User data protected'

	def maintain_privacy(self, user_id):
		if user_id in self.user_data:
			return 'Privacy maintained'
		else:
			return 'User not found'

	def secure_transaction(self, transaction_id, transaction_info):
		self.transaction_data[transaction_id] = transaction_info
		return 'Transaction secured'
