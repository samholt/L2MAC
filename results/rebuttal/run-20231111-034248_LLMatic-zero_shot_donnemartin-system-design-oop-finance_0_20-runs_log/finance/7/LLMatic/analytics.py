class Analytics:
	def __init__(self):
		self.data = {}

	def add_data(self, user_id, data):
		if user_id not in self.data:
			self.data[user_id] = []
		self.data[user_id].append(data)

	def generate_monthly_report(self, user_id):
		if user_id not in self.data:
			return 'No data available'
		return self.data[user_id]

	def generate_spending_habits(self, user_id):
		if user_id not in self.data:
			return 'No data available'
		return self.data[user_id]

	def compare_year_on_year(self, user_id):
		if user_id not in self.data:
			return 'No data available'
		return self.data[user_id]
