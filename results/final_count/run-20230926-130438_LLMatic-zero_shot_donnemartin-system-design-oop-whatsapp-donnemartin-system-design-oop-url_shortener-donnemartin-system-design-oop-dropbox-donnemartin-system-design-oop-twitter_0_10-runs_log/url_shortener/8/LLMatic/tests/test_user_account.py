from services.user_account import UserAccount


def test_create_account():
	user_account = UserAccount()
	assert user_account.create_account('test_user') == 'Account created successfully.'
	assert user_account.create_account('test_user') == 'Username already exists.'


def test_view_urls():
	user_account = UserAccount()
	user_account.create_account('test_user')
	assert user_account.view_urls('test_user') == []
	assert user_account.view_urls('non_existent_user') == 'Username does not exist.'


def test_edit_url():
	user_account = UserAccount()
	user_account.create_account('test_user')
	user_account.users['test_user']['urls'].append('http://test.com')
	assert user_account.edit_url('test_user', 'http://test.com', 'http://newtest.com') == 'URL edited successfully.'
	assert user_account.edit_url('test_user', 'http://nonexistent.com', 'http://newtest.com') == 'URL does not exist.'
	assert user_account.edit_url('non_existent_user', 'http://test.com', 'http://newtest.com') == 'Username does not exist.'


def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('test_user')
	user_account.users['test_user']['urls'].append('http://test.com')
	assert user_account.delete_url('test_user', 'http://test.com') == 'URL deleted successfully.'
	assert user_account.delete_url('test_user', 'http://nonexistent.com') == 'URL does not exist.'
	assert user_account.delete_url('non_existent_user', 'http://test.com') == 'Username does not exist.'


def test_view_analytics():
	user_account = UserAccount()
	user_account.create_account('test_user')
	user_account.users['test_user']['urls'].append({'url': 'http://test.com', 'analytics': {'clicks': 10, 'locations': ['USA', 'UK']}})
	assert user_account.view_analytics('test_user') == {'http://test.com': {'clicks': 10, 'locations': ['USA', 'UK']}}
	assert user_account.view_analytics('non_existent_user') == 'Username does not exist.'
