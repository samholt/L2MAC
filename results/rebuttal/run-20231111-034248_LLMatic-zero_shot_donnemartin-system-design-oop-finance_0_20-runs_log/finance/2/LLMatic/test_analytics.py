import pytest
from analytics import Analytics

def test_analytics():
	analytics = Analytics()
	analytics.add_monthly_report('user1', 'January', 'report1')
	assert analytics.get_monthly_report('user1', 'January') == 'report1'
	assert analytics.get_monthly_report('user1', 'February') == 'No report found'
	analytics.add_yearly_report('user1', '2021', 'report2')
	assert analytics.get_yearly_report('user1', '2021') == 'report2'
	assert analytics.get_yearly_report('user1', '2022') == 'No report found'
	analytics.add_spending_habits('user1', 'habits1')
	assert analytics.get_spending_habits('user1') == 'habits1'
	assert analytics.get_spending_habits('user2') == 'No habits found'
