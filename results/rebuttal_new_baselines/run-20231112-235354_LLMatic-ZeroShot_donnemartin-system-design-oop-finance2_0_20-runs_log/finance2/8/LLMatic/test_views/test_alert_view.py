from views.alert_view import AlertView


def test_create_alert():
	alert = AlertView.create_alert('user1', 'low_balance', 'Your balance is low.')
	assert alert.user == 'user1'
	assert alert.alert_type == 'low_balance'
	assert alert.message == 'Your balance is low.'


def test_get_user_alerts():
	AlertView.create_alert('user1', 'low_balance', 'Your balance is low.')
	AlertView.create_alert('user1', 'high_spending', 'Your spending is high.')
	alerts = AlertView.get_user_alerts('user1')
	assert len(alerts) == 2
	assert alerts[0].user == 'user1'
	assert alerts[0].alert_type == 'low_balance'
	assert alerts[0].message == 'Your balance is low.'
	assert alerts[1].user == 'user1'
	assert alerts[1].alert_type == 'high_spending'
	assert alerts[1].message == 'Your spending is high.'


def test_customize_alert():
	AlertView.create_alert('user1', 'low_balance', 'Your balance is low.')
	AlertView.customize_alert('user1', 'low_balance', 'Your balance is critically low.')
	alerts = AlertView.get_user_alerts('user1')
	assert alerts[0].message == 'Your balance is critically low.'
