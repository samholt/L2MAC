from categorization import categorize_expense, categorize_income

def test_categorize_expense():
	assert categorize_expense(50) == 'Small'
	assert categorize_expense(150) == 'Medium'
	assert categorize_expense(600) == 'Large'

def test_categorize_income():
	assert categorize_income('Salary') == 'Stable'
	assert categorize_income('Rent') == 'Stable'
	assert categorize_income('Dividends') == 'Stable'
	assert categorize_income('Freelance') == 'Variable'
