from models.transaction import Transaction
from models.investment import Investment
from collections import defaultdict
from datetime import datetime


class Report:
	def __init__(self, user):
		self.user = user

	def generate_monthly_summary(self):
		transactions = Transaction.get_user_transactions(self.user)
		monthly_summary = defaultdict(float)
		for transaction in transactions:
			month = transaction.date.strftime('%Y-%m')
			monthly_summary[month] += transaction.amount
		return dict(monthly_summary)

	def analyze_spending_patterns(self):
		transactions = Transaction.get_user_transactions(self.user)
		spending_patterns = defaultdict(float)
		for transaction in transactions:
			spending_patterns[transaction.category] += transaction.amount
		return dict(spending_patterns)

	def overview_asset_allocation(self):
		investments = Investment.get_user_investments(self.user)
		asset_allocation = defaultdict(float)
		for investment in investments:
			asset_allocation[investment.type] += investment.amount
		return dict(asset_allocation)
