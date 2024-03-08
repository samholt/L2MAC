import pytest
from models.alert import Alert

def test_create_alert():
	alert = Alert.create_alert('user1', 'Low balance', 'warning')
	assert alert.user == 'user1'
	assert alert.message == 'Low balance'
	assert alert.alert_type == 'warning'

def test_get_user_alerts():
	alerts = Alert.get_user_alerts('user1')
	assert len(alerts) == 2
	assert alerts[0].user == 'user1'
	assert alerts[0].message == 'Low balance'
	assert alerts[0].alert_type == 'warning'
	assert alerts[1].user == 'user1'
	assert alerts[1].message == 'Transaction alert'
	assert alerts[1].alert_type == 'info'

def test_customize_alert():
	alert = Alert.create_alert('user1', 'Low balance', 'warning')
	alert.customize_alert('New message', 'info')
	assert alert.message == 'New message'
	assert alert.alert_type == 'info'
