import pytest
from web_app_service import WebAppService


def test_web_application_access():
	web_app_service = WebAppService()
	user_id = 1
	assert web_app_service.access_web_version(user_id) == True
