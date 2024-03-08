class Security:
	def __init__(self):
		self.user_data = {}
		self.payment_data = {}

	def protect_user_data(self, user_id, data):
		self.user_data[user_id] = data
		return True

	def get_user_data(self, user_id):
		return self.user_data.get(user_id, None)

	def secure_payment(self, user_id, payment_info):
		self.payment_data[user_id] = payment_info
		return True

	def get_payment_info(self, user_id):
		return self.payment_data.get(user_id, None)
