import pytest
from services.url_shortener import URLShortener
from services.user_service import UserService
from services.admin_service import AdminService


def test_admin_service():
	url_shortener = URLShortener()
	user_service = UserService()
	admin_service = AdminService(url_shortener, user_service)

	url_shortener.shorten('https://www.google.com')
	assert len(admin_service.get_all_urls()) == 1

	user_service.create_user('test', 'password')
	assert admin_service.delete_user('test') == 'User deleted'
	assert admin_service.delete_user('invalid') == 'User not found'

	assert admin_service.delete_url('invalid') == 'URL not found'
