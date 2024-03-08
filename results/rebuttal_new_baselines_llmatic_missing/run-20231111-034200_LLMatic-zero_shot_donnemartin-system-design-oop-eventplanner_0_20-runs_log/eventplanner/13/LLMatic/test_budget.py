import pytest
from budget import Budget

budget_manager = Budget()

def test_set_budget():
	budget_manager.set_budget('event1', 1000)
	assert budget_manager.budgets['event1']['budget'] == 1000

def test_track_budget():
	budget_manager.track_budget('event1', 500)
	assert budget_manager.budgets['event1']['spent'] == 500

def test_alert_overrun():
	budget_manager.track_budget('event1', 600)
	assert budget_manager.alert_overrun('event1') == 'Budget overrun'
