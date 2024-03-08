import pytest
from budget import Budget

def test_budget():
	budget = Budget()
	budget.set_budget('Groceries', 500)
	assert budget.get_budget('Groceries') == 500
	budget.adjust_budget('Groceries', 100)
	assert budget.get_budget('Groceries') == 600
	assert 'Low budget alert for Groceries!' not in budget.alert()
	budget.adjust_budget('Groceries', -550)
	assert 'Low budget alert for Groceries!' in budget.alert()
	expenses = {'Groceries': 700}
	budget.analyze_spending(expenses)
	assert budget.get_budget('Groceries') == 800
