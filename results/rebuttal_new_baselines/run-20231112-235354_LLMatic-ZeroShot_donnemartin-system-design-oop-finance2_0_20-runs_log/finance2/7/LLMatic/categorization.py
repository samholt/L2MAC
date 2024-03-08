def categorize_expense(amount):
	if amount < 100:
		return 'Small'
	elif amount < 500:
		return 'Medium'
	else:
		return 'Large'

def categorize_income(source):
	if source in ['Salary', 'Rent', 'Dividends']:
		return 'Stable'
	else:
		return 'Variable'
