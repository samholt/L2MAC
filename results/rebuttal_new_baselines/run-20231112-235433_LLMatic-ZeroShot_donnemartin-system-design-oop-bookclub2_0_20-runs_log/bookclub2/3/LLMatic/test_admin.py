import pytest
import admin


def test_moderate_content_missing_data():
	admin_obj = admin.Admin()
	with pytest.raises(ValueError):
		admin_obj.moderate_content('')


def test_manage_users_missing_data():
	admin_obj = admin.Admin()
	with pytest.raises(ValueError):
		admin_obj.manage_users('', '')
