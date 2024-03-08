from services import UserService
from models import Category, BankAccount, Transaction, Budget, Investment
from datetime import datetime

def test_user_service():
	user_service = UserService()
	assert user_service.create_user('testuser', 'testpassword', 'testemail') == 'User created successfully'
	assert user_service.authenticate_user('testuser', 'testpassword') == 'User authenticated'
	assert user_service.recover_password('testuser') == user_service.encrypt_password('testpassword')
	assert user_service.get_savings_tips('testuser') == ['Consider saving more money']
	assert user_service.get_product_recommendations('testuser') == ['Consider a high-interest savings account']

	# Create a bank account for the user
	bank_account = BankAccount('12345678', 'Test Bank', 1000)
	# Add transactions to the bank account
	bank_account.add_transaction(Transaction('Bill', 600, datetime.now()))
	bank_account.add_transaction(Transaction('Grocery', 200, datetime.now()))
	user_service.users['testuser'].bank_account = bank_account

	# Test notifications and alerts
	assert user_service.send_notifications('testuser') == ['Large transaction alert']
	assert user_service.send_alerts('testuser') == []

	# Add a large transaction to trigger a fraud alert
	bank_account.add_transaction(Transaction('Travel', 1500, datetime.now()))
	assert user_service.send_alerts('testuser') == ['Potential fraud alert']

	# Test security audit
	assert user_service.conduct_security_audit('testuser') == 'No unusual activity detected'
	# Add a very large transaction to trigger a security audit
	bank_account.add_transaction(Transaction('Property', 6000, datetime.now()))
	assert user_service.conduct_security_audit('testuser') == 'Unusual activity detected'
