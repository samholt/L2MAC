import pytest
from budget import Budget

def test_budget():
	budget = Budget()
	user_id = 'user1'
	budget.set_monthly_budget(user_id, 1000)
	budget_info = budget.get_budget_info(user_id)
	assert budget_info['monthly_budget'] == 1000
	assert budget_info['current_spending'] == 0

	budget.add_expense(user_id, 900)
	budget_info = budget.get_budget_info(user_id)
	assert budget_info['current_spending'] == 900

	budget.add_expense(user_id, 200)
	budget_info = budget.get_budget_info(user_id)
	assert budget_info['current_spending'] == 0

	budget.set_monthly_budget(user_id, 2000)
	budget_info = budget.get_budget_info(user_id)
	assert budget_info['monthly_budget'] == 2000
	assert budget_info['current_spending'] == 0
