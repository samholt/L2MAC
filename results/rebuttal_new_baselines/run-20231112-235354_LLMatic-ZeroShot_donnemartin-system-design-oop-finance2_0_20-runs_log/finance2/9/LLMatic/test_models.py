import pytest
from models.alert import Alert


def test_alert():
	alert = Alert('user1', 'type1', 'message1')
	assert alert.user == 'user1'
	assert alert.alert_type == 'type1'
	assert alert.message == 'message1'

	report = alert.generate_financial_report()
	assert report == {'report': 'This is a financial report'}

	alert.set_custom_alert('type2', 'message2')
	assert alert.alert_type == 'type2'
	assert alert.message == 'message2'

	status = alert.send_alert()
	assert status == {'status': 'Alert sent'}
