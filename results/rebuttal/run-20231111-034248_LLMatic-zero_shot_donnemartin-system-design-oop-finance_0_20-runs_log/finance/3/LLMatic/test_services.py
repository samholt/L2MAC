from services import UserService
from datetime import datetime
import hashlib

def test_user_service():
	user_service = UserService()
	assert user_service.create_user('test', 'test', 'test@test.com')
	assert user_service.authenticate_user('test', 'test')
	assert user_service.recover_password('test') == 'Cannot recover password for security reasons.'
	assert 'You are spending more than your income. Try to cut down on unnecessary expenses.' in user_service.provide_savings_tips('test')
	assert 'You have a high level of debt. Consider a debt consolidation loan.' in user_service.recommend_financial_products('test')
	assert user_service.send_notifications('test', 'Test notification')
	assert 'Test notification' in user_service.users['test'].notifications
	assert user_service.alert_user('test', 'Test alert')
	assert 'Test alert' in user_service.users['test'].alerts

	user_service.create_user('weak', '123456', 'weak@test.com')
	user_service.conduct_security_audit()
	assert 'Your password is too weak. Please change it immediately.' in user_service.users['weak'].alerts

	user_service.users['test'].income = 20000
	user_service.ensure_compliance()
	assert 'Your income level requires additional verification. Please contact us immediately.' in user_service.users['test'].alerts
