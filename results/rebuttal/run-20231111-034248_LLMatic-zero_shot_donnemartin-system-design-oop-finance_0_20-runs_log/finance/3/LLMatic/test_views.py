from views import UserView
from datetime import datetime

def test_user_view():
	user_view = UserView()
	assert user_view.register('test', 'test', 'test@test.com')
	assert user_view.login('test', 'test')
	assert user_view.recover_password('test') == 'Cannot recover password for security reasons.'
	assert 'You are spending more than your income. Try to cut down on unnecessary expenses.' in user_view.view_savings_tips('test')
	assert 'You have a high level of debt. Consider a debt consolidation loan.' in user_view.view_financial_product_recommendations('test')
	assert user_view.send_notifications('test', 'Test notification')
	assert user_view.alert_user('test', 'Test alert')
