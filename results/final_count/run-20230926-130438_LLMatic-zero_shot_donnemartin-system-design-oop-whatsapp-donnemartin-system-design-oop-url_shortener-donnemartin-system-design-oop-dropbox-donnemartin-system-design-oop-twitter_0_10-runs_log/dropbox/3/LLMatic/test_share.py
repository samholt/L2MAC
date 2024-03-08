import share
import datetime


def test_shareable_link():
	share_instance = share.Share()
	link_id = share_instance.generate_shareable_link('/path/to/file')
	assert share_instance.get_shared_link(link_id) == '/path/to/file'

	link_id = share_instance.generate_shareable_link('/path/to/file', datetime.datetime.now() - datetime.timedelta(days=1))
	assert share_instance.get_shared_link(link_id) is None

	link_id = share_instance.generate_shareable_link('/path/to/file', password='password')
	assert share_instance.get_shared_link(link_id) is None
	assert share_instance.get_shared_link(link_id, 'password') == '/path/to/file'


def test_shared_folder():
	share_instance = share.Share()
	share_instance.invite_to_folder('/path/to/folder', 'user', 'read')
	assert share_instance.get_folder_permissions('/path/to/folder', 'user') == 'read'
	assert share_instance.get_folder_permissions('/path/to/folder', 'other_user') is None
