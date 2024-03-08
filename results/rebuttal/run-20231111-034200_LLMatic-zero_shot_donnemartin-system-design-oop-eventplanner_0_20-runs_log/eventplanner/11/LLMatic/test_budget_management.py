import pytest
from budget_management import BudgetManagement

def test_set_and_get_budget():
	bm = BudgetManagement()
	bm.set_budget('event1', 1000)
	status = bm.get_budget_status('event1')
	assert status['budget'] == 1000
	assert status['spent'] == 0
	assert status['remaining'] == 1000

def test_track_budget():
	bm = BudgetManagement()
	bm.set_budget('event1', 1000)
	bm.track_budget('event1', 200)
	status = bm.get_budget_status('event1')
	assert status['spent'] == 200
	assert status['remaining'] == 800

def test_check_budget_overrun():
	bm = BudgetManagement()
	bm.set_budget('event1', 1000)
	bm.track_budget('event1', 1200)
	assert bm.check_budget_overrun('event1') == True
