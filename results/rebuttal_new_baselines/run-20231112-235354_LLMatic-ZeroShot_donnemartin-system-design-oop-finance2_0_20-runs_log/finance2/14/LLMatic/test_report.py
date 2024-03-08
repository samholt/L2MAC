import pytest
from models.user import User
from models.transaction import Transaction
from models.investment import Investment
from models.report import Report
from datetime import datetime


def test_generate_monthly_summary():
	user = User('test_user', 'test@example.com', 'password')
	transactions = [
		Transaction(user, 100, 'groceries', datetime(2021, 1, 1)),
		Transaction(user, 200, 'rent', datetime(2021, 1, 2)),
		Transaction(user, 300, 'groceries', datetime(2021, 2, 1)),
		Transaction(user, 400, 'rent', datetime(2021, 2, 2))
	]
	Transaction.get_user_transactions = lambda user: transactions
	report = Report(user)
	assert report.generate_monthly_summary() == {'2021-01': 300, '2021-02': 700}


def test_analyze_spending_patterns():
	user = User('test_user', 'test@example.com', 'password')
	transactions = [
		Transaction(user, 100, 'groceries'),
		Transaction(user, 200, 'rent'),
		Transaction(user, 300, 'groceries'),
		Transaction(user, 400, 'rent')
	]
	Transaction.get_user_transactions = lambda user: transactions
	report = Report(user)
	assert report.analyze_spending_patterns() == {'groceries': 400, 'rent': 600}


def test_overview_asset_allocation():
	user = User('test_user', 'test@example.com', 'password')
	investments = [
		Investment(user, 1000, 'Stocks'),
		Investment(user, 2000, 'Bonds')
	]
	Investment.get_user_investments = lambda user: investments
	report = Report(user)
	assert report.overview_asset_allocation() == {'Stocks': 1000, 'Bonds': 2000}
