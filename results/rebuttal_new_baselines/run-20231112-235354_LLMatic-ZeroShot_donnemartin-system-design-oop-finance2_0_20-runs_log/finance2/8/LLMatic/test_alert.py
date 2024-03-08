import pytest
from models.alert import Alert

def test_create_alert():
	alert = Alert.create_alert('user1', 'type1', 'message1')
	assert alert.user == 'user1'
	assert alert.alert_type == 'type1'
	assert alert.message == 'message1'


def test_get_user_alerts():
	Alert.create_alert('user1', 'type2', 'message2')
	alerts = Alert.get_user_alerts('user1')
	assert len(alerts) == 2
	assert alerts[0].alert_type == 'type1'
	assert alerts[1].alert_type == 'type2'


def test_customize_alert():
	Alert.customize_alert('user1', 'type1', 'new message')
	alerts = Alert.get_user_alerts('user1')
	assert alerts[0].message == 'new message'
