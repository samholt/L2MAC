import pytest
import user


def test_create_user_missing_data():
	with pytest.raises(ValueError):
		user.User('', '')


def test_create_profile_missing_data():
	user_obj = user.User('Test User', 'password')
	with pytest.raises(ValueError):
		user_obj.create_profile('')


def test_update_profile_missing_data():
	user_obj = user.User('Test User', 'password')
	with pytest.raises(ValueError):
		user_obj.update_profile('')


def test_follow_user_missing_data():
	user_obj = user.User('Test User', 'password')
	with pytest.raises(ValueError):
		user_obj.follow_user('')
