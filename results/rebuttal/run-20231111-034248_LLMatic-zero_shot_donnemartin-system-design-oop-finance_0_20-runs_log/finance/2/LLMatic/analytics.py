class Analytics:
	def __init__(self):
		self.data = {}

	def add_monthly_report(self, user, month, report):
		if user not in self.data:
			self.data[user] = {}
		self.data[user][month] = report

	def get_monthly_report(self, user, month):
		if user in self.data and month in self.data[user]:
			return self.data[user][month]
		return 'No report found'

	def add_yearly_report(self, user, year, report):
		if user not in self.data:
			self.data[user] = {}
		self.data[user][year] = report

	def get_yearly_report(self, user, year):
		if user in self.data and year in self.data[user]:
			return self.data[user][year]
		return 'No report found'

	def add_spending_habits(self, user, habits):
		if user not in self.data:
			self.data[user] = {}
		self.data[user]['habits'] = habits

	def get_spending_habits(self, user):
		if user in self.data and 'habits' in self.data[user]:
			return self.data[user]['habits']
		return 'No habits found'
