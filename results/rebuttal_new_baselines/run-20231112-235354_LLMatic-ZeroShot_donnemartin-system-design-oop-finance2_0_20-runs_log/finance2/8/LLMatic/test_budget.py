import pytest
from models.budget import Budget

def test_budget():
	budget = Budget('user1', 1000, 'groceries')
	budget.set_budget('user1', 2000, 'rent')
	assert budget.get_budgets('user1') == {'amount': 2000, 'category': 'rent'}
	budget.adjust_budget('user1', 500)
	assert budget.get_budgets('user1') == {'amount': 2500, 'category': 'rent'}
