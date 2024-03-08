import pytest
from budget_management import Budget

def test_budget_management():
	budget = Budget(1000, {'Food': 500, 'Decorations': 500})
	budget.set_budget(2000, {'Food': 1000, 'Decorations': 1000})
	assert budget.total_budget == 2000
	assert budget.breakdown == {'Food': 1000, 'Decorations': 1000}
	budget.update_budget('Food', 500)
	assert budget.breakdown['Food'] == 1500
	budget.track_usage('Food', 1600)
	assert budget.usage['Food'] == 1600
