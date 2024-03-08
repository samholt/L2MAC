import pytest
from user import User
from account import Account
from transaction import Transaction
import datetime


def test_generate_monthly_report():
	user = User('testuser', 'testpass', 'testemail')
	account = Account('123456', 'Test Bank')
	transaction1 = Transaction(100, 'groceries', datetime.datetime.now(), False, False)
	transaction2 = Transaction(200, 'rent', datetime.datetime.now(), True, False)
	account.transactions.extend([transaction1, transaction2])
	user.accounts.append(account)
	assert user.generate_monthly_report() == {'groceries': 100, 'rent': 200}


def test_generate_yearly_report():
	user = User('testuser', 'testpass', 'testemail')
	account = Account('123456', 'Test Bank')
	transaction1 = Transaction(100, 'groceries', datetime.datetime.now(), False, False)
	transaction2 = Transaction(200, 'rent', datetime.datetime.now(), True, False)
	account.transactions.extend([transaction1, transaction2])
	user.accounts.append(account)
	assert user.generate_yearly_report() == {'groceries': 100, 'rent': 200}


def test_compare_yearly_spending():
	user = User('testuser', 'testpass', 'testemail')
	account = Account('123456', 'Test Bank')
	transaction1 = Transaction(100, 'groceries', datetime.datetime.now().replace(year=datetime.datetime.now().year - 1), False, False)
	transaction2 = Transaction(200, 'rent', datetime.datetime.now(), True, False)
	account.transactions.extend([transaction1, transaction2])
	user.accounts.append(account)
	assert user.compare_yearly_spending(datetime.datetime.now().year - 1, datetime.datetime.now().year) == {'groceries': -100, 'rent': 200}


def test_get_savings_tips():
	user = User('testuser', 'testpass', 'testemail')
	account = Account('123456', 'Test Bank')
	transaction1 = Transaction(1000, 'salary', datetime.datetime.now(), True, True)
	transaction2 = Transaction(700, 'rent', datetime.datetime.now(), False, False)
	account.transactions.extend([transaction1, transaction2])
	user.accounts.append(account)
	assert user.get_savings_tips() == 'You are doing well with your savings. Keep it up!'


def test_recommend_products():
	user = User('testuser', 'testpass', 'testemail')
	account = Account('123456', 'Test Bank')
	transaction1 = Transaction(1000, 'salary', datetime.datetime.now(), True, True)
	transaction2 = Transaction(300, 'rent', datetime.datetime.now(), False, False)
	account.transactions.extend([transaction1, transaction2])
	user.accounts.append(account)
	assert user.recommend_products() == 'You have a high amount of savings. Consider investing in stocks or bonds.'


def test_notifications_and_alerts():
	user = User('testuser', 'testpass', 'testemail')
	user.set_notification('Bill due in 3 days')
	user.set_alert('Unusual account activity detected')
	assert user.get_notifications() == ['Bill due in 3 days']
	assert user.get_alerts() == ['Unusual account activity detected']


def test_conduct_security_audit():
	user = User('testuser', 'testpass', 'testemail')
	assert user.conduct_security_audit() == True
	user.password = user.encrypt_password('password')
	assert user.conduct_security_audit() == False

