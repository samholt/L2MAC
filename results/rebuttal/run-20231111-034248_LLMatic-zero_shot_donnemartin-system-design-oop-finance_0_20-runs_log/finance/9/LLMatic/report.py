from user import User
from investment import Investment


class Report:
	def __init__(self, user, month, income, expenses, savings, investments):
		self.user = user
		self.month = month
		self.income = income
		self.expenses = expenses
		self.savings = savings
		self.investments = [Investment(name, 0, 0, 0) for name in investments]

	def generate_monthly_report(self):
		return {
			'user': self.user.username,
			'month': self.month,
			'income': self.income,
			'expenses': self.expenses,
			'savings': self.savings,
			'investments': [investment.name for investment in self.investments]
		}

	def visualize_spending(self):
		# This function is a placeholder as we cannot visualize any graphical output.
		pass

	def compare_year_on_year(self, previous_year_report):
		# This function is a placeholder as we cannot visualize any graphical output.
		pass


class ReportManager:
	def __init__(self):
		self.reports = {}

	def create_report(self, user, month, income, expenses, savings, investments):
		report = Report(user, month, income, expenses, savings, investments)
		self.reports[(user.username, month)] = report
		return report

	def get_report(self, username, month):
		return self.reports.get((username, month))
