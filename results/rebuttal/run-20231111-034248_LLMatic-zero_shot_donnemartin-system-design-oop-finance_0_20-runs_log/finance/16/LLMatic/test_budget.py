import pytest
from budget import Budget
from user import User
from transaction import Transaction


def test_set_budget():
	user = User('test_user', 'password')
	budget = Budget(user)
	assert budget.set_budget('groceries', 200) == 'Budget set successfully'
	assert budget.categories['groceries'] == 200


def test_alert_user():
	user = User('test_user', 'password')
	budget = Budget(user)
	budget.set_budget('groceries', 200)
	transaction = Transaction(user, 200, 'groceries', 'expense')
	user.transactions.append(transaction)
	assert budget.alert_user('groceries') == 'Alert! You have reached or exceeded your budget limit for groceries'


def test_track_progress():
	user = User('test_user', 'password')
	budget = Budget(user)
	budget.goals['new car'] = 5000
	user.balance = 5000
	assert budget.track_progress('new car') == 'Congratulations! You have reached your financial goal for new car'
