import pytest
from investment import Investment

investment = Investment()

user_id = 'user1'
investment_data = {'id': 'inv1', 'amount': 1000, 'current_value': 1200}


def test_add_investment():
	response = investment.add_investment(user_id, investment_data)
	assert response['status'] == 'success'


def test_track_investment():
	response = investment.track_investment(user_id)
	assert response['status'] == 'success'
	assert response['data'] == [investment_data]


def test_calculate_performance():
	response = investment.calculate_performance(user_id)
	assert response['status'] == 'success'
	assert response['data']['total_investment'] == 1000
	assert response['data']['total_value'] == 1200
	assert response['data']['performance'] == 0.2


def test_set_alert():
	response = investment.set_alert(user_id, 'inv1', 1500)
	assert response['status'] == 'success'
	response = investment.track_investment(user_id)
	assert response['data'][0]['alert_value'] == 1500
