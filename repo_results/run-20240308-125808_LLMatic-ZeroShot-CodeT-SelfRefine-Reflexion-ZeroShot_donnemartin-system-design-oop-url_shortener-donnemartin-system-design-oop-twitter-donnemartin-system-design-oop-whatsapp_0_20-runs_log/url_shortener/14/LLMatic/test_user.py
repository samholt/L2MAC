import pytest
from user import User
from analytics import Analytics


def test_create_account():
	user = User('test_user')
	assert user.create_account() == {'username': 'test_user', 'urls': {}}


def test_add_url():
	user = User('test_user')
	user.add_url('short_url', 'original_url')
	assert user.view_urls() == {'short_url': 'original_url'}


def test_edit_url():
	user = User('test_user')
	user.add_url('short_url', 'original_url')
	user.edit_url('short_url', 'new_url')
	assert user.view_urls() == {'short_url': 'new_url'}


def test_delete_url():
	user = User('test_user')
	user.add_url('short_url', 'original_url')
	user.delete_url('short_url')
	assert user.view_urls() == {}


def test_view_analytics():
	user = User('test_user')
	analytics = Analytics()
	user.add_url('short_url', 'original_url')
	analytics.track('short_url', '2022-01-01T00:00:00', 'USA')
	assert user.view_analytics(analytics) == {'short_url': [{'timestamp': '2022-01-01T00:00:00', 'location': 'USA'}]}
