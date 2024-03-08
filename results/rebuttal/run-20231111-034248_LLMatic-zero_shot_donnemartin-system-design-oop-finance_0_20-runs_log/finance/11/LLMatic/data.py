from datetime import datetime

class Transaction:
	def __init__(self):
		self.transactions = {}
		self.budgets = {}
		self.investments = {}
		self.investment_alerts = {}
		self.monthly_reports = {}
		self.yearly_reports = {}
		self.savings_tips = {}
		self.product_recommendations = {}
		self.notifications = {}
		self.alerts = {}

	def add_transaction(self, user_id, transaction):
		if user_id not in self.transactions:
			self.transactions[user_id] = []
		transaction['date'] = datetime.strptime(transaction['date'], '%Y-%m-%d')
		self.transactions[user_id].append(transaction)

	def generate_monthly_report(self, user_id):
		if user_id not in self.transactions:
			return {}
		monthly_report = {}
		for transaction in self.transactions[user_id]:
			month = transaction['date'].month
			if month not in monthly_report:
				monthly_report[month] = {'income': 0, 'expenses': 0}
			if transaction['amount'] > 0:
				monthly_report[month]['income'] += transaction['amount']
			else:
				monthly_report[month]['expenses'] += transaction['amount']
		self.monthly_reports[user_id] = monthly_report
		return monthly_report

	def generate_yearly_report(self, user_id):
		if user_id not in self.transactions:
			return {}
		yearly_report = {}
		for transaction in self.transactions[user_id]:
			year = transaction['date'].year
			if year not in yearly_report:
				yearly_report[year] = {'income': 0, 'expenses': 0}
			if transaction['amount'] > 0:
				yearly_report[year]['income'] += transaction['amount']
			else:
				yearly_report[year]['expenses'] += transaction['amount']
		self.yearly_reports[user_id] = yearly_report
		return yearly_report

	def compare_yearly_data(self, user_id, year1, year2):
		if user_id not in self.yearly_reports:
			return {}
		if year1 not in self.yearly_reports[user_id] or year2 not in self.yearly_reports[user_id]:
			return {}
		comparison = {
			'year1': self.yearly_reports[user_id][year1],
			'year2': self.yearly_reports[user_id][year2]
		}
		return comparison

	def add_investment(self, user_id, investment):
		if user_id not in self.investments:
			self.investments[user_id] = []
		self.investments[user_id].append(investment)

	def calculate_investment_performance(self, user_id, investment_id):
		for investment in self.investments[user_id]:
			if investment['id'] == investment_id:
				return investment['amount'] * (1 + investment['return'] / 100)
		return 'Investment not found'

	def set_investment_alert(self, user_id, investment_id, alert_threshold):
		if user_id not in self.investment_alerts:
			self.investment_alerts[user_id] = {}
		self.investment_alerts[user_id][investment_id] = alert_threshold

	def check_investment_alerts(self, user_id):
		alerts = []
		for investment in self.investments[user_id]:
			if investment['id'] in self.investment_alerts[user_id] and self.calculate_investment_performance(user_id, investment['id']) >= self.investment_alerts[user_id][investment['id']]:
				alerts.append({'investment_id': investment['id'], 'message': 'Investment has reached alert threshold'})
				self.investment_alerts[user_id].pop(investment['id'])
		return alerts

	def generate_savings_tips(self, user_id):
		if user_id not in self.monthly_reports:
			self.generate_monthly_report(user_id)
		tips = []
		for month, report in self.monthly_reports[user_id].items():
			if report['expenses'] > report['income']:
				tips.append(f'You spent more than you earned in month {month}. Try to cut down on unnecessary expenses.')
			elif report['income'] - report['expenses'] < 0.2 * report['income']:
				tips.append(f'You are not saving enough in month {month}. Try to save at least 20% of your income.')
		self.savings_tips[user_id] = tips
		return tips

	def recommend_products(self, user_id):
		if user_id not in self.yearly_reports:
			self.generate_yearly_report(user_id)
		recommendations = []
		for year, report in self.yearly_reports[user_id].items():
			if report['income'] - report['expenses'] > 0.2 * report['income']:
				recommendations.append('Consider investing your surplus income.')
			else:
				recommendations.append('Consider a savings account to help manage your finances.')
		self.product_recommendations[user_id] = recommendations
		return recommendations

	def set_notification(self, user_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(notification)

	def get_notifications(self, user_id):
		if user_id in self.notifications:
			return self.notifications[user_id]
		return []

	def set_alert(self, user_id, alert):
		if user_id not in self.alerts:
			self.alerts[user_id] = []
		self.alerts[user_id].append(alert)

	def get_alerts(self, user_id):
		if user_id in self.alerts:
			return self.alerts[user_id]
		return []
