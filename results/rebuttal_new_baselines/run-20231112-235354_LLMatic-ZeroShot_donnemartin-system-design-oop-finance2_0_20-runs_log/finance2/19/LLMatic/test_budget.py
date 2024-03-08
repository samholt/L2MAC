import pytest
from budget import Budget

def test_budget():
	budget = Budget()
	budget.set_budget(1000)
	assert budget.budget == 1000

	budget.adjust_budget(500)
	assert budget.budget == 1500

	budget.add_expense(100)
	budget.add_expense(200)
	budget.add_expense(300)
	assert budget.check_budget() == 'You are within your budget limit.'

	budget.add_expense(1000)
	assert budget.check_budget() == 'Warning: You are nearing your budget limit.'

	assert budget.analyze_expenses() == 'Your budget is well balanced.'

	budget.add_expense(500)
	assert budget.analyze_expenses() == 'Your budget is well balanced.'

	budget.add_expense(500)
	budget.add_expense(500)
	assert budget.analyze_expenses() == 'Consider adjusting your budget.'
