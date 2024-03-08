class Reports:
	def __init__(self):
		self.data = {}

	def add_data(self, month, expenses, incomes, budget, investments):
		# Add data for a month
		self.data[month] = {'expenses': expenses, 'incomes': incomes, 'budget': budget, 'investments': investments}

	def generate_report(self, month):
		# Generate a report for a month
		if month in self.data:
			return self.data[month]
		else:
			return 'No data for this month'

	def set_alert(self, month, alert):
		# Set an alert for a month
		if month in self.data:
			self.data[month]['alert'] = alert
			return 'Alert set'
		else:
			return 'No data for this month to set an alert'
