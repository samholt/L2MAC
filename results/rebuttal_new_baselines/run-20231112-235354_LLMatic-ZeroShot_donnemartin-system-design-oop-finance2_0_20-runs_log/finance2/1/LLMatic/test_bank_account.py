from models.user import User


def test_add_bank_account():
	user = User('username', 'password', 'email')
	user.add_bank_account('Bank', '123456', 1000)
	assert len(user.bank_accounts) == 1
	assert user.bank_accounts['123456'].bank_name == 'Bank'


def test_update_bank_account():
	user = User('username', 'password', 'email')
	user.add_bank_account('Bank', '123456', 1000)
	user.update_bank_account('123456', new_bank_name='New Bank', new_balance=2000)
	assert user.bank_accounts['123456'].bank_name == 'New Bank'
	assert user.bank_accounts['123456'].balance == 2000


def test_delete_bank_account():
	user = User('username', 'password', 'email')
	user.add_bank_account('Bank', '123456', 1000)
	user.delete_bank_account('123456')
	assert len(user.bank_accounts) == 0
