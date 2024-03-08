import datetime
import pandas as pd

# Mock database
DB = {}


def generate_monthly_report(user_id):
	"""Generate a monthly financial report for a user"""
	transactions = DB.get(user_id, [])
	if not transactions:
		return 'No transactions found'
	
	# Convert list of transactions to DataFrame
	data = pd.DataFrame(transactions)
	
	# Group by month and calculate total amount
	report = data.groupby(data.date.dt.month).amount.sum()
	return report.to_dict()


def generate_spending_trends(user_id):
	"""Generate spending habits and trends for a user"""
	transactions = DB.get(user_id, [])
	if not transactions:
		return 'No transactions found'
	
	# Convert list of transactions to DataFrame
	data = pd.DataFrame(transactions)
	
	# Group by category and calculate total amount
	trends = data.groupby('category').amount.sum()
	return trends.to_dict()


def compare_year_on_year(user_id):
	"""Compare year-on-year financial data for a user"""
	transactions = DB.get(user_id, [])
	if not transactions:
		return 'No transactions found'
	
	# Convert list of transactions to DataFrame
	data = pd.DataFrame(transactions)
	
	# Group by year and calculate total amount
	comparison = data.groupby(data.date.dt.year).amount.sum()
	return comparison.to_dict()
