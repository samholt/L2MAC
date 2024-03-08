from services import UserService, BankAccountService

def test_user_service():
	user_service = UserService()
	user = user_service.create_user('test', 'password', 'test@test.com')
	assert user.username == 'test'
	assert user.password == 'password'
	assert user.email == 'test@test.com'

	updated_user = user_service.update_user('test', 'new_password', 'new@test.com')
	assert updated_user.password == 'new_password'
	assert updated_user.email == 'new@test.com'

	assert user_service.delete_user('test') == True
	assert user_service.delete_user('test') == False

	user_service.create_user('test', 'password', 'test@test.com')
	otp = user_service.generate_otp('test')
	assert otp is not None
	assert len(otp) == 6
	assert user_service.verify_otp('test', otp) == True
	assert user_service.verify_otp('test', otp) == False

def test_bank_account_service():
	bank_account_service = BankAccountService()
	bank_account = bank_account_service.link_bank_account('123456', 'Bank', 'test')
	assert bank_account.account_number == '123456'
	assert bank_account.bank_name == 'Bank'
	assert bank_account.user_id == 'test'

	updated_bank_account = bank_account_service.update_bank_account('123456', 'New Bank')
	assert updated_bank_account.bank_name == 'New Bank'

	assert bank_account_service.unlink_bank_account('123456') == True
	assert bank_account_service.unlink_bank_account('123456') == False
