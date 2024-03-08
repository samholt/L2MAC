class Reports:
	def __init__(self, database):
		self.database = database

	def generate_financial_report(self, user_id):
		# Mocking a financial report generation
		user_data = self.database.get(user_id)
		return {'balance': user_data['balance'], 'expenses': user_data['expenses'], 'income': user_data['income']}

	def customize_alerts(self, user_id, alert_type, alert_value):
		# Mocking a customizable alert
		user_data = self.database.get(user_id)
		user_data['alerts'][alert_type] = alert_value
		self.database[user_id] = user_data
		return user_data['alerts']
