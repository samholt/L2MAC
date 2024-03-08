from models.user import User
from models.bank_account import BankAccount
from models.transaction import Transaction
from models.budget import Budget


def test_user():
	user = User('test', 'test', 'test@test.com')
	assert user.username == 'test'
	assert user.password == 'test'
	assert user.email == 'test@test.com'


def test_bank_account():
	bank_account = BankAccount('test_bank', '123456', 1000)
	assert bank_account.bank_name == 'test_bank'
	assert bank_account.account_number == '123456'
	assert bank_account.balance == 1000


def test_transaction():
	transaction = Transaction('test', 100, '2022-01-01', 'test_category', 'test_type')
	assert transaction.user_id == 'test'
	assert transaction.amount == 100
	assert transaction.date == '2022-01-01'
	assert transaction.category == 'test_category'
	assert transaction.type == 'test_type'


def test_budget():
	budget = Budget('test', 1000, 'January')
	assert budget.user_id == 'test'
	assert budget.amount == 1000
	assert budget.month == 'January'
