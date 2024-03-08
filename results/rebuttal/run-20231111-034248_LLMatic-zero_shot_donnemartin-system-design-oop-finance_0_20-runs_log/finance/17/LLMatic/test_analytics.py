import datetime
import analytics


def test_generate_monthly_report():
	user_id = 'test_user'
	analytics.user_data[user_id] = {'name': 'Test User'}
	analytics.transaction_data[user_id] = [
		{'date': datetime.datetime.now(), 'type': 'expense', 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime.now(), 'type': 'income', 'amount': 200, 'category': 'salary'}
	]
	
	report = analytics.generate_monthly_report(user_id)
	assert report['total_spent'] == 100
	assert report['total_income'] == 200
	assert report['balance'] == 100


def test_analyze_spending_habits():
	user_id = 'test_user'
	analytics.user_data[user_id] = {'name': 'Test User'}
	analytics.transaction_data[user_id] = [
		{'date': datetime.datetime.now(), 'type': 'expense', 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime.now(), 'type': 'expense', 'amount': 50, 'category': 'entertainment'},
		{'date': datetime.datetime.now(), 'type': 'income', 'amount': 200, 'category': 'salary'}
	]
	
	habits = analytics.analyze_spending_habits(user_id)
	assert habits['groceries'] == 1
	assert habits['entertainment'] == 1


def test_compare_year_on_year():
	user_id = 'test_user'
	analytics.user_data[user_id] = {'name': 'Test User'}
	analytics.transaction_data[user_id] = [
		{'date': datetime.datetime.now() - datetime.timedelta(days=365), 'type': 'expense', 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime.now(), 'type': 'expense', 'amount': 200, 'category': 'groceries'}
	]
	
	comparison = analytics.compare_year_on_year(user_id)
	assert comparison['last_year_spent'] == 100
	assert comparison['this_year_spent'] == 200
	assert comparison['difference'] == 100
