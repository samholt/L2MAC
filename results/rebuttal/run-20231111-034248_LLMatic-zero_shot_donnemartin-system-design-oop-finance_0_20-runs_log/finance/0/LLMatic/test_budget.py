import budget


def test_set_budget():
	assert budget.set_budget('test_user', 1000) == 'Budget set successfully'
	budget_info = budget.get_budget('test_user')
	assert budget_info['budget'] == 1000
	assert budget_info['spent'] == 0


def test_update_spending():
	assert budget.update_spending('test_user', 500) == 'Spending updated'
	budget_info = budget.get_budget('test_user')
	assert budget_info['spent'] == 500


def test_check_budget():
	assert budget.check_budget('test_user') == 'Budget under control'
	assert budget.update_spending('test_user', 500) == 'Spending updated'
	assert budget.check_budget('test_user') == 'Budget close to limit'
	assert budget.update_spending('test_user', 100) == 'Spending updated'
	assert budget.check_budget('test_user') == 'Budget exceeded'
