import mock_db
import datetime

def test_add_user():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	assert db.get_user('test@test.com') is not None


def test_get_user():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	assert db.get_user('test@test.com', 'password') is not None


def test_set_user_picture():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.set_user_picture('test@test.com', 'picture')
	assert db.get_user('test@test.com')['picture'] == 'picture'


def test_set_user_status_message():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.set_user_status_message('test@test.com', 'status')
	assert db.get_user('test@test.com')['status'] == 'status'


def test_update_user_privacy_settings():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.update_user_privacy_settings('test@test.com', 'private')
	assert db.get_user('test@test.com')['privacy'] == 'private'


def test_block_contact():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.add_user('contact@test.com', 'password')
	db.block_contact('test@test.com', 'contact@test.com')
	assert 'contact@test.com' in db.get_user('test@test.com')['blocked']


def test_unblock_contact():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.add_user('contact@test.com', 'password')
	db.block_contact('test@test.com', 'contact@test.com')
	db.unblock_contact('test@test.com', 'contact@test.com')
	assert 'contact@test.com' not in db.get_user('test@test.com')['blocked']


def test_create_group():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.create_group('test@test.com', 'group', ['member@test.com'])
	assert db.get_group('group') is not None


def test_edit_group():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.create_group('test@test.com', 'group', ['member@test.com'])
	db.edit_group('test@test.com', 'group', ['new_member@test.com'])
	assert 'new_member@test.com' in db.get_group('group')['members']


def test_add_group_admin():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.create_group('test@test.com', 'group', ['member@test.com'])
	db.add_group_admin('test@test.com', 'group', 'admin@test.com')
	assert 'admin@test.com' in db.get_group('group')['admins']


def test_remove_group_admin():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.create_group('test@test.com', 'group', ['member@test.com'])
	db.add_group_admin('test@test.com', 'group', 'admin@test.com')
	db.remove_group_admin('test@test.com', 'group', 'admin@test.com')
	assert 'admin@test.com' not in db.get_group('group')['admins']


def test_add_offline_message():
	db = mock_db.MockDB()
	db.add_user('sender@test.com', 'password')
	db.add_user('recipient@test.com', 'password')
	db.add_offline_message('sender@test.com', 'recipient@test.com', 'Hello')
	assert db.get_offline_messages('recipient@test.com') != []


def test_get_offline_messages():
	db = mock_db.MockDB()
	db.add_user('sender@test.com', 'password')
	db.add_user('recipient@test.com', 'password')
	db.add_offline_message('sender@test.com', 'recipient@test.com', 'Hello')
	assert db.get_offline_messages('recipient@test.com')[0]['text'] == 'Hello'


def test_clear_offline_messages():
	db = mock_db.MockDB()
	db.add_user('sender@test.com', 'password')
	db.add_user('recipient@test.com', 'password')
	db.add_offline_message('sender@test.com', 'recipient@test.com', 'Hello')
	db.clear_offline_messages('recipient@test.com')
	assert db.get_offline_messages('recipient@test.com') == []


def test_update_last_activity():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.update_last_activity('test@test.com')
	assert db.get_last_activity('test@test.com') is not None


def test_get_last_activity():
	db = mock_db.MockDB()
	db.add_user('test@test.com', 'password')
	db.update_last_activity('test@test.com')
	assert isinstance(db.get_last_activity('test@test.com'), datetime.datetime)

