import pytest
from data import Transaction

def test_add_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', {'date': '2021-01-01', 'amount': 100})
	assert transaction.transactions['user1'][0]['amount'] == 100

def test_generate_monthly_report():
	transaction = Transaction()
	transaction.add_transaction('user1', {'date': '2021-01-01', 'amount': 100})
	report = transaction.generate_monthly_report('user1')
	assert report[1]['income'] == 100

def test_generate_yearly_report():
	transaction = Transaction()
	transaction.add_transaction('user1', {'date': '2021-01-01', 'amount': 100})
	report = transaction.generate_yearly_report('user1')
	assert report[2021]['income'] == 100

def test_compare_yearly_data():
	transaction = Transaction()
	transaction.add_transaction('user1', {'date': '2021-01-01', 'amount': 100})
	transaction.add_transaction('user1', {'date': '2022-01-01', 'amount': 200})
	transaction.generate_yearly_report('user1')
	comparison = transaction.compare_yearly_data('user1', 2021, 2022)
	assert comparison['year1']['income'] == 100
	assert comparison['year2']['income'] == 200

def test_add_investment():
	transaction = Transaction()
	transaction.add_investment('user1', {'id': 'inv1', 'amount': 1000, 'return': 10})
	assert transaction.investments['user1'][0]['amount'] == 1000

def test_calculate_investment_performance():
	transaction = Transaction()
	transaction.add_investment('user1', {'id': 'inv1', 'amount': 1000, 'return': 10})
	performance = transaction.calculate_investment_performance('user1', 'inv1')
	assert performance == 1100

def test_set_investment_alert():
	transaction = Transaction()
	transaction.add_investment('user1', {'id': 'inv1', 'amount': 1000, 'return': 10})
	transaction.set_investment_alert('user1', 'inv1', 1100)
	assert transaction.investment_alerts['user1']['inv1'] == 1100

def test_check_investment_alerts():
	transaction = Transaction()
	transaction.add_investment('user1', {'id': 'inv1', 'amount': 1000, 'return': 10})
	transaction.set_investment_alert('user1', 'inv1', 1100)
	alerts = transaction.check_investment_alerts('user1')
	assert alerts[0]['investment_id'] == 'inv1'

def test_set_notification():
	transaction = Transaction()
	transaction.set_notification('user1', 'Bill due soon')
	assert transaction.notifications['user1'][0] == 'Bill due soon'

def test_get_notifications():
	transaction = Transaction()
	transaction.set_notification('user1', 'Bill due soon')
	notifications = transaction.get_notifications('user1')
	assert notifications[0] == 'Bill due soon'

def test_set_alert():
	transaction = Transaction()
	transaction.set_alert('user1', 'Unusual account activity detected')
	assert transaction.alerts['user1'][0] == 'Unusual account activity detected'

def test_get_alerts():
	transaction = Transaction()
	transaction.set_alert('user1', 'Unusual account activity detected')
	alerts = transaction.get_alerts('user1')
	assert alerts[0] == 'Unusual account activity detected'

