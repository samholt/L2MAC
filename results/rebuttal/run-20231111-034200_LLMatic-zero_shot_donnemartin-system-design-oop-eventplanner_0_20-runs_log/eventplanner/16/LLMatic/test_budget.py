import pytest
from budget import Budget

def test_budget_management():
	budget = Budget()
	budget.set_budget('event1', 1000, {'food': 500, 'decor': 500})
	assert budget.get_budget('event1') == {'total_budget': 1000, 'breakdown': {'food': 500, 'decor': 500}, 'spent': 0}
	assert budget.track_budget('event1', 500) == 'Budget is within limit'
	assert budget.track_budget('event1', 600) == 'Budget overrun'

