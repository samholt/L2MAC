import pytest
from models.budget import Budget

def test_set_budget():
	budget = Budget('user1', 1000, 'groceries')
	budget.set_budget('user1', 2000, 'rent')
	assert budget.get_user_budgets('user1') == [{'user': 'user1', 'amount': 2000, 'category': 'rent'}]

def test_adjust_budget():
	budget = Budget('user1', 1000, 'groceries')
	budget.adjust_budget('user1', 500)
	assert budget.get_user_budgets('user1') == [{'user': 'user1', 'amount': 1500, 'category': 'groceries'}]

def test_get_user_budgets():
	budget = Budget('user1', 1000, 'groceries')
	assert budget.get_user_budgets('user1') == [{'user': 'user1', 'amount': 1000, 'category': 'groceries'}]
