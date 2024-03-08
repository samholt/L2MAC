from security import Security

def test_security():
	security = Security()

	user_data = {}
	transaction_data = {}

	assert security.protect_user_data(user_data) == True
	assert security.maintain_privacy(user_data) == True
	assert security.secure_transaction(transaction_data) == True
