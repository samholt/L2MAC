import pytest
from budget import Budget

def test_set_budget():
	budget = Budget()
	budget.set_budget('event1', 1000)
	assert budget.get_budget_status('event1') == {'budget': 1000, 'spent': 0}

def test_track_budget():
	budget = Budget()
	budget.set_budget('event2', 2000)
	assert budget.track_budget('event2', 500) == 'Budget is under control'
	assert budget.track_budget('event2', 2000) == 'Budget overrun'

def test_get_budget_status():
	budget = Budget()
	budget.set_budget('event3', 3000)
	budget.track_budget('event3', 1500)
	assert budget.get_budget_status('event3') == {'budget': 3000, 'spent': 1500}
