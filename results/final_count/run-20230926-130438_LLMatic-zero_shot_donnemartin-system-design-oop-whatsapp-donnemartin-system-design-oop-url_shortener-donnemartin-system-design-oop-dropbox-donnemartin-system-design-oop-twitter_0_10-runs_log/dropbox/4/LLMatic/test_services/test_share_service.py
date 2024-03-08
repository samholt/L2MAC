import string

from services.share_service import ShareService


def test_generate_shareable_link_for_folder():
	share_service = ShareService()
	share_id = share_service.generate_shareable_link_for_folder('test_folder', 'test@example.com', 'read')
	assert share_id in share_service.shares
	assert share_service.shares[share_id].file == 'test_folder'
	assert share_service.shares[share_id].user == 'test@example.com'
	assert share_service.shares[share_id].permissions == 'read'
