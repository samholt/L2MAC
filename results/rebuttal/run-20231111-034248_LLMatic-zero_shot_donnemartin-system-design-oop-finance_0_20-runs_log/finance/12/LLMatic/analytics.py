import datetime

# Mock database
user_data = {}


def generate_monthly_report(user_id):
	"""Generate a monthly financial report for a user"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	# Calculate monthly income and expenses
	income = sum([t['amount'] for t in user['transactions'] if t['type'] == 'income'])
	expenses = sum([t['amount'] for t in user['transactions'] if t['type'] == 'expense'])
	
	return {
		'income': income,
		'expenses': expenses,
		'net': income - expenses
	}


def generate_spending_trends(user_id):
	"""Generate spending trends for a user"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	# Calculate spending by category
	spending = {}
	for t in user['transactions']:
		if t['type'] == 'expense':
			if t['category'] in spending:
				spending[t['category']] += t['amount']
			else:
				spending[t['category']] = t['amount']
	
	return spending


def compare_year_on_year(user_id, year1, year2):
	"""Compare year-on-year financial data for a user"""
	user = user_data.get(user_id)
	if not user:
		return 'User not found'
	
	# Calculate income and expenses for each year
	income1 = sum([t['amount'] for t in user['transactions'] if t['type'] == 'income' and t['date'].year == year1])
	expenses1 = sum([t['amount'] for t in user['transactions'] if t['type'] == 'expense' and t['date'].year == year1])
	income2 = sum([t['amount'] for t in user['transactions'] if t['type'] == 'income' and t['date'].year == year2])
	expenses2 = sum([t['amount'] for t in user['transactions'] if t['type'] == 'expense' and t['date'].year == year2])
	
	return {
		'year1': {
			'income': income1,
			'expenses': expenses1,
			'net': income1 - expenses1
		},
		'year2': {
			'income': income2,
			'expenses': expenses2,
			'net': income2 - expenses2
		}
	}
