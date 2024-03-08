import pytest
from account import Account
from transaction import Transaction

def test_account_creation():
	account = Account('123456', 'Bank of ChatGPT')
	assert account.account_number == '123456'
	assert account.bank_name == 'Bank of ChatGPT'
	assert account.balance == 0
	assert account.transactions == []

def test_link_account():
	account = Account('123456', 'Bank of ChatGPT')
	account.link_account('654321', 'ChatGPT Bank')
	assert account.account_number == '654321'
	assert account.bank_name == 'ChatGPT Bank'

def test_import_transactions():
	account = Account('123456', 'Bank of ChatGPT')
	transactions = [Transaction(100, 'groceries', '2022-01-01', False, False), Transaction(-50, 'groceries', '2022-01-02', False, False)]
	account.import_transactions(transactions)
	assert account.transactions == transactions
	assert account.balance == 50
