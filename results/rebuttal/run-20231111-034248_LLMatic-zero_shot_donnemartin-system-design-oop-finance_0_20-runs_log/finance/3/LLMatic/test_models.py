from models import User, Transaction, BankAccount, Budget, Investment

def test_user_creation():
	user = User('test', 'test', 'test@test.com')
	assert user.username == 'test'
	assert user.password == 'test'
	assert user.email == 'test@test.com'

def test_transaction_creation():
	transaction = Transaction(100, 'groceries', '2022-01-01')
	assert transaction.amount == 100
	assert transaction.category == 'groceries'
	assert transaction.date == '2022-01-01'

def test_bank_account_creation():
	account = BankAccount('123456', 'Test Bank', 1000)
	assert account.account_number == '123456'
	assert account.bank_name == 'Test Bank'
	assert account.balance == 1000

def test_budget_creation():
	budget = Budget('groceries', 500)
	assert budget.category == 'groceries'
	assert budget.limit == 500
	assert budget.progress == 0

def test_investment_creation():
	investment = Investment('stocks', 1000, 1000)
	assert investment.investment_type == 'stocks'
	assert investment.amount_invested == 1000
	assert investment.current_value == 1000
