import datetime

# Mock database
budget_db = {}


def set_budget(username, amount):
	budget_db[username] = {'budget': amount, 'spent': 0, 'last_updated': datetime.datetime.now()}
	return 'Budget set successfully'


def get_budget(username):
	if username in budget_db:
		return budget_db[username]
	else:
		return 'No budget set'


def update_spending(username, amount):
	if username in budget_db:
		budget_db[username]['spent'] += amount
		budget_db[username]['last_updated'] = datetime.datetime.now()
		return 'Spending updated'
	else:
		return 'No budget set'


def check_budget(username):
	if username in budget_db:
		budget = budget_db[username]['budget']
		spent = budget_db[username]['spent']
		if spent > budget:
			return 'Budget exceeded'
		elif spent > 0.9 * budget:
			return 'Budget close to limit'
		else:
			return 'Budget under control'
	else:
		return 'No budget set'
