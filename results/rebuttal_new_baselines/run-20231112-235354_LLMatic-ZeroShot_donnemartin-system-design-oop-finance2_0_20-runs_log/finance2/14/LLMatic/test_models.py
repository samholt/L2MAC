import unittest
import models.user
import models.transaction
import models.budget
import models.investment
import models.alert

def test_user():
	user = models.user.User('test', 'test@test.com', 'password')
	assert user.name == 'test'
	assert user.email == 'test@test.com'
	assert user.authenticate('password')

def test_transaction():
	transaction = models.transaction.Transaction('test', 100, 'groceries')
	assert transaction.user == 'test'
	assert transaction.amount == 100
	assert transaction.category == 'groceries'

def test_budget():
	budget = models.budget.Budget()
	budget_id = budget.create_budget('test', 1000, 'groceries')
	assert budget.budgets[budget_id] == {'user': 'test', 'amount': 1000, 'category': 'groceries'}

def test_investment():
	investment = models.investment.Investment('test', 1000, 'stock')
	assert investment.user == 'test'
	assert investment.amount == 1000
	assert investment.type == 'stock'

def test_alert():
	alert = models.alert.Alert('test', 'Alert message', 'warning')
	assert alert.user == 'test'
	assert alert.message == 'Alert message'
	assert alert.alert_type == 'warning'
