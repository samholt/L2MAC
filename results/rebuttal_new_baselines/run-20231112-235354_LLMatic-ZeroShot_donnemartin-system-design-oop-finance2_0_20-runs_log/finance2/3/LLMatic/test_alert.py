import pytest
from models.alert import Alert

def test_create_alert():
	alert = Alert.create_alert('user1', 'type1', 'message1')
	assert alert.user == 'user1'
	assert alert.alert_type == 'type1'
	assert alert.message == 'message1'

def test_get_user_alerts():
	alerts = Alert.get_user_alerts('user1')
	assert isinstance(alerts, list)

def test_customize_alert():
	alert = Alert('user1', 'type1', 'message1')
	alert.customize_alert('type2', 'message2')
	assert alert.alert_type == 'type2'
	assert alert.message == 'message2'
