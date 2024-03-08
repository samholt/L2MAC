from cloudsafe.app.sharing_service import SharingService


def test_generate_share_link():
	sharing_service = SharingService()
	assert sharing_service.generate_share_link(1, file_id=1) == 'Share link generated successfully'


def test_set_expiry_date():
	sharing_service = SharingService()
	sharing_service.generate_share_link(1, file_id=1)
	assert sharing_service.set_expiry_date(1, 7) == 'Expiry date set successfully'


def test_set_password():
	sharing_service = SharingService()
	sharing_service.generate_share_link(1, file_id=1)
	assert sharing_service.set_password(1, 'password') == 'Password set successfully'


def test_invite_user():
	sharing_service = SharingService()
	assert sharing_service.invite_user(1, folder_id=1, user_id=1, permissions='read') == 'User invited successfully'


def test_set_permissions():
	sharing_service = SharingService()
	sharing_service.invite_user(1, folder_id=1, user_id=1, permissions='read')
	assert sharing_service.set_permissions(1, 'write') == 'Permissions set successfully'

