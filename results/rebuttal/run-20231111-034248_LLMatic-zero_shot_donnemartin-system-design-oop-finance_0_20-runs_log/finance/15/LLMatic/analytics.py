import datetime

# Mock database
DATABASE = {}


def generate_monthly_report(user_id):
	"""Generate a monthly financial report for a user"""
	user_data = DATABASE.get(user_id, {})
	report = {}
	for month in range(1, 13):
		monthly_data = user_data.get(month, {})
		report[month] = {
			'income': sum(transaction['amount'] for transaction in monthly_data.get('income', [])),
			'expenses': sum(transaction['amount'] for transaction in monthly_data.get('expenses', []))
		}
	return report


def get_spending_habits(user_id):
	"""Provide visual analytics for spending habits"""
	# For simplicity, we just return the data. In a real application, we would generate a chart or graph.
	return generate_monthly_report(user_id)


def compare_year_on_year(user_id, year1, year2):
	"""Compare year-on-year financial data"""
	data1 = DATABASE.get(user_id, {}).get(year1, {})
	data2 = DATABASE.get(user_id, {}).get(year2, {})
	comparison = {
		'year1': {
			'income': sum(transaction['amount'] for transaction in data1.get('income', [])),
			'expenses': sum(transaction['amount'] for transaction in data1.get('expenses', []))
		},
		'year2': {
			'income': sum(transaction['amount'] for transaction in data2.get('income', [])),
			'expenses': sum(transaction['amount'] for transaction in data2.get('expenses', []))
		}
	}
	return comparison
