from views import UserView, BankAccountView

def test_user_view():
	user_view = UserView()
	user = user_view.create_user('test', 'password', 'test@test.com')
	assert user.username == 'test'
	assert user.password == 'password'
	assert user.email == 'test@test.com'

	updated_user = user_view.update_user('test', 'new_password', 'new@test.com')
	assert updated_user.password == 'new_password'
	assert updated_user.email == 'new@test.com'

	assert user_view.delete_user('test') == True
	assert user_view.delete_user('test') == False

	user_view.create_user('test', 'password', 'test@test.com')
	otp = user_view.generate_otp('test')
	assert otp is not None
	assert len(otp) == 6
	assert user_view.verify_otp('test', otp) == True
	assert user_view.verify_otp('test', otp) == False

def test_bank_account_view():
	bank_account_view = BankAccountView()
	bank_account = bank_account_view.link_bank_account('123456', 'Bank', 'test')
	assert bank_account.account_number == '123456'
	assert bank_account.bank_name == 'Bank'
	assert bank_account.user_id == 'test'

	updated_bank_account = bank_account_view.update_bank_account('123456', 'New Bank')
	assert updated_bank_account.bank_name == 'New Bank'

	assert bank_account_view.unlink_bank_account('123456') == True
	assert bank_account_view.unlink_bank_account('123456') == False
