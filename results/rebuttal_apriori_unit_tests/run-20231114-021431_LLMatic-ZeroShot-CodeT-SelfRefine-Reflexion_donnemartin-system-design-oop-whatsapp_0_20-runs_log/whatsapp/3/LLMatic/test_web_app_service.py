import pytest
from web_app_service import WebAppService


def test_access_web_version():
	web_app_service = WebAppService()
	web_app_service.users['user1'] = True
	assert web_app_service.access_web_version('user1') == True
