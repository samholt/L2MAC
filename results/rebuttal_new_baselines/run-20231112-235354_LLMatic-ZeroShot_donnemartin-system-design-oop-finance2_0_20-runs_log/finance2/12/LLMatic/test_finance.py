from finance import Finance

def test_add_expense():
	finance = Finance()
	finance.add_expense('user1', 'expense1')
	assert finance.expenses['user1'] == ['expense1']

def test_add_income():
	finance = Finance()
	finance.add_income('user1', 'income1')
	assert finance.incomes['user1'] == ['income1']

def test_import_expenses():
	finance = Finance()
	finance.import_expenses('user1', ['expense1', 'expense2'])
	assert finance.expenses['user1'] == ['expense1', 'expense2']

def test_import_incomes():
	finance = Finance()
	finance.import_incomes('user1', ['income1', 'income2'])
	assert finance.incomes['user1'] == ['income1', 'income2']

def test_categorize_expense():
	finance = Finance()
	finance.categorize_expense('user1', 'expense1', 'category1')
	assert finance.expense_categories['user1']['expense1'] == 'category1'

def test_categorize_income():
	finance = Finance()
	finance.categorize_income('user1', 'income1', 'category1')
	assert finance.income_categories['user1']['income1'] == 'category1'
