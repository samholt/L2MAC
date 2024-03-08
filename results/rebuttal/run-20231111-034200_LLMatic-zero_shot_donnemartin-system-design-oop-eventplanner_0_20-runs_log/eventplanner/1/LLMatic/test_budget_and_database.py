import pytest
from budget import Budget
from database import Database

def test_budget_management():
	db = Database()
	budget = Budget(1000)
	budget.set_category_budget('Food', 500)
	budget.track_spending('Food', 600)
	assert budget.alert_overrun() == 'Alert: Budget overrun in Food!'
	db.add_budget('1', budget)
	retrieved_budget = db.get_budget('1')
	assert retrieved_budget is not None
	assert retrieved_budget.alert_overrun() == 'Alert: Budget overrun in Food!'
