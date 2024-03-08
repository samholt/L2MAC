import datetime

# Mock database
user_data = {}
transaction_data = {}


def generate_monthly_report(user_id):
	"""Generate a monthly financial report for a user"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	transactions = transaction_data.get(user_id)
	if not transactions:
		return 'No transactions found'
	
	current_month = datetime.datetime.now().month
	monthly_transactions = [t for t in transactions if t['date'].month == current_month]
	
	total_spent = sum(t['amount'] for t in monthly_transactions if t['type'] == 'expense')
	total_income = sum(t['amount'] for t in monthly_transactions if t['type'] == 'income')
	
	return {
		'total_spent': total_spent,
		'total_income': total_income,
		'balance': total_income - total_spent
	}


def analyze_spending_habits(user_id):
	"""Analyze a user's spending habits"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	transactions = transaction_data.get(user_id)
	if not transactions:
		return 'No transactions found'
	
	spending_categories = [t['category'] for t in transactions if t['type'] == 'expense']
	category_counts = {category: spending_categories.count(category) for category in set(spending_categories)}
	
	return category_counts


def compare_year_on_year(user_id):
	"""Compare year-on-year financial data for a user"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	transactions = transaction_data.get(user_id)
	if not transactions:
		return 'No transactions found'
	
	current_year = datetime.datetime.now().year
	last_year_transactions = [t for t in transactions if t['date'].year == current_year - 1]
	this_year_transactions = [t for t in transactions if t['date'].year == current_year]
	
	last_year_spent = sum(t['amount'] for t in last_year_transactions if t['type'] == 'expense')
	this_year_spent = sum(t['amount'] for t in this_year_transactions if t['type'] == 'expense')
	
	return {
		'last_year_spent': last_year_spent,
		'this_year_spent': this_year_spent,
		'difference': this_year_spent - last_year_spent
	}
