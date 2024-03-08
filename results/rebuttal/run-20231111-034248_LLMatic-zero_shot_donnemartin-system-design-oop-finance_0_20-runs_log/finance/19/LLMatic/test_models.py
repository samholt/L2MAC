from models import Category, BankAccount, Transaction, Budget, Investment
from datetime import datetime

def test_category_creation():
	category = Category('testcategory')
	assert category.name == 'testcategory'

def test_transaction_creation():
	transaction = Transaction('Grocery', 100, datetime.now())
	assert transaction.category == 'Grocery'
	assert transaction.amount == 100

def test_bank_account_creation():
	bank_account = BankAccount('12345678', 'Test Bank', 1000)
	assert bank_account.account_number == '12345678'
	assert bank_account.bank_name == 'Test Bank'
	assert bank_account.balance == 1000

def test_budget_creation():
	budget = Budget('Grocery', 500, 'January')
	assert budget.category == 'Grocery'
	assert budget.amount == 500
	assert budget.month == 'January'

def test_investment_creation():
	investment = Investment('Test Investment', 1000, 1500)
	assert investment.name == 'Test Investment'
	assert investment.amount_invested == 1000
	assert investment.current_value == 1500
