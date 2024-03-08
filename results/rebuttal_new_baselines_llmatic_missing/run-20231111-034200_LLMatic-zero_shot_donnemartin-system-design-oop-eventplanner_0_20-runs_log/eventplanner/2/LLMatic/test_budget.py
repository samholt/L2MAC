import pytest
from budget import Budget

def test_set_budget():
	budget = Budget()
	budget.set_budget('event1', 1000)
	assert budget.get_budget_status('event1') == {'total': 1000, 'spent': 0, 'categories': {}}

def test_track_budget():
	budget = Budget()
	budget.set_budget('event1', 1000)
	budget.track_budget('event1', 'food', 200)
	assert budget.get_budget_status('event1') == {'total': 1000, 'spent': 200, 'categories': {'food': 200}}

def test_check_budget_overrun():
	budget = Budget()
	budget.set_budget('event1', 1000)
	budget.track_budget('event1', 'food', 200)
	budget.track_budget('event1', 'venue', 900)
	assert budget.check_budget_overrun('event1') == 'Budget overrun'
