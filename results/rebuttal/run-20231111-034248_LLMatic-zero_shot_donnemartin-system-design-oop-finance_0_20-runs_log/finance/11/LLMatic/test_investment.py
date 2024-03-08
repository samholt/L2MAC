import pytest
from data import Transaction

def test_investment():
	transaction = Transaction()
	user_id = 'user1'
	investment = {'id': 1, 'amount': 1000, 'return': 5}
	updated_investment = {'id': 1, 'amount': 2000, 'return': 5}
	alert_threshold = 1050

	# Test adding investment
	transaction.add_investment(user_id, investment)
	assert transaction.investments[user_id][0] == investment

	# Test updating investment
	transaction.add_investment(user_id, updated_investment)
	assert transaction.investments[user_id][1] == updated_investment

	# Test calculating investment performance
	assert transaction.calculate_investment_performance(user_id, investment['id']) == investment['amount'] * (1 + investment['return'] / 100)

	# Test setting investment alert
	transaction.set_investment_alert(user_id, updated_investment['id'], alert_threshold)
	assert transaction.investment_alerts[user_id][updated_investment['id']] == alert_threshold

	# Test checking investment alerts
	alerts = transaction.check_investment_alerts(user_id)
	assert len(alerts) == 1
	assert alerts[0]['investment_id'] == updated_investment['id']
	assert alerts[0]['message'] == 'Investment has reached alert threshold'
