import pytest
from data import Data

# ... existing tests ...

def test_alerts():
	data = Data()
	data.add_transaction('user1', -600, 'groceries', 12, 2021)
	alerts = data.get_alerts('user1')
	assert len(alerts) == 1
	assert 'Large transaction alert: $-600' in alerts

	data.add_transaction('user1', -400, 'entertainment', 12, 2021)
	alerts = data.get_alerts('user1')
	assert len(alerts) == 1

	data.add_transaction('user1', -700, 'rent', 12, 2021)
	alerts = data.get_alerts('user1')
	assert len(alerts) == 2
	assert 'Large transaction alert: $-700' in alerts

def test_notifications():
	data = Data()
	data.add_notification('user1', 'Bill due: Rent $700')
	notifications = data.get_notifications('user1')
	assert len(notifications) == 1
	assert 'Bill due: Rent $700' in notifications

	data.add_notification('user1', 'Payment received: Salary $2000')
	notifications = data.get_notifications('user1')
	assert len(notifications) == 2
	assert 'Payment received: Salary $2000' in notifications

