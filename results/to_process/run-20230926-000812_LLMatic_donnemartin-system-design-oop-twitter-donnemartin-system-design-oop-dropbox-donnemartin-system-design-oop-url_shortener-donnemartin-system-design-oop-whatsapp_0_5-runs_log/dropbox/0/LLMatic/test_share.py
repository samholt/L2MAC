from share import Share
from datetime import datetime, timedelta


def test_shareable_link():
	share = Share()
	share_id = share.generate_shareable_link('/path/to/file')
	assert share.get_shared_file(share_id) == '/path/to/file'

	share_id = share.generate_shareable_link('/path/to/file', expiry_date=datetime.now() - timedelta(days=1))
	assert share.get_shared_file(share_id) == 'Link expired'

	share_id = share.generate_shareable_link('/path/to/file', password='password')
	assert share.get_shared_file(share_id) == 'Invalid password'
	assert share.get_shared_file(share_id, password='password') == '/path/to/file'


def test_shared_folder():
	share = Share()
	share.share_folder('/path/to/folder', ['user1', 'user2'], {'user1': 'read', 'user2': 'write'})
	assert share.get_shared_folder('/path/to/folder') == {'users': ['user1', 'user2'], 'permissions': {'user1': 'read', 'user2': 'write'}}
