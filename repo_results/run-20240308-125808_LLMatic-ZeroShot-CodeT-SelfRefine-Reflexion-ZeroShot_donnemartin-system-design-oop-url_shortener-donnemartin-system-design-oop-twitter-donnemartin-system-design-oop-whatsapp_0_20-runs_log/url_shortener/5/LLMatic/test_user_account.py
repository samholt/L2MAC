from user_account import UserAccount

def test_user_account():
	user_account = UserAccount()

	# Test creating account
	assert user_account.create_account('test', 'password') == 'Account created successfully'
	assert user_account.create_account('test', 'password') == 'Username already exists'

	# Test viewing URLs
	assert user_account.view_urls('test') == []
	assert user_account.view_urls('nonexistent') == 'Username does not exist'

	# Test editing URLs
	user_account.accounts['test']['urls'].append('http://example.com')
	assert user_account.edit_url('test', 'http://example.com', 'http://newexample.com') == 'URL edited successfully'
	assert user_account.edit_url('test', 'http://nonexistent.com', 'http://newexample.com') == 'URL does not exist'
	assert user_account.edit_url('nonexistent', 'http://example.com', 'http://newexample.com') == 'Username does not exist'

	# Test deleting URLs
	assert user_account.delete_url('test', 'http://newexample.com') == 'URL deleted successfully'
	assert user_account.delete_url('test', 'http://nonexistent.com') == 'URL does not exist'
	assert user_account.delete_url('nonexistent', 'http://example.com') == 'Username does not exist'

	# Test viewing analytics
	assert user_account.view_analytics('test') == {}
	assert user_account.view_analytics('nonexistent') == 'Username does not exist'

	# Test deleting user
	assert user_account.delete_user('test') == 'User deleted successfully'
	assert user_account.delete_user('nonexistent') == 'Username does not exist'

	# Test get_all_users
	assert isinstance(user_account.get_all_users(), dict)
