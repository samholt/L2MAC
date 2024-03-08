import pytest
from unittest.mock import MagicMock
from controller import URLShortenerController


def test_controller():
	controller = URLShortenerController()
	controller.view.get_long_url = MagicMock(return_value='http://example.com')
	controller.create_short_url()
	assert len(controller.url_store.urls) == 1

	controller.view.get_short_url = MagicMock(return_value=list(controller.url_store.urls.keys())[0])
	controller.redirect_to_long_url()
	assert list(controller.url_store.urls.values())[0].clicks == 1

	controller.delete_expired_urls()
	assert len(controller.url_store.urls) == 1

