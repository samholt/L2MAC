import pytest
from budget import Budget

def test_set_budget():
	budget = Budget()
	budget.set_budget('event1', 1000)
	assert budget.budget_data['event1'] == {'budget': 1000, 'spent': 0}

def test_track_budget():
	budget = Budget()
	budget.set_budget('event1', 1000)
	budget.track_budget('event1', 200)
	assert budget.budget_data['event1'] == {'budget': 1000, 'spent': 200}

def test_alert_overrun():
	budget = Budget()
	budget.set_budget('event1', 1000)
	budget.track_budget('event1', 1200)
	assert budget.alert_overrun('event1') == 'Budget overrun'
