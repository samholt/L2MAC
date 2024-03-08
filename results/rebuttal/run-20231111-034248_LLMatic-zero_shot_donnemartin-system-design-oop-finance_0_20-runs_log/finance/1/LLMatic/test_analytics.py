import datetime
import analytics


def test_generate_monthly_report():
	user_id = 'user1'
	transactions = [
		{'date': datetime.datetime(2022, 1, 1), 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime(2022, 1, 2), 'amount': 200, 'category': 'utilities'},
		{'date': datetime.datetime(2022, 2, 1), 'amount': 150, 'category': 'groceries'},
		{'date': datetime.datetime(2022, 2, 2), 'amount': 250, 'category': 'utilities'}
	]
	analytics.DB[user_id] = transactions
	report = analytics.generate_monthly_report(user_id)
	assert report == {1: 300, 2: 400}


def test_generate_spending_trends():
	user_id = 'user1'
	transactions = [
		{'date': datetime.datetime(2022, 1, 1), 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime(2022, 1, 2), 'amount': 200, 'category': 'utilities'},
		{'date': datetime.datetime(2022, 2, 1), 'amount': 150, 'category': 'groceries'},
		{'date': datetime.datetime(2022, 2, 2), 'amount': 250, 'category': 'utilities'}
	]
	analytics.DB[user_id] = transactions
	trends = analytics.generate_spending_trends(user_id)
	assert trends == {'groceries': 250, 'utilities': 450}


def test_compare_year_on_year():
	user_id = 'user1'
	transactions = [
		{'date': datetime.datetime(2021, 1, 1), 'amount': 100, 'category': 'groceries'},
		{'date': datetime.datetime(2021, 1, 2), 'amount': 200, 'category': 'utilities'},
		{'date': datetime.datetime(2022, 1, 1), 'amount': 150, 'category': 'groceries'},
		{'date': datetime.datetime(2022, 1, 2), 'amount': 250, 'category': 'utilities'}
	]
	analytics.DB[user_id] = transactions
	comparison = analytics.compare_year_on_year(user_id)
	assert comparison == {2021: 300, 2022: 400}
