import pytest
from models.alert import Alert


def test_create_alert():
	Alert.alerts = []
	alert = Alert.create_alert('user1', 'nearing budget limit', 'You are nearing your budget limit')
	assert alert.user == 'user1'
	assert alert.alert_type == 'nearing budget limit'
	assert alert.message == 'You are nearing your budget limit'


def test_get_user_alerts():
	Alert.alerts = []
	Alert.create_alert('user1', 'nearing budget limit', 'You are nearing your budget limit')
	Alert.create_alert('user1', 'unusual spending', 'Your spending is unusual')
	alerts = Alert.get_user_alerts('user1')
	assert len(alerts) == 2
	assert alerts[0].user == 'user1'
	assert alerts[1].user == 'user1'
