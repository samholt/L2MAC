from views.budget_view import BudgetView


def test_set_budget():
	budget = BudgetView.set_budget('user1', 1000, 'groceries')
	assert budget.budgets['user1']['amount'] == 1000
	assert budget.budgets['user1']['category'] == 'groceries'


def test_adjust_budget():
	budget = BudgetView.set_budget('user1', 1000, 'groceries')
	BudgetView.adjust_budget('user1', 200, 'groceries')
	assert budget.budgets['user1']['amount'] == 1200


def test_get_budgets():
	budget = BudgetView.set_budget('user1', 1000, 'groceries')
	user_budget = BudgetView.get_budgets('user1', 1000, 'groceries')
	assert user_budget['amount'] == 1000
	assert user_budget['category'] == 'groceries'
