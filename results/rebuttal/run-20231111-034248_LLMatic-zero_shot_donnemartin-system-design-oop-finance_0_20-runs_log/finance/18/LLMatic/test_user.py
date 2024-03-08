import pytest
from user import User
from account import Account
from transaction import Transaction
from datetime import datetime, timedelta


def test_user():
	user = User('username', 'password', 'email@example.com')
	assert user.username == 'username'
	assert user.authenticate('password')
	assert not user.authenticate('wrong_password')
	assert user.recover_password() == User.hash_password('password')

	assert user.email != 'email@example.com'
	assert user.decrypt_data(user.email) == 'email@example.com'

	user.set_budget('food', 100)
	assert user.check_budget('food') == False

	account = Account()
	transaction1 = Transaction(-50, 'food', 'Grocery shopping', datetime(2022, 1, 1))
	account.transactions.append(transaction1)
	user.accounts.append(account)

	assert user.check_budget('food') == False
	assert user.track_progress('food') == 0.5

	report = user.generate_monthly_report(1, 2022)
	assert report['income'] == 0
	assert report['expenses'] == -50
	assert report['savings'] == 50

	spending = user.visualize_spending_habits()
	assert spending == {'food': 50}

	transaction2 = Transaction(-100, 'food', 'Grocery shopping', datetime(2023, 1, 1))
	account.transactions.append(transaction2)

	comparison = user.compare_year_on_year(2022, 2023)
	assert comparison['income'] == 0
	assert comparison['expenses'] == 50
	assert comparison['savings'] == -50

	tips = user.get_savings_tips()
	assert tips == ['You are overspending on food. Try to cut back.']

	recommendations = user.get_product_recommendations()
	assert recommendations == ['Consider a savings account for food expenses.']

	transaction3 = Transaction(-500, 'rent', 'Rent payment', datetime.now())
	account.transactions.append(transaction3)
	transaction4 = Transaction(-1000, 'car', 'Car payment', datetime.now() + timedelta(days=10))
	account.transactions.append(transaction4)

	notifications = user.get_notifications()
	assert f'Upcoming bill: Car payment for -1000 on {transaction4.date}' in notifications
	assert f'Alert: Unusual activity detected. Large transaction of -500' in notifications

	assert 'Authentication attempt with password: Success' in user.log
	assert 'Password recovery attempt' in user.log
	assert 'Set budget for food: 100' in user.log
	assert 'Checked budget for food' in user.log
	assert 'Tracked progress for food' in user.log
	assert 'Generated monthly report for 1/2022' in user.log
	assert 'Visualized spending habits' in user.log
	assert 'Compared year on year for 2022 and 2023' in user.log
	assert 'Generated savings tips' in user.log
	assert 'Generated product recommendations' in user.log
	assert 'Generated notifications' in user.log

