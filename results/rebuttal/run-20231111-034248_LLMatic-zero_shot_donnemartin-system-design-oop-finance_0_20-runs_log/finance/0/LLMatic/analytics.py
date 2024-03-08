class Analytics:
	def __init__(self):
		self.data = {}

	def add_data(self, user_id, month, amount):
		if user_id not in self.data:
			self.data[user_id] = {}
		if month not in self.data[user_id]:
			self.data[user_id][month] = 0
		self.data[user_id][month] += amount

	def monthly_report(self, user_id):
		if user_id in self.data:
			return self.data[user_id]
		else:
			return 'No data available for this user'

	def yearly_report(self, user_id):
		if user_id in self.data:
			return sum(self.data[user_id].values())
		else:
			return 'No data available for this user'

	def compare_year_on_year(self, user_id, year1, year2):
		if user_id in self.data:
			if year1 in self.data[user_id] and year2 in self.data[user_id]:
				return self.data[user_id][year2] - self.data[user_id][year1]
			else:
				return 'One or both years not available for this user'
		else:
			return 'No data available for this user'
