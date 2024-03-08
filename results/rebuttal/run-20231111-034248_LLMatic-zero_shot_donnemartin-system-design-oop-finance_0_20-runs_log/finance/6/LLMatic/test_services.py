from services import UserService
from models import User
import hashlib

def test_user_service():
	user_service = UserService()
	user = User('Test User', 'test@example.com', 'password')
	assert user_service.generate_savings_tips(user) == 'Save more, spend less!'
	assert user_service.recommend_products(user) == 'Consider investing in stocks.'
	assert user_service.send_notifications(user) == 'You have an upcoming bill due tomorrow.'
	assert user_service.alert_unusual_activity(user) == 'Unusual activity detected in your account.'
	assert user_service.encrypt_user_data(user) == hashlib.sha256(user.password.encode()).hexdigest()
	assert user_service.conduct_security_audit() == 'Security audit conducted successfully.'
	assert user_service.ensure_compliance() == 'Compliance with financial regulations ensured.'

# existing code...
