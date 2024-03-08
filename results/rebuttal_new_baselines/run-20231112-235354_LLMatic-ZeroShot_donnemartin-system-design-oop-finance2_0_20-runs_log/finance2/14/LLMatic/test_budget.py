import pytest
from models.budget import Budget

def test_create_budget():
	budget = Budget()
	budget_id = budget.create_budget('user1', 1000, 'groceries')
	assert budget_id == 1
	assert budget.budgets[budget_id] == {'user': 'user1', 'amount': 1000, 'category': 'groceries'}

def test_get_user_budgets():
	budget = Budget()
	budget.create_budget('user1', 1000, 'groceries')
	budget.create_budget('user1', 500, 'entertainment')
	budget.create_budget('user2', 2000, 'rent')
	user1_budgets = budget.get_user_budgets('user1')
	assert len(user1_budgets) == 2
	assert {'user': 'user1', 'amount': 1000, 'category': 'groceries'} in user1_budgets
	assert {'user': 'user1', 'amount': 500, 'category': 'entertainment'} in user1_budgets

def test_adjust_budget():
	budget = Budget()
	budget_id = budget.create_budget('user1', 1000, 'groceries')
	budget.adjust_budget(budget_id, 1200)
	assert budget.budgets[budget_id]['amount'] == 1200
