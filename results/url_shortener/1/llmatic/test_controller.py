import pytest
from unittest.mock import MagicMock
from controller import URLShortenerController


def test_create_short_url():
	controller = URLShortenerController()
	controller.view.get_long_url = MagicMock(return_value='https://www.example.com')
	controller.view.display_short_url = MagicMock()
	controller.create_short_url()
	assert controller.view.get_long_url.called
	assert controller.view.display_short_url.called


def test_redirect_to_long_url():
	controller = URLShortenerController()
	controller.view.get_short_url = MagicMock(return_value='abcdef')
	controller.view.redirect_to_long_url = MagicMock()
	controller.redirect_to_long_url()
	assert controller.view.get_short_url.called
	assert controller.view.redirect_to_long_url.called


def test_delete_expired_urls():
	controller = URLShortenerController()
	controller.delete_expired_urls()
	assert controller.url_store.urls == {}

