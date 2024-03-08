class Analytics:
	def __init__(self):
		self.data = {}

	def generate_monthly_report(self, month):
		if month not in self.data:
			return 'No data for this month'
		return self.data[month]

	def visualize_spending(self, month):
		if month not in self.data:
			return 'No data for this month'
		return 'Visualizing data for ' + month

	def compare_year_on_year(self, year1, year2):
		if year1 not in self.data or year2 not in self.data:
			return 'Data for one or both years not available'
		return 'Comparing data for ' + year1 + ' and ' + year2
