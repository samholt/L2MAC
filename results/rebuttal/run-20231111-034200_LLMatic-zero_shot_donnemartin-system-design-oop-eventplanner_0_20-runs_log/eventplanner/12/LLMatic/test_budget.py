import pytest
from budget import Budget

def test_set_budget():
	budget = Budget()
	budget.set_budget(1000, {'food': 500, 'decor': 500})
	assert budget.total_budget == 1000
	assert budget.category_budget == {'food': 500, 'decor': 500}

def test_track_expense():
	budget = Budget()
	budget.set_budget(1000, {'food': 500, 'decor': 500})
	budget.track_expense('food', 200)
	assert budget.expenses == {'food': 200}

def test_check_budget():
	budget = Budget()
	budget.set_budget(1000, {'food': 500, 'decor': 500})
	budget.track_expense('food', 600)
	budget.track_expense('decor', 600)
	assert budget.check_budget() == 'Budget Overrun'
