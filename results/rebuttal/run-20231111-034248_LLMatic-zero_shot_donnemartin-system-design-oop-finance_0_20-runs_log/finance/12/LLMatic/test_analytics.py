import analytics
import datetime


def test_generate_monthly_report():
	user_data = {
		'1': {
			'transactions': [
				{'type': 'income', 'amount': 1000, 'date': datetime.datetime.now()},
				{'type': 'expense', 'amount': 500, 'date': datetime.datetime.now()}
			]
		}
	}
	analytics.user_data = user_data
	
	report = analytics.generate_monthly_report('1')
	assert report['income'] == 1000
	assert report['expenses'] == 500
	assert report['net'] == 500


def test_generate_spending_trends():
	user_data = {
		'1': {
			'transactions': [
				{'type': 'expense', 'amount': 500, 'category': 'food', 'date': datetime.datetime.now()},
				{'type': 'expense', 'amount': 300, 'category': 'transport', 'date': datetime.datetime.now()}
			]
		}
	}
	analytics.user_data = user_data
	
	trends = analytics.generate_spending_trends('1')
	assert trends['food'] == 500
	assert trends['transport'] == 300


def test_compare_year_on_year():
	user_data = {
		'1': {
			'transactions': [
				{'type': 'income', 'amount': 1000, 'date': datetime.datetime(2020, 1, 1)},
				{'type': 'expense', 'amount': 500, 'date': datetime.datetime(2020, 1, 1)},
				{'type': 'income', 'amount': 2000, 'date': datetime.datetime(2021, 1, 1)},
				{'type': 'expense', 'amount': 1000, 'date': datetime.datetime(2021, 1, 1)}
			]
		}
	}
	analytics.user_data = user_data
	
	comparison = analytics.compare_year_on_year('1', 2020, 2021)
	assert comparison['year1']['income'] == 1000
	assert comparison['year1']['expenses'] == 500
	assert comparison['year1']['net'] == 500
	assert comparison['year2']['income'] == 2000
	assert comparison['year2']['expenses'] == 1000
	assert comparison['year2']['net'] == 1000
